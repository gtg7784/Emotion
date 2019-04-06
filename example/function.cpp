#include <stdio.h>

int add(int a, int b){
    return a+b;
}

void add_noReturn(int a, int b){
    printf("%d\n", a+b);
}

int main(){   
    printf("%d\n", add(1, 2));

    add_noReturn(1, 2);
}