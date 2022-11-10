----------

**Language EBNF:**

SYNTAX = { DEF }, BLOCK ;  
DEF = ("i32" | "String" | "Void" | Float"), IDENTIFIER, "(", { ATT, { ",", ATT } }, ")", BLOCK , { "return", { IDENTIFIER | FLOAT | INT | STRING } }, ";" ;
ATT = ("i32" | "String" | "Float"), IDENTIFIER ;  
BLOCK = "{", { STATEMENT }, "}" ;  
STATEMENT = ( { ASSIGNMENT | PRINT }, ";") | BLOCK | WHILE | IF | TYPE ;
WHILE = "loop", "(", RELEXPRESSION, ")" , STATEMENT ;  
IF = "condition", "(", RELEXPRESSION, ")" , STATEMENT) , { "exception", STATEMENT } ;  
TYPE = "var", IDENTIFIER, { ",", OIDENTIFIER }, { ":", ("i32" | "String" | "Float") } ;  
OIDENTIFIER = IDENTIFIER, "," ;  
ASSIGNMENT = IDENTIFIER, "=", RELEXPRESSION ;  
PRINT = "out", "(", RELEXPRESSION, ")" ;  
EXPRESSION = TERM, { ("+" | "-" | "or" ), TERM } ;  
RELEXPRESSION = EXPRESSION, { ("==" | "!=" | ">" | "<" | ">=" | "<=" | "+"), EXPRESSION } ;  
TERM = FACTOR, { ("\*" | "/" | "and"), FACTOR } ;  
FACTOR = FLOAT | INT | STRING | IDENTIFIER | ("+" | "-" | "not"), FACTOR) | "in", "(", ")" | "(", RELEXPRESSION, ")" ;
IDENTIFIER = LETTER, { LETTER | "\_" } ;  
FLOAT = { DIGIT }, ".", DIGIT ;
INT = DIGIT ;
STRING = """, { LETTER | DIGIT}, """ ;
LETTER = ( a | ... | z  ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

-----------
