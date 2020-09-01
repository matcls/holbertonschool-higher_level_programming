#include "lists.h"

/**
 * check_cycle - finds the loop in a linked list.
 * @list: pointer to the address of the first node of the list.
 *
 * Return: 1 if there is a loop,
 * or 0 if there is no loop
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = NULL, *hare = NULL;

	turtle = list, hare = list;

	while (list && hare && hare->next && hare->next->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		
		if (turtle == hare)
			return (1);
	}
	return (0);
}
