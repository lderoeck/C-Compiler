#include <stdio.h>

int main()
{

    char c;                  //declare c
    c = 0;                  //c=0

    c = 55 + '2' + 'd';     //c=205
    c = c - 55.0;           //c=150
    c = c*2;                //c=300
    c = c/2.0;              //c=150
    c = c%100;              //c=50
    c = c && 1;             //c=1
    c = c || 0;             //c=1
    c = c < 5;              //c=0

    c = c == 0;             //c=1
    c = !c;                 //c=0
    c = c > -500;           //c=1
    c = c != (55+5)/3;      //c=1
    c = c <= 88/5*(2.0-1);  //c=1
    c--;                    //c=0
    --c;                    //c=-1
    c++;                    //c=0
    ++c;                    //c=1
    c += c = 5;             //c=10
    c -= c--;               //c=-1
    c *= -(88%4+5);         //c=5
    c /= 5.0;               //c=1
    c %= 1;                 //c=0

    int i;                  //declare i
    i = 0;                  //i=0

    i = 55 + '2' + 'd';     //i=205
    i = i - 55.0;           //i=150
    i = i*2;                //i=300
    i = i/2.0;              //i=150
    i = i%100;              //i=50
    i = i && 1;             //i=1
    i = i || 0;             //i=1
    i = i < 5;              //i=0

    i = i == 0;             //i=1
    i = !i;                 //i=0
    i = i > -500;           //i=1
    i = i != (55+5)/3;      //i=1
    i = i <= 88/5*(2.0-1);  //i=1
    i--;                    //i=0
    --i;                    //i=-1
    i++;                    //i=0
    ++i;                    //i=1
    i += i = 5;             //i=10
    i -= i--;               //i=-1
    i *= -(88%4+5);         //i=5
    i /= 5.0;               //i=1
    i %= 1;                 //i=0

    float f;                //declare f
    f = 0;                  //f=0

    f = 55 + '2' + 'd';     //f=205
    f = f - 55.0;           //f=150
    f = f*2;                //f=300
    f = f/2.0;              //f=150
    //f = f%100;              //f=50
    f = f && 1;             //f=1
    f = f || 0;             //f=1
    f = f < 5;              //f=0

    f = f == 0;             //f=1
    f = !f;                 //f=0
    f = f > -500;           //f=1
    f = f != (55+5)/3;      //f=1
    f = f <= 88/5*(2.0-1);  //f=1
    f--;                    //f=0
    --f;                    //f=-1
    f++;                    //f=0
    ++f;                    //f=1
    f += f = 5;             //f=10
    f -= f--;               //f=-1
    f *= -(88%4+5);         //f=5
    f /= 5.0;               //f=1
    //f %= 1;               //f=0


    return i >= 1;          //RETURN 0
}