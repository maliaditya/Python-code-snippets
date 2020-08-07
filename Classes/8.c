#include <stdio.h>
 
int main () {
    int space=4,bspace=4,mspace =3,a,b,c = 65;

    for(a=0;a<5;a++){
        printf("\n");
        
        for(b=0;b<9;b++){

            if(b<space)
                printf(" ");
            else if(b>bspace)
                printf(" ");
            else if(b==space || b == bspace)
                printf("%c ",c);
            else
                printf(" ");
                
            
        }
        space = space -1;
        bspace = bspace +1;
        c = c+1;


    }
  
   return 0;
}