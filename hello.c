#include <stdio.h>
 int main(){
	 int a=2;
	 int b=2;
	 int c=a+b;

	 printf("C says: Hello, World!\n");
	 printf("%d + %d=%d\n",a,b,c);
	 char arr[][10]={"User1", "user2", "user2"};
	 printf("How many users\n");
	 
	for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++){
        	printf("%s\n ", arr[i]);
    		
	}
	 return 0;
 }
