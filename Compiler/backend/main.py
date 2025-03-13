from fastapi import FastAPI  # Importación del framework FastAPI para crear la API
from fastapi.middleware.cors import CORSMiddleware  # Middleware para habilitar CORS
from pydantic import BaseModel  # Librería para validar datos con Pydantic
import re  # Módulo de expresiones regulares

# Lista de orígenes permitidos para CORS
origins = [
    "http://localhost:5173",
]

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Configuración de middleware CORS
app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,  # Permitir acceso solo desde los orígenes definidos
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"]   # Permitir todos los encabezados
)

# Diccionario con los patrones de expresión regular para los diferentes tipos de tokens
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

# Compilación de todas las expresiones regulares en un solo patrón
TOKEN_REGEX = re.compile('|'.join(f'(?P<{key}>{value})' for key, value in TOKEN_PATTERNS.items()), re.IGNORECASE)

# Definición del modelo para el cuerpo de la solicitud (código fuente en formato de texto)
class CodigoFuente(BaseModel):
    codigo: str

# Función que realiza el análisis léxico del código fuente
def analizador_lexico(codigo_fuente: str):
    tokens = []
    # Se divide el código en líneas para procesarlas
    for num_linea, linea in enumerate(codigo_fuente.split('\n'), start=1):
        pos = 0
        while pos < len(linea):
            match = TOKEN_REGEX.match(linea, pos)  # Intenta hacer coincidir cada token con las expresiones regulares
            if match:
                # Si el token no es un comentario ni un espacio, se añade a la lista de tokens
                if match.lastgroup not in ['COMENTARIO', 'ESPACIO']:
                    tokens.append({
                        "tipo": match.lastgroup,  # Tipo de token
                        "valor": match.group(),  # Valor del token
                        "linea": num_linea,  # Línea del código donde se encuentra el token
                        "columna": pos  # Posición en la línea donde comienza el token
                    })
                pos = match.end()  # Avanzar la posición en la línea
            else:
                # Si no hay coincidencia, se considera un token desconocido
                tokens.append({
                    "tipo": "DESCONOCIDO", 
                    "valor": linea[pos], 
                    "linea": num_linea, 
                    "columna": pos
                })
                pos += 1

    return {"tokens": tokens}  # Devuelve los tokens encontrados

# Ruta de la API para analizar el código fuente (POST)
@app.post("/api/v1/analizador_lexico")
def analizar_codigo(codigo: CodigoFuente):
    return analizador_lexico(codigo.codigo)  # Llama a la función de análisis léxico
