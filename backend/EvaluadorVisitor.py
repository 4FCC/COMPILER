
from antlr4 import *
from antlr.LenguajeGrupo9Visitor import LenguajeGrupo9Visitor
from antlr.LenguajeGrupo9Parser import LenguajeGrupo9Parser

class EvaluadorVisitor(LenguajeGrupo9Visitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx:LenguajeGrupo9Parser.ProgramaContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.variables

    def visitSentencia(self, ctx:LenguajeGrupo9Parser.SentenciaContext):
        nombre_var = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.variables[nombre_var] = valor

    def visitPotencia(self, ctx:LenguajeGrupo9Parser.PotenciaContext):
        return self.visit(ctx.expresion(0)) ** self.visit(ctx.expresion(1))

    def visitMultiplicacion(self, ctx:LenguajeGrupo9Parser.MultiplicacionContext):
        return self.visit(ctx.expresion(0)) * self.visit(ctx.expresion(1))

    def visitDivision(self, ctx:LenguajeGrupo9Parser.DivisionContext):
        return self.visit(ctx.expresion(0)) / self.visit(ctx.expresion(1))

    def visitSuma(self, ctx:LenguajeGrupo9Parser.SumaContext):
        return self.visit(ctx.expresion(0)) + self.visit(ctx.expresion(1))

    def visitResta(self, ctx:LenguajeGrupo9Parser.RestaContext):
        return self.visit(ctx.expresion(0)) - self.visit(ctx.expresion(1))

    def visitAgrupacion(self, ctx:LenguajeGrupo9Parser.AgrupacionContext):
        return self.visit(ctx.expresion())

    def visitNumero(self, ctx:LenguajeGrupo9Parser.NumeroContext):
        texto = ctx.NUMERO().getText()
        return float(texto) if '.' in texto else int(texto)

    def visitVariable(self, ctx:LenguajeGrupo9Parser.VariableContext):
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre not in self.variables:
            raise Exception(f"Variable '{nombre}' no definida")
        return self.variables[nombre]
