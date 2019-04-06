#include <stdio.h>

int facto(int n){
    int a = 1;
    for(int i = 1; i <= n; i++){
        a *= i;
    }
    return a;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", facto(n));
}