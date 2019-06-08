#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<malloc.h>
void getsort(char *);
struct number{
	int a : 2;
};
int main()
{
	char *filename = (char *)malloc(sizeof(char) * 100);
	gets(filename);
	getsort(filename);
	getchar();
	getchar();
}
void getsort(char *filename)
{
	struct number *num = (struct number *)malloc(1000000* sizeof(struct number));
	FILE *fp;
	char c;
	unsigned int val;
	fp = fopen(filename, "r");
	int z = 0;
	for (int i = 0; i<10; i++)
	{
		z = 0;
		while (fscanf(fp, "%u", &val)!=EOF)
		{
			//printf("%d ",z++);
			if (val<(1000000 * (i + 1)) && val>(1000000 * (i)))
			{
				num[val % 1000000].a = 1;
			}
			else
				num[val % 1000000].a = 0;
		}
		//printf("hi");
		for (int j = 0; j < 1000000; j++){
			//printf("%d",num[j].a);
			if (num[j].a == 1)
			{
				printf("%u ", (i * 1000000) + j);
			}
		}
		for (int i = 0; i < 1000000; i++)
			num[i].a = 0;
		rewind(fp);
		//fseek(fp, 0, SEEK_SET);
	}
}
