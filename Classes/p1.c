#include <stdio.h>
 
int main () {

int num,i,count ,sum = 0 ,c=0;

for(num=1;num<200;num++){
    count = 0;
    for(i=2;i<num/2 + 1;i++){
        if(num%i==0){
            count = count +1;
            break;
        }
    }
    if (count == 0 && num != 1){
        printf(" %d ",num);
        c++;
        sum = sum +num;
    } 
}

printf("\n The sum of all prime numbers is: %d",sum);
printf("\n There are total %d prime numbers between 1 to 200",c);

   return 0;
}