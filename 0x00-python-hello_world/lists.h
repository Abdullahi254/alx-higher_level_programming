#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct my_list - singly linked list
 * @data: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct my_list
{
	int data;
	struct Node *next;
} Node;

int check_cycle(Node *list);

#endif
