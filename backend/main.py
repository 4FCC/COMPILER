# Importación de FastAPI para crear el servidor web
from fastapi import FastAPI
# Permite configurar CORS (para que otros dominios puedan acceder al backend, como el frontend en React)
from fastapi.middleware.cors import CORSMiddleware
# BaseModel se usa para definir el esquema de entrada de datos
from pydantic import BaseModel

# Importaciones de ANTLR
from antlr4 import *  # Librería base de ANTLR para Python
from antlr.LenguajeGrupo9Lexer import LenguajeGrupo9Lexer  # Analizador léxico generado por ANTLR
from antlr.LenguajeGrupo9Parser import LenguajeGrupo9Parser  # Analizador sintáctico generado por ANTLR
from EvaluadorVisitor import EvaluadorVisitor  # Visitor personalizado para evaluar expresiones

# Librería para expresiones regulares (usada en análisis léxico manual)
import re

# Se crea la aplicación FastAPI
app = FastAPI()

# Se configura CORS para permitir peticiones desde el frontend (en localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Clase de entrada de datos, que espera un campo llamado "codigo" con una cadena
class CodigoFuente(BaseModel):
    codigo: str

# Diccionario de patrones de tokens con expresiones regulares
# Se utiliza para hacer el análisis léxico personalizado antes de pasar a ANTLR
TOKEN_PATTERNS = {
    'PALABRA_RESERVADA': r'\b(int|float|bool|char|string|if|else|for|while|print|println|EscribirLinea|Escribir|Longitud|aCadena)\b',
    'IDENTIFICADOR': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'NUMERO': r'-?\b\d+(\.\d+)?\b',
    'OPERADOR_ARITMETICO': r'(\+\+|--|[+\-*/^#])',
    'OPERADOR_RELACIONAL': r'(==|!=|<=|>=|<|>)',
    'OPERADOR_LOGICO': r'(\|\||&&|!)',
    'ASIGNACION': r'(==|<-|=>)',
    'DELIMITADOR': r'[;{}\[\]\(\)]',
    'CADENA': r'"([^"\\]|\\.)*"',
    'CARACTER': r"'.{1}'",
    'ESPACIO': r'\s+'
}

# Función que elimina los comentarios (tanto de una línea como multilínea) usando regex
def eliminar_comentarios(codigo: str) -> str:
    codigo = re.sub(r'//.*', '', codigo)
    codigo = re.sub(r'/\*[\s\S]*?\*/', '', codigo)
    return codigo

# Función que realiza el análisis léxico: detecta tokens, tabla de símbolos y errores
def analizador_lexico(codigo_fuente: str):
    codigo_fuente = eliminar_comentarios(codigo_fuente)
    tokens = []
    tabla_simbolos = []
    errores = []

    # Se compilan todos los patrones en una sola expresión
    TOKEN_REGEX = re.compile('|'.join(f'(?P<{key}>{value})' for key, value in TOKEN_PATTERNS.items()), re.IGNORECASE)

    # Se analiza línea por línea
    for num_linea, linea in enumerate(codigo_fuente.split('\n'), start=1):
        pos = 0
        while pos < len(linea):
            match = TOKEN_REGEX.match(linea, pos)
            if match:
                tipo_token = match.lastgroup
                valor = match.group()
                if tipo_token == 'ESPACIO':
                    pos = match.end()
                    continue  # Se ignoran los espacios

                token_info = {
                    "tipo": tipo_token,
                    "valor": valor,
                    "linea": num_linea,
                    "columna": pos
                }
                tokens.append(token_info)

                # Si es un identificador nuevo, se guarda en la tabla de símbolos
                if tipo_token == 'IDENTIFICADOR':
                    if not any(sim['valor'] == valor for sim in tabla_simbolos):
                        tabla_simbolos.append(token_info)

                pos = match.end()
            else:
                # Si no coincide con ningún patrón, se reporta como error léxico
                errores.append({
                    "descripcion": f'Error léxico en línea {num_linea} y columna {pos}: el carácter “{linea[pos]}” es inválido.',
                    "linea": num_linea,
                    "columna": pos,
                    "valor": linea[pos]
                })
                pos += 1

    # Validación manual para marcar error si se usan paréntesis `()` (grupo 9 solo acepta `{}`)
    for t in tokens:
        if t["valor"] == "(" or t["valor"] == ")":
            errores.append({
                "descripcion": f"Agrupador '{t['valor']}' inválido para grupo 9. Solo se permite '{{}}'.",
                "linea": t["linea"],
                "columna": t["columna"],
                "valor": t["valor"]
            })

    return {
        "tokens": tokens,
        "tabla_simbolos": tabla_simbolos,
        "errores": errores
    }

# Ruta POST para análisis léxico
@app.post("/api/v1/analizador_lexico")
def analizar_codigo(codigo: CodigoFuente):
    return analizador_lexico(codigo.codigo)

# Ruta POST para análisis sintáctico y evaluación con ANTLR
@app.post("/api/v1/analizador_sintactico")
def analizar_sintaxis(codigo: CodigoFuente):
    # Primero se ejecuta el análisis léxico personalizado
    errores = analizador_lexico(codigo.codigo)["errores"]
    if errores:
        # Si hay errores léxicos, se devuelven sin pasar al análisis sintáctico
        return {"errores": errores}

    try:
        # Entrada del texto como stream
        input_stream = InputStream(codigo.codigo)
        lexer = LenguajeGrupo9Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = LenguajeGrupo9Parser(stream)

        # Se genera el árbol sintáctico a partir del punto de entrada de la gramática
        tree = parser.programa()

        # Se visita el árbol sintáctico con nuestro Visitor personalizado
        visitor = EvaluadorVisitor()
        resultado = visitor.visit(tree)

        # Se devuelve el resultado final de la evaluación
        return {
            "evaluacion": resultado,
            "errores": []
        }

    except Exception as e:
        # Si ocurre un error interno durante el análisis, se reporta
        return {
            "evaluacion": {},
            "errores": [{"descripcion": str(e)}]
        }
