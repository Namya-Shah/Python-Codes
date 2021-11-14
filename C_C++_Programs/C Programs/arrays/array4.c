//#include<stdio.h>
//int main()
//{
//	int i,j;
//	char c1[10], c2[10], c3[10], c4[40];
//	printf("Enter First Name:");
//	scanf("%s", c1);
//	
//	printf("Enter Middle Name:");
//	scanf("%s", c2);
//	
//	printf("Enter Last Name:");
//	scanf("%s", c3);
//	i=0; j=0;
//	
//	do
//	{
//		c4[j] = c1[i];
//		i++;
//		j++;
//	}while(c1[i]!='\0');
//	c4[j]='_';
//	j++;
//	i=0;
//	do
//	{
//		c4[j] = c2[i];
//		i++;
//		j++;
//	}while(c2[i]!='\0');
//	c4[j]='_';
//	j++;
//	i=0;
//	do
//	{
//		c4[j] = c3[i];
//		i++;
//		j++;
//	}while(c3[i]!='\0');
//		c4[j] ='\0';
//		printf("Full Name: %s", c4);
//		
//}