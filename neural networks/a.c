
// # lastnum = 1 
// # for a in range(1,6):
// # 	print()

// # 	for b in range(lastnum,a+lastnum):
// # 		print(b,end=" ")
		
// # 	lastnum = b

#include <stdio.h>
 
int main () {

   int a,b,lastnum=1;
	
   /* for loop execution */
   for( a = 1; a < 6; a++ ){
      printf("\n");
        for( b = lastnum; a <a+lastnum; a++ ){ 
        	printf("%d",b );
        }
        lastnum 
   }
 
   return 0;
}
