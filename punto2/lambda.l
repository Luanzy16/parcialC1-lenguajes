%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
%}

%%

[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*lambda(\s*[a-zA-Z_][a-zA-Z0-9_]*(\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*)*)?\s*:\s*.+  { printf("Acepta\n"); return 1; }

.|\n  { yyerror("No Acepta"); }

%%

void yyerror(const char *s) {
    printf("%s\n", s);
    exit(1);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        printf("No se pudo abrir el archivo.\n");
        return 1;
    }

    yyin = file;
    yylex();
    fclose(file);

    return 0;
}
