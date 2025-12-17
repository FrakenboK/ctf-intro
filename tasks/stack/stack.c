#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BANNER "\
===========================================\n\
          STACK VAULT v3.1\n\
   Secure Password Storage System\n\
===========================================\n"

char secret[64];

void getFirstFlag() {
    char* flag = getenv("FLAG1");
    if (flag == NULL) {
        flag = "flag{1}";
    }
    printf("\n[+] Vault opened successfully!\n");
    printf("[+] FLAG1: %s\n", flag);
    exit(0);
}

void getSecondFlag() {
    char* flag = getenv("FLAG2");
    if (flag == NULL) {
        flag = "flag{2}";
    }
    printf("\n[+] Vault opened successfully!\n");
    printf("[+] FLAG2: %s\n", flag);
    exit(0);
}

void checkAdminPassword() {
    char input[64];
    
    printf("\n[*] Enter vault password: ");
    
    char* env_pass = getenv("SECRET_PASSWORD");
    if (env_pass == NULL) {
        strcpy(secret, "DEFAULT_SAFE_PASSWORD_123!");
    } else {
        strcpy(secret, env_pass);
    }
    
    fgets(input, 64, stdin);
    
    input[strcspn(input, "\n")] = 0;
    
    if (strcmp(input, secret) == 0) {
        printf("[+] Admin password correct!\n");
        return;
    } else {
        printf("[-] Admin access denied!\n");
        printf("[-] Invalid password: %s\n", input);
        exit(1);
    }
}

void checkPassword() {
    char secret[64];
    char input[64];
    
    printf("\n[*] Enter vault password: ");
    
    char* env_pass = getenv("SECRET_ADMIN_PASSWORD");
    if (env_pass == NULL) {
        strcpy(secret, "DEFAULT_SAFE_PASSWORD_123!");
    } else {
        strcpy(secret, env_pass);
    }
    
    fgets(input, 200, stdin);
    
    input[strcspn(input, "\n")] = 0;
    
    if (strcmp(input, secret) == 0) {
        printf("[+] Password correct!\n");
        return;
    } else {
        printf("[-] Access denied!\n");
        printf("[-] Invalid password: %s\n", input);
        exit(1);
    }
}


int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    
    puts(BANNER);
    
    printf("[*] Initializing vault system...\n");
    
    checkPassword();
    getFirstFlag();

    checkAdminPassword();
    getSecondFlag();
    return 0;
}