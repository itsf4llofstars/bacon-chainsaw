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

// Count the prime numbers between start and stop
int countPrimes(int start, int stop) {
    int chkPrime = 1;
    int primes = 0;
    int nonPrimes = 0;

    while (start < stop) {
        ++chkPrime;

        if (chkPrime >= (start / 2)) {
            ++primes;
            ++start;
            chkPrime = 1;
        }
        else if (!(start % chkPrime)) {
            ++nonPrimes;
            ++start;
            chkPrime = 1;
        }
    }

    printf("Between %d and %d, there are %d prime numbers and %d non-prime numbers.\n", star, stop, primes, nonPrimes);
    return primes;
}

int main(int argc, char **argv[]) {
    printPrimes(2, 15);
    int itsPrime = isItPrime(47);
    int numPrimes = countPrimes(2, 47);

    return 0;
}
