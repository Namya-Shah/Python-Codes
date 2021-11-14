#include<stdio.h>

int main()
{
	int a,b,c;
	printf("Enter a:");
	scanf("%d", &a);
	
	printf("Enter b:");
	scanf("%d", &b);
	
	printf("Enter c:");
	scanf("%d", &c);
	
	if(a > b && a > c)
	{
		printf("\t%d", a);
		
		if(b>c)
		{
			printf("\t%d\t%d",b,c);
		}
		else
		{
			printf("\t%d\t%d",c,b);
		}
	}
	else if(b>a && b > c)
	{
		printf("\t%d", b);
		if(a > c)
		{
			printf("\t%d\t%d", a,c);
		}
		else
		{
			printf("\t%d\t%d", c,a);
		}
	}
	else
	{
		printf("\t%d", c);
		
		if(a>b)
		{
			printf("\t%d\t%d", a, b);
			
		}
		else
		{
			printf("\t%d\t%d", b,a);
		}
	}
	return 0;
}