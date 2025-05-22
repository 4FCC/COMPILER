# Generated from LenguajeGrupo9.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,46,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,24,8,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,41,8,2,10,
        2,12,2,44,9,2,1,2,0,1,4,3,0,2,4,0,0,50,0,7,1,0,0,0,2,11,1,0,0,0,
        4,23,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,
        1,0,0,0,10,1,1,0,0,0,11,12,5,10,0,0,12,13,5,9,0,0,13,14,3,4,2,0,
        14,15,5,1,0,0,15,3,1,0,0,0,16,17,6,2,-1,0,17,18,5,7,0,0,18,19,3,
        4,2,0,19,20,5,8,0,0,20,24,1,0,0,0,21,24,5,11,0,0,22,24,5,10,0,0,
        23,16,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,42,1,0,0,0,25,26,10,
        8,0,0,26,27,5,2,0,0,27,41,3,4,2,9,28,29,10,7,0,0,29,30,5,3,0,0,30,
        41,3,4,2,8,31,32,10,6,0,0,32,33,5,4,0,0,33,41,3,4,2,7,34,35,10,5,
        0,0,35,36,5,5,0,0,36,41,3,4,2,6,37,38,10,4,0,0,38,39,5,6,0,0,39,
        41,3,4,2,5,40,25,1,0,0,0,40,28,1,0,0,0,40,31,1,0,0,0,40,34,1,0,0,
        0,40,37,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,5,1,
        0,0,0,44,42,1,0,0,0,4,9,23,40,42
    ]

class LenguajeGrupo9Parser ( Parser ):

    grammarFileName = "LenguajeGrupo9.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'^'", "'*'", "'/'", "'+'", "'-'", 
                     "'{'", "'}'", "'=>'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ASIGNACION", "IDENTIFICADOR", "NUMERO", 
                      "ESPACIO", "LINE_COMMENT", "BLOCK_COMMENT", "PARENTESIS_IZQ", 
                      "PARENTESIS_DER" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_expresion = 2

    ruleNames =  [ "programa", "sentencia", "expresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ASIGNACION=9
    IDENTIFICADOR=10
    NUMERO=11
    ESPACIO=12
    LINE_COMMENT=13
    BLOCK_COMMENT=14
    PARENTESIS_IZQ=15
    PARENTESIS_DER=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeGrupo9Parser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LenguajeGrupo9Parser.SentenciaContext,i)


        def getRuleIndex(self):
            return LenguajeGrupo9Parser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = LenguajeGrupo9Parser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.sentencia()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeGrupo9Parser.IDENTIFICADOR, 0)

        def ASIGNACION(self):
            return self.getToken(LenguajeGrupo9Parser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeGrupo9Parser.ExpresionContext,0)


        def getRuleIndex(self):
            return LenguajeGrupo9Parser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = LenguajeGrupo9Parser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(LenguajeGrupo9Parser.IDENTIFICADOR)
            self.state = 12
            self.match(LenguajeGrupo9Parser.ASIGNACION)
            self.state = 13
            self.expresion(0)
            self.state = 14
            self.match(LenguajeGrupo9Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LenguajeGrupo9Parser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeGrupo9Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(LenguajeGrupo9Parser.NUMERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)


    class SumaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeGrupo9Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeGrupo9Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeGrupo9Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeGrupo9Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeGrupo9Parser.IDENTIFICADOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class DivisionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeGrupo9Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeGrupo9Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeGrupo9Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)


    class PotenciaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeGrupo9Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeGrupo9Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeGrupo9Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencia" ):
                listener.enterPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencia" ):
                listener.exitPotencia(self)


    class MultiplicacionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeGrupo9Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeGrupo9Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeGrupo9Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacion" ):
                listener.enterMultiplicacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacion" ):
                listener.exitMultiplicacion(self)


    class AgrupacionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeGrupo9Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeGrupo9Parser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgrupacion" ):
                listener.enterAgrupacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgrupacion" ):
                listener.exitAgrupacion(self)


    class RestaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeGrupo9Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeGrupo9Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeGrupo9Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResta" ):
                listener.enterResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResta" ):
                listener.exitResta(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LenguajeGrupo9Parser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = LenguajeGrupo9Parser.AgrupacionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 17
                self.match(LenguajeGrupo9Parser.T__6)
                self.state = 18
                self.expresion(0)
                self.state = 19
                self.match(LenguajeGrupo9Parser.T__7)
                pass
            elif token in [11]:
                localctx = LenguajeGrupo9Parser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(LenguajeGrupo9Parser.NUMERO)
                pass
            elif token in [10]:
                localctx = LenguajeGrupo9Parser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(LenguajeGrupo9Parser.IDENTIFICADOR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 40
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = LenguajeGrupo9Parser.PotenciaContext(self, LenguajeGrupo9Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 25
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 26
                        self.match(LenguajeGrupo9Parser.T__1)
                        self.state = 27
                        self.expresion(9)
                        pass

                    elif la_ == 2:
                        localctx = LenguajeGrupo9Parser.MultiplicacionContext(self, LenguajeGrupo9Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 28
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 29
                        self.match(LenguajeGrupo9Parser.T__2)
                        self.state = 30
                        self.expresion(8)
                        pass

                    elif la_ == 3:
                        localctx = LenguajeGrupo9Parser.DivisionContext(self, LenguajeGrupo9Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        self.match(LenguajeGrupo9Parser.T__3)
                        self.state = 33
                        self.expresion(7)
                        pass

                    elif la_ == 4:
                        localctx = LenguajeGrupo9Parser.SumaContext(self, LenguajeGrupo9Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        self.match(LenguajeGrupo9Parser.T__4)
                        self.state = 36
                        self.expresion(6)
                        pass

                    elif la_ == 5:
                        localctx = LenguajeGrupo9Parser.RestaContext(self, LenguajeGrupo9Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 37
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 38
                        self.match(LenguajeGrupo9Parser.T__5)
                        self.state = 39
                        self.expresion(5)
                        pass

             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




