#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_MAX 30000

void insertion_sort(int *a, int n){
    /* variable declarations */
    int i, j, key;

    for (i = 1; i < n; i++){
        /* for each item in the array, except the first */
        key = a[i];
        j = i - 1;
        /* shift item to the right until it either
         * comes after a smaller value, or is in the 0 position*/
        while (j >= 0 && a[j] > key){
            a[j+1] = a[j];
            j--;
        }
        /* move the key along one */
        a[j+1] = key;
    }
}

int main(void){
    int my_array[ARRAY_MAX];
    clock_t start, end;
    int i, count = 0;

    while (count < ARRAY_MAX && scanf("%d", &my_array[count]) == 1){
        count++;
    }
    
    start = clock();
    insertion_sort(my_array, count);
    end = clock();

    for (i = 0; i < count; i++){
        printf("%d\n", my_array[i]);
    }
    fprintf(stderr, "%d %f\n", count, (end - start) / (double)CLOCKS_PER_SEC);
    return EXIT_SUCCESS;
}
