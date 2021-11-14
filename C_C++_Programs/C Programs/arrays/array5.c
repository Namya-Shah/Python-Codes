//#include<stdio.h>
//int main()
//{
//	int i,j;
//	char c1[10], c2[10], c3[20];
//	bool blnc1=false, blnc2=false;
//	
//	
//	
//	printf("Enter First Name:");
//	scanf("%s", c1);
//	
//	printf("Enter Last Name:");
//	scanf("%s", c2);
//	i=0; 
//	j=0;
//	
//	do
//	{
//		c3[j]='*';
//		j++;
//		c3[j]=c1[i];
//		i++;
//		j++;
//	}while(c1[i]!='\0');
//	
//	i=0;
//	
//	do
//	{
//		c3[j]='*';
//		j++;
//		c3[j]=c2[i];
//		i++;
//		j++;
//	}while(c2[i]!='\0');
//	c3[j]='*';
//		j++;
//	c3[j]='\0';
//	
//	printf(" Full Name: %s", c3);
//}