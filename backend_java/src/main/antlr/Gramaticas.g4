
grammar Gramaticas;

program     :   (asignacion)* EOF ;

asignacion  :   IDENTIFICADOR ASIGNADOR expresion PYC ;

expresion   :   termino (OPERADOR_ARITMETICO termino)* ;

termino     :   NUMERO
            |   IDENTIFICADOR
            |   AGRUPADOR_I expresion AGRUPADOR_D ;

ASIGNADOR   :   '=>' ;
OPERADOR_ARITMETICO : '+' | '-' | '*' | '/' | '^' ;

AGRUPADOR_I :   '{' ;
AGRUPADOR_D :   '}' ;
PYC         :   ';' ;

IDENTIFICADOR : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMERO      : [0-9]+ ('.' [0-9]+)? ;
ESPACIO     : [ \t\r\n]+ -> skip ;
