#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    int size;
    double *a;
    double *b;

    size = atoi(argv[1]);
    a = (double *)malloc(size * sizeof(double));
    b = (double *)malloc(size * sizeof(double));
    for (int i=0; i<size; i++) {
	a[i] = 1;
    }

    for (int i = 0; i < size; i++) {
	b[i] = asin(sin(acos(cos(atan(tan(a[i])))))) * a[i];
    }
}
