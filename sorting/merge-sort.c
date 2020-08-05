#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_MAX 100000

void merge(int *a, int *w, int n){
    int l = 0, r = n/2;
    int k = 0;

    while (l < n / 2 && r < n){
        if (a[l] < a[r]){
            w[k] = a[l];
            l++;
        } else {
            w[k] = a[r];
            r++;
        }
        k++;
    }

    while (l < n / 2){
        w[k] = a[l];
        l++;
        k++;
    }
    while (r < n){
        w[k] = a[r];
        r++;
        k++;
    }
}

void merge_sort(int *a, int *w, int n){
    
    int i;
    
    /* base condition */
    if (n < 2)
        return;

    /* recursive calls */
    merge_sort(a, w, n / 2);
    merge_sort((a + (n / 2)), w, (n - (n / 2)));

    /* merge the two halves of a int w */
    merge(a, w, n);

    /* copy w back into a */
    for (i = 0; i < n; i++){
        a[i] = w[i];
    }

}

int main(void){
    int my_array[ARRAY_MAX];
    int workspace[ARRAY_MAX];
    clock_t start, end;
    int i, count = 0;

    while (count < ARRAY_MAX && scanf("%d", &my_array[count]) == 1){
        count++;
    }

    start = clock();
    merge_sort(my_array, workspace, count);
    end = clock();

    for (i = 0; i < count; i++){
        printf("%d\n", my_array[i]);
    }
    fprintf(stderr, "%d %f\n", count, (end - start) / (double)CLOCKS_PER_SEC);
    return EXIT_SUCCESS;
}
