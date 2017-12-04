#include "lists.h"
/**
 * check_cycle - function will check if loop exists in list
 * @list: represents pointer to linked list
 * Return: function will return 1 if cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *single;
	listint_t *dubble;

	single = list;
	dubble = list->next;
	while (single->next != NULL && dubble->next != NULL)
	{
		if (single->next == dubble->next)
			return (1);
		single = single->next;
		dubble = dubble->next->next;
	}
	return (0);
}
