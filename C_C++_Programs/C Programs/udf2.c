#include<stdio.h>

int fnSum(int a, int b)
{
	return a+b;
}

int main()
{
	int a,b,c;
	printf("Enter a:");
	scanf("%d", &a);
	printf("Enter b:");
	scanf("%d", &b);
	c=fnSum(a, b);
	printf("Sum of %d and %d = %d", a, b, c);
}