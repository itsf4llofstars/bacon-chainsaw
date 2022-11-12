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

int isItPrime(int isPrime) {
    int chkPrime = 1;
    int halfIsPrime = isPrime / 2;

    while (1)
    {
        ++chkPrime;

        if (chkPrime >= halfIsPrime)
            return 1;
        else if (isPrime % chkPrime == 0)
            break; 
    
        ++chkPrime;
    }

    return 0;
}

int main(int argc, char **argv[]) {
    // printPrimes(2, 15);
    if (isItPrime(47)) {
        printf("47 is prime\n");
    }

    return 0;
}
