#include<stdio.h>

int main()
{
	char c;
	printf("Enter character:");
	scanf("%c", &c);
	
	if(c=='a' || c == 'A' || c == 'e' || c == 'E' || c == 'i' || c == 'I' || c == 'o' || c == 'O' || c == 'u' || c == 'U')
	{
		printf("Character is a vowel\n");
	}
	else
	{
		printf("Character is a consonent\n");
	}
	return 0;
}