/*********************************************************************
* Filename:     crypto.c
* Author:       EMOTION the artificial intelligence club of sunrin internet high school
* Copyright:    GNU GENERAL PUBLIC LICENSE
* Disclaimer:   This code is base64, url, sha256, md5, rsa en/decoder
* Details:      Performs known-answer tests on the corresponding AES
                implementation. These tests do not encompass the full
                range of available test vectors and are not sufficient
                for FIPS-140 certification. However, if the tests pass
                it is very, very likely that the code is correct and was
                compiled properly. This code also serves as
                example usage of the functions.
*********************************************************************/


/*********************************************************************
 * Type: base64
 * Role: 이다은
 * Principle: base64는 문자열을 입력받아 8bit의 데이터를 6bit로 표기
*********************************************************************/


/*********************************************************************
 * Type: sha256
 * Role: 10101 김재현
 * Principle: 
*********************************************************************/


/*********************************************************************
 * Type: md5
 * Role: 10411 박민준
 * Principle: 
*********************************************************************/


/*********************************************************************
 * Type: url, rsa
 * Role: 고태건
 * Principle: 
*********************************************************************/


#include <stdio.h>
#include <unistd.h>

const char b64chars[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

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
    sleep(1);
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
    printf("|   |    \\|   | '`--'./__;  /      |   | '` ,/  |   |    \\'   | '/  :  ;   :    /  |   | '` ,/  |   |    \\:   ' | \\.' \n");
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
    sleep(1);
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
    sleep(1);
}

char *b64_encode(const unsigned char *in, size_t len) {
	char   *out;
	size_t  elen;
	size_t  i;
	size_t  j;
	size_t  v;

	if (in == NULL || len == 0)
		return NULL;

	elen = b64_encoded_size(len);
	out  = malloc(elen+1);
	out[elen] = '\0';

	for (i=0, j=0; i<len; i+=3, j+=4) {
		v = in[i];
		v = i+1 < len ? v << 8 | in[i+1] : v << 8;
		v = i+2 < len ? v << 8 | in[i+2] : v << 8;

		out[j]   = b64chars[(v >> 18) & 0x3F];
		out[j+1] = b64chars[(v >> 12) & 0x3F];
		if (i+1 < len) {
			out[j+2] = b64chars[(v >> 6) & 0x3F];
		} else {
			out[j+2] = '=';
		}
		if (i+2 < len) {
			out[j+3] = b64chars[v & 0x3F];
		} else {
			out[j+3] = '=';
		}
	}

	return out;
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
    printf("> ");
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
    printf("3. RSA\n");
    printf("ANY OHTER NUMBER TO EXIT...\n\n");
    printf("> ");
    scanf("%d", &menu);

    switch (menu){
        case 1:
            base64(2);
            break;

        case 2:
            url(2);
            break;

        case 3:
            rsa(2);
            break;
    
        default:
            printf("EXIT... BYEBYE");
            break;
    }
}

int base64(int type){
    const unsigned char *input;
    if(type == 1){
        scanf("%s", input);

        printf("%s\n", *b64_encode(*input, sizeof(*input)));
    } else {
        scanf("%s", input);

        printf("%s\n", input);
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
    char input;
    printf("Type something you want to encode\n>");
    scanf("%s", input);

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
    printf("> ");
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