
#include <stdio.h>

int main(){

    char * a;
    a = "%d%d";
    char * b  = "%d";

    printf(a, 2, 2);
    printf(b, 2);
    printf("\nabc");

    return 0;

}