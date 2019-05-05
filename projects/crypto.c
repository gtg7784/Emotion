#include <stdio.h>

const char base64chars[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

int encrypt(){
    int menu;

    printf("************************************************************\n");
    printf("EMOTION CRYPTO ENCODER\n");
    printf("************************************************************\n\n");
    printf("Choose the number…\n");
    printf("1. BASE64\n");
    printf("2. URL\n");
    printf("3. SHA256\n");
    printf("4. MD5\n");
    printf("5. RSA\n");
    printf("ANY OHTER NUMBER TO EXIT...\n\n");
    printf(">    ");
    scanf("%d", &menu);

    switch (menu){
        case 1:
            base64(1);
            break;

        case 2:
            url(1);
            break;

        case 3:
            sha256();
            break;

        case 4:
            md5(1);
            break;

        case 5:
            rsa(1);
            break;
    
        default:
            printf("EXIT... BYEBYE");
            break;
    }

}

int decrypt(){
    int menu;

    printf("************************************************************\n");
    printf("EMOTION CRYPTO DECODER\n");
    printf("************************************************************\n\n");
    printf("Choose the number…\n");
    printf("1. BASE64\n");
    printf("2. URL\n");
    printf("3. MD5\n");
    printf("4. RSA\n");
    printf("ANY OHTER NUMBER TO EXIT...\n\n");
    printf(">    ");
    scanf("%d", &menu);

    switch (menu){
        case 1:
            base64(2);
            break;

        case 2:
            url(2);
            break;

        case 3:
            md5(2);
            break;

        case 4:
            rsa(2);
            break;
    
        default:
            printf("EXIT... BYEBYE");
            break;
    }
}

int base64(int type){
    if(type == 1){
        printf("encrypting...");
         
        printf("asdf");
    } else {
        printf("decrypting...");
         
        printf("asdf");
    }
}

int url(int type){
    if(type == 1){
        printf("encrypting...");
         
        printf("asdf");
    } else {
        printf("decrypting...");
         
        printf("asdf");
    }
}

int sha256(){
        printf("encrypting...");
         
        printf("asdf");
}

int md5(int type){
    if(type == 1){
        printf("encrypting...");
         
        printf("asdf");
    } else {
        printf("decrypting...");
         
        printf("asdf");
    }
}

int rsa(int type){
    if(type == 1){
        printf("encrypting...");
         
        printf("asdf");
    } else {
        printf("decrypting...");
         
        printf("asdf");
    }
}

int main(){
    int menu;

    printf("************************************************************\n");
    printf("EMOTION CRYPTO EN / DECODER\n");
    printf("************************************************************\n\n");
    printf("Choose the number…\n");
    printf("1. ENCRYPT\n");
    printf("2. DECRYPT\n");
    printf("ANY OHTER NUMBER TO EXIT...\n\n");
    printf(">    ");
    scanf("%d", &menu);
    
    switch (menu){
        case 1:
            printf("1. ENCRYPT\n\n\n");
            encrypt();
            break;
    
        case 2:
            printf("2. DECRYPT\n\n\n");
            decrypt();
            break;

        default: 
            printf("EXIT... BYEBYE");
            break;
    }
}