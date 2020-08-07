#include <stdio.h>
 
int main () {

   int sum =0,i,a;
	
   for( i = 1; i < 5; i++ ){
      printf("\n");
      for(a=1;a<5;a++){
          if(a<i){
          printf(" ");
          } else{
              sum = sum+a;
              printf("%d ",sum);
          }
      }
   }
 
   return 0;
}