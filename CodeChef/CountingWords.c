#include<stdio.h>
int main()
{
    int i,t,N,M,words;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d",&N,&M);
        words = N*M;
        printf("\n%d",words);
    }
}