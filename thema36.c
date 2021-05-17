#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

unsigned int countBits(unsigned long long n) {
    unsigned int count = 0;
    while (n) {
        count += 1;
        n >>= 1;
    }
    return count;
}

int findDivisors(unsigned long long n) {
    int half_length = countBits(n)/2;
    unsigned long long n1 = 1L<<half_length-1;
    unsigned long long n2 = 1L<<half_length+1;

    unsigned long long i = n1;
    unsigned long long upper_limit = (unsigned long long)sqrt((double)n);

    while (i <= upper_limit) {
        if (n % i == 0) {
            return 1;
        }
        i++;
    }
    return 0;
}

unsigned long long ullrand() {
    union num {
        unsigned long long ull;
        unsigned short int usi[4];
    } res;

    for (int i = 0; i < 4; ++i)
        res.usi[i] = rand() % 65536;
    // force 1st bit = 1
    res.usi[3] |= 32768; 

    return res.ull;
}

int main(void) {
    time_t t;

    int K = 30;
    int ones = 0;
    unsigned ut = (unsigned) time(&t);
    srand(ut);
    printf("srand = %u\n", ut);
 
    for (int i = 0; i < K; i++) {
        unsigned long long n = ullrand();
        ones += findDivisors(n);
        printf("%d: %d (%llu)\n", i, ones, n);
    }
    printf("(%f", ones/(float)K);

    return 0;
}
