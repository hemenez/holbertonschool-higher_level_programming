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

	if (list == NULL)
		return (0);
	single = list;
	dubble = list->next;
	if (single == NULL || dubble == NULL)
		return (0);
	while (single->next != NULL && dubble->next != NULL)
	{
		single = single->next;
		dubble = dubble->next->next;
		if (single == dubble)
			return (1);
	}
       	return (0);
}
