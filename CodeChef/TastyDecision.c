#include <stdio.h>

int main(void) {
    int n,t,x,y,choco,candy;
    
     scanf("%d",&n);
    
     for(t=1;t<=n;t++)
    {
        scanf("%d %d",&x,&y);
        choco = 2*x;
        candy = 5*y;
    
        if(choco>candy)
        {
            printf("Chocolate\n");
        }
        else if(candy>choco)
        {
            printf("Candy\n");
        }
        else
        {
            printf("Either\n");
        }
    }
	
	return 0;
}
