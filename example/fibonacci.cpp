#include <stdio.h>

int fibo(int n){
    if(n == 1 || n == 0){
        return 1;
    } else {
        return fibo(n-1)+fibo(n-2);
    }
}

int main(){
    int a;
    scanf("%d", &a);
    printf("%d\n", fibo(a));
}