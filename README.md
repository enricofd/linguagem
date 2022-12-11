**Language EBNF:**

PROGRAM = "{", { DECLARATION }, "}" ;  
BLOCK = "{", { STATEMENT }, "}" ;  
DECLARATION = "fn", IDENTIFIER, "(", { ARGS, { ARGS, ";" } }, ")", { "->", TYPE }, BLOCK ;  
ARGS = IDENTIFIER, { ",", IDENTIFIER }, ":", TYPE ;  
STATEMENT = ({ASSIGNMENT | PRINT | RETURN }, ";") | BLOCK | WHILE | IF | TYPE ;  
RETURN = "return", RELEXPRESSION ;  
WHILE = "loop", "(", RELEXPRESSION, ")" , STATEMENT ;  
IF = "condition", "(", RELEXPRESSION, ")" , STATEMENT) , { "exception", STATEMENT } ;  
TYPE = "var", IDENTIFIER, { ",", OIDENTIFIER }, ":", ("i32" | "String") ;  
OIDENTIFIER = IDENTIFIER, "," ;  
ASSIGNMENT = IDENTIFIER, ("=", RELEXPRESSION) | FUNCCALL ;  
FUNCCALL = "(", { RELEXPRESSION , { ",", RELEXPRESSION} }, ")" ;  
PRINT = "out", "(", RELEXPRESSION, ")" ;  
EXPRESSION = TERM, { ("+" | "-" | "or"), TERM } ;  
RELEXPRESSION = FACTOR, { ("==" | ">" | "<" | "+"), FACTOR } ;  
TERM = FACTOR, { ("\*" | "/" | "and"), FACTOR } ;  
FACTOR = NUMBER | STRING | IDENTIFIER, { FUNCCALL } | ("+" | "-" | "not"), FACTOR) | "in" , "(", ")" | "(", RELEXPRESSION, ")" ;  
IDENTIFIER = LETTER, { LETTER | DIGIT | "\_" } ;  
NUMBER = DIGIT, { DIGIT } ;  
STRING = """, LETTER | DIGIT, { LETTER | DIGIT}, """;  
LETTER = ( a | ... | z | A | ... | Z ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

---

**TEST:**

Run python3 test.py
