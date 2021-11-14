#include <stdio.h>
void main()
{
	int a,b,c,d;
	printf("Enter a:");
	scanf("%d", &a);
	printf("Enter b:");
	scanf("%d", &b);
	printf("Enter c:");
	scanf("%d", &c);
	d=(a+b+c)/3;
	printf("Average of %d %d %d = %d\n",a, b, c, d);
}