%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("Error: %s\n", s); }
%}

%token INT STR FLOAT ID
%token INTTYPE STRTYPE VOIDTYPE
%token READ PRINT IF ELSE WHILE
%token BIG SMALL EQUAL OR AND NOT
%token ASSIGNEMENT VAR COMMA DEFINE SEMI RETURN
%token LPAR RPAR LCB RCB MULT DIV PLUS MINUS

%start syntax

%%

syntax : def block
       | block
       ;

types : INTTYPE
      | STRTYPE
      | VOIDTYPE
      ;

def : types ID LPAR optional_argument RPAR block return_value SEMI ;

optional_argument :
                  | types ID
                  | types ID COMMA optional_argument
                  ;

return_value :
             | RETURN values
             ;

values : ID
       | STR
       | INT
       ;

block : LCB statement RCB
      | LCB RCB
      ;

statement : assign SEMI
          | print SEMI
          | block
          | if_condition
          | while_loop
          | type
          ;

assign : ID ASSIGNEMENT relexpression ;

print: PRINT LPAR relexpression RPAR ;

if_condition : IF LPAR relexpression RPAR statement else_condition ;

else_condition : ELSE statement | SEMI ;

while_loop : WHILE LPAR relexpression RPAR statement ;

type : VAR ID optional_id optional_type ;

optional_id :
            | ID COMMA
            ;

optional_type :
              | DEFINE types ;

relexpression : expression
              | expression BIG expression
              | expression SMALL expression
              | expression EQUAL expression
              ;

expression : term
           | term PLUS term
           | term MINUS term
           | term OR term
           ;

term : factor
     | factor MULT factor
     | factor DIV factor
     | factor AND factor
     ;

factor : FLOAT
       | INT
       | STR
       | ID
       | PLUS factor
       | MINUS factor
       | NOT factor
       | READ LPAR RPAR
       | LPAR relexpression RPAR
       ;

%%

int main(){
  yyparse();
  return 0;
}