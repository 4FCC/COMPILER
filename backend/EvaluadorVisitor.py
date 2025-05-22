# Importación de herramientas base de ANTLR
from antlr4 import *

# Importa la clase base Visitor generada automáticamente por ANTLR
from antlr.LenguajeGrupo9Visitor import LenguajeGrupo9Visitor
# Importa los contextos de la gramática, necesarios para saber qué tipo de nodo estás visitando
from antlr.LenguajeGrupo9Parser import LenguajeGrupo9Parser

# Clase personalizada que hereda del Visitor generado por ANTLR
class EvaluadorVisitor(LenguajeGrupo9Visitor):

    # Constructor: crea un diccionario para guardar variables y sus valores
    def __init__(self):
        self.variables = {}

    # Visita el nodo raíz del árbol: 'programa' que contiene varias sentencias
    def visitPrograma(self, ctx:LenguajeGrupo9Parser.ProgramaContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)  # visita cada sentencia individualmente
        return self.variables  # devuelve el diccionario de variables evaluadas

    # Visita una sentencia como: a => 5;
    def visitSentencia(self, ctx:LenguajeGrupo9Parser.SentenciaContext):
        nombre_var = ctx.IDENTIFICADOR().getText()  # obtiene el nombre de la variable
        valor = self.visit(ctx.expresion())  # evalúa el valor asignado
        self.variables[nombre_var] = valor  # guarda la variable con su valor en el diccionario

    # Visita una expresión con potencia: x ^ y
    def visitPotencia(self, ctx:LenguajeGrupo9Parser.PotenciaContext):
        return self.visit(ctx.expresion(0)) ** self.visit(ctx.expresion(1))  # evalúa base y exponente

    # Visita una multiplicación: x * y
    def visitMultiplicacion(self, ctx:LenguajeGrupo9Parser.MultiplicacionContext):
        return self.visit(ctx.expresion(0)) * self.visit(ctx.expresion(1))

    # Visita una división: x / y
    def visitDivision(self, ctx:LenguajeGrupo9Parser.DivisionContext):
        return self.visit(ctx.expresion(0)) / self.visit(ctx.expresion(1))

    # Visita una suma: x + y
    def visitSuma(self, ctx:LenguajeGrupo9Parser.SumaContext):
        return self.visit(ctx.expresion(0)) + self.visit(ctx.expresion(1))

    # Visita una resta: x - y
    def visitResta(self, ctx:LenguajeGrupo9Parser.RestaContext):
        return self.visit(ctx.expresion(0)) - self.visit(ctx.expresion(1))

    # Visita una agrupación con llaves: { x + y }
    def visitAgrupacion(self, ctx:LenguajeGrupo9Parser.AgrupacionContext):
        return self.visit(ctx.expresion())  # simplemente evalúa lo que está dentro de las llaves

    # Visita un número (puede ser entero o decimal)
    def visitNumero(self, ctx:LenguajeGrupo9Parser.NumeroContext):
        texto = ctx.NUMERO().getText()  # obtiene el texto del número
        return float(texto) if '.' in texto else int(texto)  # convierte a float o int según corresponda

    # Visita una variable: x
    def visitVariable(self, ctx:LenguajeGrupo9Parser.VariableContext):
        nombre = ctx.IDENTIFICADOR().getText()  # obtiene el nombre de la variable
        if nombre not in self.variables:
            raise Exception(f"Variable '{nombre}' no definida")  # si no existe, lanza error
        return self.variables[nombre]  # devuelve su valor guardado
