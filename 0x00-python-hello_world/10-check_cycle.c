#include "lists.h"
/**
 * check_cycle - Func checks linked list contains for a cycle
 * @list: linked list
 *
 * Return: 1 for a cycle, 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *u;
	listint_t *v;

	if (list == NULL || list->next == NULL)
		return (0);

	u = list->next;
	v = list->next->next;

	while (u && v && v->next)
	{
		u = u->next;
		v = v->next->next;

		if (u == v)
			return (1);
	}
	return (0);
}
