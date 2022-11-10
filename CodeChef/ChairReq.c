#include<stdio.h>
int main()
{
    int i,n,X,Y;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        scanf("%d %d",&X,&Y);
        if(X>=Y)
        {
            printf("\n%d",X-Y);
        }
        else
        {
            printf("\n0");
        }
    }
    return 0;
}