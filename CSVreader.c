#include <stdio.h>
#define MAX_ROWS 1000
#define MAX_COLUMNS 100
#define MAX_CELL_LENGTH 256

typedef struct {
    char data[MAX_ROWS][MAX_COLUMNS][MAX_CELL_LENGTH];

    int rows;
    int columns;
} CSV;


int main(void)
{
    printf("C PROGRAM STARTED\n");

    char line[1024];

    while (fgets(line, sizeof(line), stdin) != NULL)
    {
        printf("C RECEIVED: %s", line);
    }

    printf("C PROGRAM FINISHED\n");

    return 0;
}