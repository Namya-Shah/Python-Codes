//#include<stdio.h>
//
//
//int main()
//{
//	int year,month,date;
//	fatchYear:
//	printf("Enter Year:\n");
//	scanf("%d", &year);
//	if(year<=2018)
//	{
//		printf("%d\n", year);
//	}
//	else
//	{
//		printf("Please enter right year");
//		goto fatchYear;
//	}
//	fatchMonth:
//	printf("Enter Month:");
//	scanf("%d", &month);
//	if(month<=12)
//	{
//		printf("%d", month);
//	}
//	else
//	{
//		printf("Please enter right month");
//		goto fatchMonth;
//	}
//	fatchDate:
//	printf("Enter Date");
//	scanf("%d", &date);
//	switch(month)
//	{
//		case 1:
//			if(date<=31)
//			{
//				printf("%d", date);
//			}
//			else
//			{
//				printf("Please enter right date");
//				goto fatchDate;
//			}
//			break;
//		case 2:
//			if(year%4==0)
//			{
//				/*leap*/
//				if(date<=29)
//				{
//					printf("%d", date);
//				}
//				else
//				{
//					printf("It is not a valid date");
//					goto fatchDate;
//				}
//			}
//			
//			else
//			{
//				//not a leap year
//				if(date<=28)
//				{
//				printf("%d", date);	
//				}
//				else
//				{
//					printf("It is not a valid date");
//					goto fatchDate;
//				}
//			}
//			break;
//			case 3:
//			if(date<=31)
//			{
//				printf("%d", date);
//			}
//			else
//			{
//				printf("Please enter a valid date");
//				goto fatchDate;
//			}
//	}
//	
//	return 0;
//}