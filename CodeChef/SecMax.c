#include<stdio.h>
int main()
{
    int n,a,b,c,i;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        scanf("%d %d %d",&a,&b,&c);
        if((a>b && a<c)||(a<b && a>c))// b<a<c or c<a<b
        {
            printf("\n%d",a);
        }
        else if((b>a && b<c) || (b<a && b>c)) // a<b<c or c<b<a
        {
            printf("\n%d",b);
        }
        else if((c>a && c<b) || (c<a && c>b))// a<c<b or b<c<a
        {
            printf("\n%d",c);
        }
        else
        {
            printf("NaN");
        }
    }
}