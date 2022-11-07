#include <stdio.h>

int main(void)
{
	int n,x,h,t;
	    	// your code goes here;
	scanf("%d",&n);
	for(t=1;t<=n;t++)
	{
		scanf("%d %d",&x,&h);
		if(x>=h)
		{
			printf("yes");
		}
		else
		{
			printf("no");
		}
	}
	return 0;
}
