#include "lists.h"
/**
 * insert_node - Functions insert number into singly-linked ls
 * @head: Head of linked list
 * @number: Number to include
 *
 * Return: NULL if failed,otherwise ptr to node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *u = *head;
	listint_t *v;

	v = malloc(sizeof(listint_t));
	if (v == NULL)
		return (NULL);
	v->n = number;

	if (u == NULL || u->n >= number)
	{
		v->next = u;
		*head = v;
		return (v);
	}

	while (u && u->next && u->next->n < number)
		u = u->next;
	v->next = u->next;
	u->next = v;
	return (v);
}
