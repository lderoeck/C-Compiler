
int main(){

    int i = 0;

    if (i){
        printf(0);
    }

    if (i > 0){
        printf(1);
    }else {
        i = 2;
        if (i > 0 || i < 0){
            printf(2);
        }else {
            printf(3);
        }
    }

    if (i > -1 && i < 1 ){
        printf(3);
    }

    if (i == 0){
        if (i == 1){
                printf(4);
            }
    }

    return 0;

}