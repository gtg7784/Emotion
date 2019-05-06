/*********************************************************************
* Filename:     crypto.c
* Author:       EMOTION the artificial intelligence club of sunrin internet high school
* Copyright:    GNU GENERAL PUBLIC LICENSE
* Disclaimer:   This code is presented "as is" without any guarantees.
* Details:      Performs known-answer tests on the corresponding AES
                implementation. These tests do not encompass the full
                range of available test vectors and are not sufficient
                for FIPS-140 certification. However, if the tests pass
                it is very, very likely that the code is correct and was
                compiled properly. This code also serves as
                example usage of the functions.
*********************************************************************/


#include <stdio.h>
#include <unistd.h>

const char base64chars[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

/*
 TODO:
    1. EMOTION CRYPTO ~~ -> ASCII
    2. 
*/

void printEmotion(){
    printf("                                                ,----,                                    \n");
    printf("                    ____      ,----..         ,/   .`|            ,----..            ,--. \n");
    printf("    ,---,.        ,'  , `.   /   /   \\      ,`   .'  :   ,---,   /   /   \\         ,--.'| \n");
    printf("  ,'  .' |     ,-+-,.' _ |  /   .     :   ;    ;     /,`--.' |  /   .     :    ,--,:  : | \n");
    printf(",---.'   |  ,-+-. ;   , || .   /   ;.  \\.'___,/    ,' |   :  : .   /   ;.  \\,`--.'`|  ' : \n");
    printf("|   |   .' ,--.'|'   |  ;|.   ;   /  ` ;|    :     |  :   |  '.   ;   /  ` ;|   :  :  | | \n");
    printf(":   :  |-,|   |  ,', |  ':;   |  ; \\ ; |;    |.';  ;  |   :  |;   |  ; \\ ; |:   |   \\ | : \n");
    printf(":   |  ;/||   | /  | |  |||   :  | ; | '`----'  |  |  '   '  ;|   :  | ; | '|   : '  '; | \n");
    printf("|   :   .''   | :  | :  |,.   |  ' ' ' :    '   :  ;  |   |  |.   |  ' ' ' :'   ' ;.    ; \n");
    printf("|   |  |-,;   . |  ; |--' '   ;  \\; /  |    |   |  '  '   :  ;'   ;  \\; /  ||   | | \\   | \n");
    printf("'   :  ;/||   : |  | ,     \\   \\  ',  /     '   :  |  |   |  ' \\   \\  ',  / '   : |  ; .' \n");
    printf("|   |    \\|   : '  |/       ;   :    /      ;   |.'   '   :  |  ;   :    /  |   | '`--'   \n");
    printf("|   :   .';   | |`-'         \\   \\ .'       '---'     ;   |.'    \\   \\ .'   '   : |       \n");
    printf("|   | ,'  |   ;/              `---`                   '---'       `---`     ;   |.'       \n");
    printf("`----'    '---'                                                             '---'         \n");
    sleep(3);
}

void printCrypto(){
    printf("                                                        ,----,             \n");
    printf("                                     ,-.----.         ,/   .`|  ,----..    \n");
    printf("      ,----..  ,-.----.              \\    /  \\      ,`   .'  : /   /   \\   \n");
    printf("     /   /   \\ \\    /  \\        ,---,|   :    \\   ;    ;     //   .     :  \n");
    printf("    |   :     :;   :    \\      /_ ./||   |  .\\ :.'___,/    ,'.   /   ;.  \\ \n");
    printf("    .   |  ;. /|   | .\\ :,---, |  ' :.   :  |: ||    :     |.   ;   /  ` ; \n");
    printf("    .   ; /--` .   : |: /___/ \\.  : ||   |   \\ :;    |.';  ;;   |  ; \\ ; | \n");
    printf("    ;   | ;    |   |  \\ :.  \\  \\ ,' '|   : .   /`----'  |  ||   :  | ; | ' \n");
    printf("    |   : |    |   : .  / \\  ;  `  ,';   | |`-'     '   :  ;.   |  ' ' ' : \n");
    printf("    .   | '___ ;   | |  \\  \\  \\    ' |   | ;        |   |  ''   ;  \\; /  | \n");
    printf("    '   ; : .'||   | ;\\  \\  '  \\   | :   ' |        '   :  | \\   \\  ',  /  \n");
    printf("    '   | '/  ::   ' | \\.'   \\  ;  ; :   : :        ;   |.'   ;   :    /   \n");
    printf("    |   :    / :   : :-'      :  \\  \\|   | :        '---'      \\   \\ .'    \n");
    printf("    \\   \\ .'  |   |.'         \\  ' ;`---'.|                    `---`      \n");
    printf("    `---`    `---'            `--`   `---`                   \n");            
    sleep(1);
}

void printEndecode(){
    printf("                                                                                                                      \n");
    printf("                   ,--.                                                  ,----..                                      \n");
    printf("    ,---,.       ,--.'|        ,--,    ,---,        ,---,.  ,----..     /   /   \\      ,---,        ,---,.,-.----.    \n");
    printf("  ,'  .' |   ,--,:  : |       / .`|  .'  .' `\\    ,'  .' | /   /   \\   /   .     :   .'  .' `\\    ,'  .' |\\    /  \\   \n");
    printf(",---.'   |,`--.'`|  ' :      /' / ;,---.'     \\ ,---.'   ||   :     : .   /   ;.  \\,---.'     \\ ,---.'   |;   :    \\  \n");
    printf("|   |   .'|   :  :  | |     /  / .'|   |  .`\\  ||   |   .'.   |  ;. /.   ;   /  ` ;|   |  .`\\  ||   |   .'|   | .\\ :  \n");
    printf(":   :  |-,:   |   \\ | :    /  / ./ :   : |  '  |:   :  |-,.   ; /--` ;   |  ; \\ ; |:   : |  '  |:   :  |-,.   : |: |  \n");
    printf(":   |  ;/||   : '  '; |   / ./  /  |   ' '  ;  ::   |  ;/|;   | ;    |   :  | ; | '|   ' '  ;  ::   |  ;/||   |  \\ :  \n");
    printf("|   :   .''   ' ;.    ;  /  /  /   '   | ;  .  ||   :   .'|   : |    .   |  ' ' ' :'   | ;  .  ||   :   .'|   : .  /  \n");
    printf("|   |  |-,|   | | \\   | /  /  /    |   | :  |  '|   |  |-,.   | '___ '   ;  \\; /  ||   | :  |  '|   |  |-,;   | |  \\  \n");
    printf("'   :  ;/|'   : |  ; .';  /  /     '   : | /  ; '   :  ;/|'   ; : .'| \\   \\  ',  / '   : | /  ; '   :  ;/||   | ;\\  \\ \n");
    printf("|   |   \\|   | '`--'./__;  /      |   | '` ,/  |   |    \\'   | '/  :  ;   :    /  |   | '` ,/  |   |    \\:   ' | \\.' \n");
    printf("|   :   .''   : |    |   : /       ;   :  .'    |   :   .'|   :    /    \\   \\ .'   ;   :  .'    |   :   .':   : :-'   \n");
    printf("|   | ,'  ;   |.'    ;   |/        |   ,.'      |   | ,'   \\   \\ .'      `---`     |   ,.'      |   | ,'  |   |.'     \n");
    printf("`----'    '---'      `---'         '---'        `----'      `---`                  '---'        `----'    `---'       \n");
    sleep(1);
}


void printDecode(){
    printf("                                                                                       \n");
    printf("                                      ,----..                                      \n");
    printf("    ,---,        ,---,.  ,----..     /   /   \\      ,---,        ,---,.,-.----.    \n");
    printf("  .'  .' `\\    ,'  .' | /   /   \\   /   .     :   .'  .' `\\    ,'  .' |\\    /  \\   \n");
    printf(",---.'     \\ ,---.'   ||   :     : .   /   ;.  \\,---.'     \\ ,---.'   |;   :    \\  \n");
    printf("|   |  .`\\  ||   |   .'.   |  ;. /.   ;   /  ` ;|   |  .`\\  ||   |   .'|   | .\\ :  \n");
    printf(":   : |  '  |:   :  |-,.   ; /--` ;   |  ; \\ ; |:   : |  '  |:   :  |-,.   : |: |  \n");
    printf("|   ' '  ;  ::   |  ;/|;   | ;    |   :  | ; | '|   ' '  ;  ::   |  ;/||   |  \\ :  \n");
    printf("'   | ;  .  ||   :   .'|   : |    .   |  ' ' ' :'   | ;  .  ||   :   .'|   : .  /  \n");
    printf("|   | :  |  '|   |  |-,.   | '___ '   ;  \\; /  ||   | :  |  '|   |  |-,;   | |  \\  \n");
    printf("'   : | /  ; '   :  ;/|'   ; : .'| \\   \\  ',  / '   : | /  ; '   :  ;/||   | ;\\  \\ \n");
    printf("|   | '` ,/  |   |    \\'   | '/  :  ;   :    /  |   | '` ,/  |   |    \\:   ' | \\.' \n");
    printf("    ;   :  .'    |   :   .'|   :    /    \\   \\ .'   ;   :  .'    |   :   .':   : :-'   \n");
    printf("|   ,.'      |   | ,'   \\   \\ .'      `---`     |   ,.'      |   | ,'  |   |.'     \n");
    printf("'---'        `----'      `---`                  '---'        `----'    `---'       \n");
}

void printEncode(){
    printf("                                                                                       \n");
    printf("                   ,--.               ,----..                                      \n");
    printf("    ,---,.       ,--.'|  ,----..     /   /   \\      ,---,        ,---,.,-.----.    \n");
    printf("  ,'  .' |   ,--,:  : | /   /   \\   /   .     :   .'  .' `\\    ,'  .' |\\    /  \\   \n");
    printf(",---.'   |,`--.'`|  ' :|   :     : .   /   ;.  \\,---.'     \\ ,---.'   |;   :    \\  \n");
    printf("|   |   .'|   :  :  | |.   |  ;. /.   ;   /  ` ;|   |  .`\\  ||   |   .'|   | .\\ :  \n");
    printf(":   :  |-,:   |   \\ | :.   ; /--` ;   |  ; \\ ; |:   : |  '  |:   :  |-,.   : |: |  \n");
    printf(":   |  ;/||   : '  '; |;   | ;    |   :  | ; | '|   ' '  ;  ::   |  ;/||   |  \\ :  \n");
    printf("|   :   .''   ' ;.    ;|   : |    .   |  ' ' ' :'   | ;  .  ||   :   .'|   : .  /  \n");
    printf("|   |  |-,|   | | \\   |.   | '___ '   ;  \\; /  ||   | :  |  '|   |  |-,;   | |  \\  \n");
    printf("'   :  ;/|'   : |  ; .''   ; : .'| \\   \\  ',  / '   : | /  ; '   :  ;/||   | ;\\  \\ \n");
    printf("|   |    \\|   | '`--'  '   | '/  :  ;   :    /  |   | '` ,/  |   |    \\:   ' | \\.' \n");
    printf("|   :   .''   : |      |   :    /    \\   \\ .'   ;   :  .'    |   :   .':   : :-'   \n");
    printf("|   | ,'  ;   |.'       \\   \\ .'      `---`     |   ,.'      |   | ,'  |   |.'     \n");
    printf("`----'    '---'          `---`                  '---'        `----'    `---'       \n");
}

int Encrypt(){
    int menu;

    printEncode();
                                                                                                                      
    printf("Select the number…\n");
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

int Decrypt(){
    int menu;

    printDecode();

    printf("Select the number…\n");
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

    printEmotion();
    printCrypto();
    printEndecode();
    printf("Select the number…\n");
    printf("1. ENCRYPT\n");
    printf("2. DECRYPT\n");
    printf("ANY OHTER NUMBER TO EXIT...\n\n");
    printf(">    ");
    scanf("%d", &menu);
    
    switch (menu){
        case 1:
            printf("1. ENCRYPT\n\n\n");
            Encrypt();
            break;
    
        case 2:
            printf("2. DECRYPT\n\n\n");
            Decrypt();
            break;

        default: 
            printf("EXIT... BYEBYE");
            break;
    }
}