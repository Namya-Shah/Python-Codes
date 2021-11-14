#include <stdio.h>
void main()
{
	int a,b,c;
	printf("Enter a:");
	scanf("%d", &a);
	printf("Enter b:");
	scanf("%d", &b);
	printf("Enter c:");
	scanf("%d", &c);
	if(a==b)
	{
		if(a == c)
		{
			printf("All 3 are equal\n");
		}
		else
		{
			printf("a is equal to b\n");
		}
	}
	else
	{
		if(b==c)
		{
			printf("b is equal to c\n");
		}
		else
		{
			if(c==a)
			{
				printf("c is equal to a\n");
			}
			else
			{
				printf("All three are different\n");
			}
		}
	}
}