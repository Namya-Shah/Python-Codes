#include<stdio.h>
void main()
{
	int n,mod;
	
	printf("Enter number:");
	scanf("%d", &n);
	mod = n%2;
	if (mod==0)
	{
		printf("The number is even\n");
	}
	else
	{
		printf("The number is odd\n");
	}
}