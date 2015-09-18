#include <stdio.h>
#include <string.h>
 
#define MAXSIZE 256
 
void reverse(char *str){
    char *str_begin = str;
    char *str_end = str+strlen(str)-1;  // Point to the last char
    char temp;
    while(str_begin < str_end){
        temp = *str_begin;
        *(str_begin++) = *str_end;
        *(str_end--) = temp;
    }
    return;
}
 
int main(int argc, char * argv[]){
    if(argc != 2){
        printf("Unsuitable arguments!\n");
        return 1;
    }
    char str[MAXSIZE];
    str[MAXSIZE-1] = '\0';
    strncpy(str,argv[1],MAXSIZE-1);
    printf("ready to work: %s\n",str);
    reverse(str);
    printf("Work result: %s\n",str);
    return 0;
}
