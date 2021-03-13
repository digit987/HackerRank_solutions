// https://www.hackerrank.com/challenges/reverse-game?h_r=next-challenge&h_v=zen
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a[10000],i,start=0,end,n,temp,t,ti,k;
    scanf("%d",&t);
    ti=1;
    while(ti<=t)
        {
        scanf("%d%d",&n,&k);
    end=n-1;
    while(start<=n)
        {
    for(i=start;i<(end-start)/2;i++)
        {
        temp=a[i];
        a[i]=a[end];
        a[end]=temp;
        end--;
    }
    start++;
    end=n-1;
    }
        for(i=0;i<n;i++)
            {
            if(a[i]==k)
                {
                printf("i\n");
            }
        }
        ti++;
    }

    return 0;
}
