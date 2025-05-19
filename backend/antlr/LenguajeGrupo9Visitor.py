# Generated from LenguajeGrupo9.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LenguajeGrupo9Parser import LenguajeGrupo9Parser
else:
    from LenguajeGrupo9Parser import LenguajeGrupo9Parser

# This class defines a complete generic visitor for a parse tree produced by LenguajeGrupo9Parser.

class LenguajeGrupo9Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by LenguajeGrupo9Parser#programa.
    def visitPrograma(self, ctx:LenguajeGrupo9Parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#sentencia.
    def visitSentencia(self, ctx:LenguajeGrupo9Parser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#Numero.
    def visitNumero(self, ctx:LenguajeGrupo9Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#Suma.
    def visitSuma(self, ctx:LenguajeGrupo9Parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#Variable.
    def visitVariable(self, ctx:LenguajeGrupo9Parser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#Division.
    def visitDivision(self, ctx:LenguajeGrupo9Parser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#Potencia.
    def visitPotencia(self, ctx:LenguajeGrupo9Parser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#Multiplicacion.
    def visitMultiplicacion(self, ctx:LenguajeGrupo9Parser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#Agrupacion.
    def visitAgrupacion(self, ctx:LenguajeGrupo9Parser.AgrupacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeGrupo9Parser#Resta.
    def visitResta(self, ctx:LenguajeGrupo9Parser.RestaContext):
        return self.visitChildren(ctx)



del LenguajeGrupo9Parser