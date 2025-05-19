
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from antlr4 import *
from antlr.LenguajeGrupo9Lexer import LenguajeGrupo9Lexer
from antlr.LenguajeGrupo9Parser import LenguajeGrupo9Parser
from EvaluadorVisitor import EvaluadorVisitor
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class CodigoFuente(BaseModel):
    codigo: str

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

def eliminar_comentarios(codigo: str) -> str:
    codigo = re.sub(r'//.*', '', codigo)
    codigo = re.sub(r'/\*[\s\S]*?\*/', '', codigo)
    return codigo

def analizador_lexico(codigo_fuente: str):
    codigo_fuente = eliminar_comentarios(codigo_fuente)
    tokens = []
    tabla_simbolos = []
    errores = []
    TOKEN_REGEX = re.compile('|'.join(f'(?P<{key}>{value})' for key, value in TOKEN_PATTERNS.items()), re.IGNORECASE)

    for num_linea, linea in enumerate(codigo_fuente.split('\n'), start=1):
        pos = 0
        while pos < len(linea):
            match = TOKEN_REGEX.match(linea, pos)
            if match:
                tipo_token = match.lastgroup
                valor = match.group()
                if tipo_token == 'ESPACIO':
                    pos = match.end()
                    continue
                token_info = {
                    "tipo": tipo_token,
                    "valor": valor,
                    "linea": num_linea,
                    "columna": pos
                }
                tokens.append(token_info)
                if tipo_token == 'IDENTIFICADOR':
                    if not any(sim['valor'] == valor for sim in tabla_simbolos):
                        tabla_simbolos.append(token_info)
                pos = match.end()
            else:
                errores.append({
                    "descripcion": f'Error léxico en línea {num_linea} y columna {pos}: el carácter “{linea[pos]}” es inválido.',
                    "linea": num_linea,
                    "columna": pos,
                    "valor": linea[pos]
                })
                pos += 1

    return {
        "tokens": tokens,
        "tabla_simbolos": tabla_simbolos,
        "errores": errores
    }

@app.post("/api/v1/analizador_lexico")
def analizar_codigo(codigo: CodigoFuente):
    return analizador_lexico(codigo.codigo)

@app.post("/api/v1/analizador_sintactico")
def analizar_sintaxis(codigo: CodigoFuente):
    errores = analizador_lexico(codigo.codigo)["errores"]
    if errores:
        return {"errores": errores}

    try:
        input_stream = InputStream(codigo.codigo)
        lexer = LenguajeGrupo9Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = LenguajeGrupo9Parser(stream)

        tree = parser.programa()
        visitor = EvaluadorVisitor()
        resultado = visitor.visit(tree)

        return {
            "evaluacion": resultado,
            "errores": []
        }
    except Exception as e:
        return {
            "evaluacion": {},
            "errores": [{"descripcion": str(e)}]
        }
