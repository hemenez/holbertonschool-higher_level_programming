#include "lists.h"
/**
 * insert_node - function will insert new node
 * @head: represents double pointer to head
 * @number: represents number to be added
 * Return: function will return pointenr to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;

	new = malloc(sizeof(*new));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	tmp = *head;
	new->n = number;
	while (tmp->next != NULL)
	{
		if (*head == NULL || tmp == NULL)
		{
			new->next = NULL;
			*head = new;
			return (new);
		}
		if (tmp->n <= new->n && tmp->next->n >= new->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
