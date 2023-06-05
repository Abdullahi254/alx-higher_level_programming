#include "lists.h"
/**
 * check_cycle - checks for cycle
 * @list: pointer to linked list
 * Return: 1 for true or 0 for false
 */
int check_cycle(Node *list)
{
	Node *second = list;
	Node *first = list;

	while (first != NULL && first->next != NULL)
	{
		second = second->next;
		first = first->next->next;
	if (second == first)
		return (1);
	}
	return (0);

}
