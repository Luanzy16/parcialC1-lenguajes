grammar cal;

// Reglas léxicas
REAL      : '-'?[0-9]+('.'[0-9]+)? ;
IMAGINARY : '-'?[0-9]+('.'[0-9]+)? ('i' | 'j') ;
WS        : [ \t\r\n]+ -> skip ;
PLUS      : '+' ;
MINUS     : '-' ;
MUL       : '*' ;
DIV       : '/' ;
LPAREN    : '(' ;
RPAREN    : ')' ;

// Reglas sintácticas
expr    : expr PLUS expr   # Add
        | expr MINUS expr  # Sub
        | expr MUL expr    # Mul
        | expr DIV expr    # Div
        | REAL             # Real
        | IMAGINARY        # Imaginary
        | LPAREN expr RPAREN  # Parens
        ;
