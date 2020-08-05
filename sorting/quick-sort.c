#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int partition(int *a, int p, int r){
    int x = a[r];
    int i = p - 1;
    int j, temp;
    for (j = p; j < r; j++){
        if (a[j] <= x){
            i++;
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }
    temp = a[i+1];
    a[i+1] = a[r];
    a[r] = temp;
    return i+1;
}

void quicksort(int *a, int p, int r){
    int q;
    if (p < r){
        q = partition(a, p, r);
        quicksort(a, p, q-1);
        quicksort(a, q+1, r);
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
    quicksort(my_array, count);
    end = clock();

    for (i = 0; i < count; i++){
        printf("%d\n", my_array[i]);
    }
    fprintf(stderr, "%d %f\n", count, (end - start) / (double)CLOCKS_PER_SEC);
    return EXIT_SUCCESS;
}
