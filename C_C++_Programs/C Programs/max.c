#include <stdio.h>

int main(int argc, char **argv)
{
	int a,b,c;
	printf("Enter a:");
	scanf("%d", &a);
	printf("Enter b:");
	scanf("%d", &b);
	printf("Enter c:");
	scanf("%d", &c);
	if(a>=b)
	{
		if(a>=c)
		{
			printf("%d is maximum\n", a);
			
		}
		else
		{
			printf("%d is maximum\n", c);
		}
	}
	else
	{
		if(b>=c)
		{
			printf("%d is maximum\n", b);
		}
		else
		{
			printf("%d is maximum\n", c);
		}
	}
}
