#include <stdio.h>
/**
 * Just some C code for exploring GitHub
 * */

typedef struct
{
    const char *make;
    int year;
} car; 

int main(int argc, char *argv[])
{
    car aCar = {"Chevy", 2021};
    printf("I own a %d %s Volt.\n", aCar.year, aCar.make);

    puts("");
    return 0;
}
