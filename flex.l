%{
#include <stdio.h>
#include <string.h>
%}

%%

[ \t\n]               

"*"                   return MULT;
"/"                   return DIV;
"+"                   return PLUS;
"-"                   return MINUS;

"("                   return LPAR;
")"                   return RPAR;
"{"                   return LCB;
"}"                   return RCB;

"="                   return ASSIGNEMENT;
"var"                 return VAR;
","                   return COMMA;
":"                   return DEFINE;
";"                   return SEMI;
"return"              return RETURN;

">"                   return BIG;
"<"                   return SMALL;
">="                  return BIGEQ;
"<="                  return SMALLEQ;
"=="                  return EQUAL;
"!="                  return DIFF;
"or"                  return OR;
"and"                 return AND;
"not"                 return NOT;

"condition"           return IF;
"exception"           return ELSE;
"loop"                return WHILE;

"in"                  return READ;
"out"                 return PRINT;

"i32"                 return INTTYPE;
"String"              return STRTYPE;
"Float"               return FLOATTYPE;
"Void"                return VOIDTYPE;

[0-9]+                return INT;
[a-z0-9]              return STR;
[0-9]*[.][0-9]        return FLOAT;
[a-z][_a-z0-9]        return ID;

.                     printf("Token not acceptable!"); yyterminate();

%%