#include <stdio.h>

int main(void) {
    int t, X, Y, n, sum;
    scanf("%d",&n);
    for(t=1;t<=n;t++){
        scanf("%d %d",&X,&Y);
        sum = X*10 + Y*90;
        printf("\n%d",sum);
    }

	// your code goes here
	return 0;
	
}
