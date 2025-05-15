
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
    'ASIGNACION': r'(==|<-|=>|=)',
    'DELIMITADOR': r'[;{}\[\]\(\)]',
    'COMENTARIO': r'//.*|/\*[\s\S]*?\*/',
    'CADENA': r'"([^"\\]|\\.)*"',
    'CARACTER': r"'.{1}'",
    'ESPACIO': r'\s+'
}

TOKEN_REGEX = re.compile('|'.join(f'(?P<{key}>{value})' for key, value in TOKEN_PATTERNS.items()), re.IGNORECASE)

def analizador_lexico(codigo_fuente: str):
    tokens = []
    tabla_simbolos = []
    errores = []

    for num_linea, linea in enumerate(codigo_fuente.split('\n'), start=1):
        pos = 0
        while pos < len(linea):
            match = TOKEN_REGEX.match(linea, pos)
            if match:
                tipo_token = match.lastgroup
                valor = match.group()
                if tipo_token not in ['COMENTARIO', 'ESPACIO']:
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

def es_expresion_valida(tokens):
    pila = []
    prev = None
    for tok in tokens:
        if tok['tipo'] in ['NUMERO', 'IDENTIFICADOR']:
            if prev in ['NUMERO', 'IDENTIFICADOR']:
                return False
        elif tok['tipo'] == 'OPERADOR_ARITMETICO':
            if prev is None or prev in ['OPERADOR_ARITMETICO']:
                return False
        elif tok['valor'] in ['(', '[', '{']:
            pila.append(tok['valor'])
        elif tok['valor'] in [')', ']', '}']:
            if not pila:
                return False
            abre = pila.pop()
            if not ((abre == '(' and tok['valor'] == ')') or (abre == '[' and tok['valor'] == ']') or (abre == '{' and tok['valor'] == '}')):
                return False
        prev = tok['tipo']
    return not pila and prev not in ['OPERADOR_ARITMETICO']

def evaluar_expresion_con_variables(tokens, variables):
    expr = ''
    try:
        for tok in tokens:
            if tok['tipo'] == 'IDENTIFICADOR':
                if tok['valor'] in variables:
                    expr += str(variables[tok['valor']])
                else:
                    return f"Error: variable '{tok['valor']}' no definida"
            elif tok['tipo'] == 'NUMERO' or tok['tipo'] == 'DELIMITADOR' or tok['tipo'] == 'OPERADOR_ARITMETICO':
                expr += tok['valor']
        expr = expr.replace('^', '**').replace('#', '%')
        return eval(expr)
    except Exception:
        return "Error de evaluación"

@app.post("/api/v1/analizador_lexico")
def analizar_codigo(codigo: CodigoFuente):
    return analizador_lexico(codigo.codigo)

@app.post("/api/v1/analizador_sintactico")
def analizar_sintaxis(codigo: CodigoFuente):
    analisis = analizador_lexico(codigo.codigo)
    tokens = analisis["tokens"]
    errores = analisis["errores"]
    resultado = None
    variables = {}
    evaluaciones = {}

    if errores:
        return {"errores": errores}

    i = 0
    while i < len(tokens):
        if i + 3 >= len(tokens):
            errores.append({"descripcion": "Sentencia incompleta o mal formada."})
            break

        if tokens[i]['tipo'] != 'IDENTIFICADOR' or tokens[i + 1]['tipo'] != 'ASIGNACION':
            errores.append({"descripcion": f"Error en asignación en línea {tokens[i]['linea']}."})
            break

        nombre_var = tokens[i]['valor']
        j = i + 2
        expresion = []
        while j < len(tokens) and tokens[j]['valor'] != ';':
            expresion.append(tokens[j])
            j += 1

        if j == len(tokens) or tokens[j]['valor'] != ';':
            errores.append({"descripcion": f"Falta punto y coma al final de la instrucción en línea {tokens[i]['linea']}."})
            break

        if not es_expresion_valida(expresion):
            errores.append({"descripcion": f"Expresión inválida en línea {tokens[i]['linea']}."})
            break

        evaluado = evaluar_expresion_con_variables(expresion, variables)
        if isinstance(evaluado, str) and evaluado.startswith("Error"):
            errores.append({"descripcion": evaluado})
            break

        variables[nombre_var] = evaluado
        evaluaciones[nombre_var] = evaluado
        i = j + 1

    return {
        "tokens": tokens,
        "tabla_simbolos": analisis["tabla_simbolos"],
        "errores": errores,
        "evaluacion": evaluaciones
    }