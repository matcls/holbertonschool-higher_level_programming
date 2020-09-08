#include "lists.h"

/**
 * finds_palindrome - checks if a list is a palindrome
 * @head:      head of the list to be checked
 * @length:    iterator to help find if is palindrome
  * Return: returns 1 if is a palindrome and 0 if not.
 */
int finds_palindrome(listint_t **head, listint_t *length)
{
	if (!length)
		return (1);

	if (finds_palindrome(head, length->next) == 1 && (*head)->n == length->n)
	{
		(*head) = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: ahead of the list to be checked
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (finds_palindrome(head, *head));
}
