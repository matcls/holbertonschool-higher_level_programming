#include "lists.h"

/**
 * insert_node - inserts a new node.
 * @head: pointer to the address of the head of the list.
 * @number: value to add to the new node.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *newnode = NULL;

	if (!head)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);

	newnode->n = number;
	if (!current || current->n >= number)
	{
		newnode->next = current;
		*head = newnode;
		return (newnode);
	}
	while (current && current->next && current->next->n < number)
		current = current->next;

	newnode->next = current->next;
	current->next = newnode;
	return (newnode);
}
