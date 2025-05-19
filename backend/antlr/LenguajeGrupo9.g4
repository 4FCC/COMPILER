grammar LenguajeGrupo9;

programa: sentencia+ ;

sentencia: IDENTIFICADOR ASIGNACION expresion ';' ;

expresion
    : expresion '^' expresion     #Potencia
    | expresion '*' expresion     #Multiplicacion
    | expresion '/' expresion     #Division
    | expresion '+' expresion     #Suma
    | expresion '-' expresion     #Resta
    | '{' expresion '}'           #Agrupacion
    | NUMERO                      #Numero
    | IDENTIFICADOR               #Variable
    ;

ASIGNACION: '=>';
IDENTIFICADOR: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: '-'? [0-9]+ ('.' [0-9]+)?;
ESPACIO: [ \t\r\n]+ -> skip;

// Comentarios ignorados
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
