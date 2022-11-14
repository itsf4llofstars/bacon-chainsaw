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

// Determine if isPrime is a prime number
int isItPrime(int *isPrime) {
    int chkPrime = 1;

    while (++chkPrime < (*isPrime / 2))
        if (*isPrime % chkPrime == 0)
            return 0;

    return 1;
}

int main(int argc, char **argv[]) {
    printPrimes(2, 15);

    int number = 25;
    if (isItPrime(&number))
        printf("%d is prime\n", number);
    else
        printf("%d is not prime\n", number);

    return 0;
}
