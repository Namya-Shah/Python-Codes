#include<stdio.h>
int main()
{
	int a;
	printf("Enter a:");
	scanf("%d", &a);
	if(a==0)
	{
		printf("The number is zero/n");
	}
	else if(a>0)
	{
		printf("The number is positive");
	}
	else
	{
		printf("The number is negative");
	}
	return 0;
}