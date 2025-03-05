#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s <archivo> <palabra_clave>n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    char word[100];
    int count = 0;

    while (fscanf(file, "%s", word) == 1) {
        if (strcmp(word, argv[2]) == 0) {
            count++;
        }
    }

    fclose(file);
    printf("'%s' se repite %d veces en el texto.\n", argv[2], count);

    return 0;
}