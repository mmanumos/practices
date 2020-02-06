#include <stdio.h>
#include "holberton.h"

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
	char mundo[] = "Mundo";
	char f = 'f';
	int a = 598;
	int b = 56;

	_printf("Este es el string %s", mundo);
	_printf("Este es el char %c", f);
	_printf("Este es el int %i",a);
	_printf("Este es el digit %d", b);
	return (0);
}
