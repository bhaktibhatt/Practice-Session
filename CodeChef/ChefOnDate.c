#include <stdio.h>

int main(void) {
    int X, Y,n;
    scanf("%d",&n);
    for(int t=1;t<=n;t++){
    scanf("%d %d",&X,&Y);
    if(X>=Y){
        printf("\nYES");
    }
    else{
        printf("\nNO");
    }
    }
	// your code goes here
	return 0;
}