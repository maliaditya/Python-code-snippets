class SelectionSort{


    static void printArray(int a[]){

        for(int i=0;i<a.length;i++){
            System.out.printf("%d ",a[i]);
        }
    }

    static void selectionSort(int a[]){

        for(int i=0;i<a.length;i++){
            for(int j=i+1;j<a.length;j++){

                if(a[i]>a[j]){
                    int temp = a[i];
                    a[i]=a[j];
                    a[j] = temp;
                }
            }
        }
        printArray(a);

    }   

    public static void main(String[] args){
        int a[] = {10,20,8,9,6,30,40};

        selectionSort(a);
    }
}