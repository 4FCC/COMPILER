from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

# Orígenes permitidos para CORS
origins = ["http://localhost:5173"]

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Patrones de tokens para el análisis léxico
TOKEN_PATTERNS = {
    'PALABRA_RESERVADA': r'\b(int|float|bool|char|string|if|else|for|while|print|println)\b',
    'IDENTIFICADOR': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'NUMERO': r'\b\d+(\.\d+)?\b',
    'OPERADOR_ARITMETICO': r'[+\-*/^#]',
    'OPERADOR_RELACIONAL': r'(==|!=|<=|>=|<|>)',
    'OPERADOR_LOGICO': r'(\|\||&&|!)',
    'ASIGNACION': r'=',
    'DELIMITADOR': r'[;{}()]',
    'COMENTARIO': r'//.*|/\*[\s\S]*?\*/',
    'CADENA': r'"([^"\\]|\\.)*"',
    'CARACTER': r"'.{1}'",
    'ESPACIO': r'\s+'
}

# Compilación de las expresiones regulares
TOKEN_REGEX = re.compile('|'.join(f'(?P<{key}>{value})' for key, value in TOKEN_PATTERNS.items()), re.IGNORECASE)

# Modelo de entrada
class CodigoFuente(BaseModel):
    codigo: str

# Análisis léxico
def analizador_lexico(codigo_fuente: str):
    tokens = []
    for num_linea, linea in enumerate(codigo_fuente.split('\n'), start=1):
        pos = 0
        while pos < len(linea):
            match = TOKEN_REGEX.match(linea, pos)
            if match:
                if match.lastgroup not in ['COMENTARIO', 'ESPACIO']:
                    tokens.append({
                        "tipo": match.lastgroup,
                        "valor": match.group(),
                        "linea": num_linea,
                        "columna": pos
                    })
                pos = match.end()
            else:
                tokens.append({
                    "tipo": "DESCONOCIDO", 
                    "valor": linea[pos], 
                    "linea": num_linea, 
                    "columna": pos
                })
                pos += 1

    return {"tokens": tokens}

# Ruta de la API
@app.post("/api/v1/analizador_lexico")
def analizar_codigo(codigo: CodigoFuente):
    return analizador_lexico(codigo.codigo)
