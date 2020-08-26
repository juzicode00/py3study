/*
author: juzicode
address : www.juzicode.com
¹«ÖÚºÅ : ½Û×Ócode / juzicode
date : 2020.8.1
*/
#include "stdio.h"

#ifdef __cplusplus
extern "C" {
#endif 

__declspec(dllexport) int addi(int x, int y) 
{
	return x + y;
}

__declspec(dllexport) double addd(double x, double y)
{
	return x + y;
}


__declspec(dllexport) float addf(float x, float y)
{
	return x + y;
}


__declspec(dllexport) long long addll(long long x, long long y)
{
	return x + y;
}


__declspec(dllexport) char trans_c(char y)
{
	return y ;
}

__declspec(dllexport) wchar_t trans_wc(wchar_t y)
{
	return y;
}


__declspec(dllexport) char* trans_cp(char* y)
{
	return y;
}
__declspec(dllexport) wchar_t* trans_wcp(wchar_t* y)
{
	return y;
}


typedef struct __ts_fruit {
	char name[10];
	float weight;
	int a;

}TS_FRUIT,PTS_FRUIT;


__declspec(dllexport) long long trans_array_i(int x[10])
{
	long long sum = 0;
	printf("in c:");
	for (int i = 0; i < 10; i++)
	{
		printf("%d ", x[i]);
		sum += x[i];
	}
	printf("\n");
	return sum;
}



__declspec(dllexport) char trans_array_c(char x[20])
{
	for (int i = 0; i < 20; i++)
	{
		printf("%c ", x[i]);
	}
	printf("\n");
	return x[0];
}



#ifdef __cplusplus
}
#endif









