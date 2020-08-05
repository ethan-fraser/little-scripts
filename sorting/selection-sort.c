#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_MAX 30000

void selection_sort(int *a, int n){
    int i, j, minidx, temp;

    for (i = 0; i < n; i++){
        /* get the smallest item */
        minidx = i;
        for (j = i+1; j < n; j++){
            if (a[j] < a[minidx]){
                minidx = j;
            }
        }
        
        /* swap the smallest item with a[i] */
        if (minidx != i){
            temp = a[i];
            a[i] = a[minidx];
            a[minidx] = temp;
        }
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
    selection_sort(my_array, count);
    end = clock();

    for (i = 0; i < count; i++){
        printf("%d\n", my_array[i]);
    }
    fprintf(stderr, "%d %f\n", count, (end - start) / (double)CLOCKS_PER_SEC);
    return EXIT_SUCCESS;
}
