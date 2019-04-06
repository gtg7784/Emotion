#include <stdio.h>

int facto(int n, int a){
    if(n == 1){
        return a;
    }else{
        a *= n;
        return facto(n-1, a);
    }
}

int main(){
    int n, a = 1;
    scanf("%d", &n);
    printf("%d\n", facto(n, a));
}
