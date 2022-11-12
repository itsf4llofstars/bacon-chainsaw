#include <stdio.h>
// Some funcitons to calculate prime numbers

// Print prime numbers from start to stop
void printPrimes(int start, int stop) {
    int chkPrime = 1;

    while (start < stop) {
        ++chkPrime;

        if (!(start % chkPrime)) {
            if (start == chkPrime)
                printf("Prime: %d\n", start);

            ++start;
            chkPrime = 1;
        }
    }
}

int main(int argc, char **argv[]) {
    printPrimes(2, 15);

    return 0;
}
