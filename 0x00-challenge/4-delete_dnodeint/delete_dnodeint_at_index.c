#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *saved_head;
	dlistint_t *tmp;
	unsigned int p;

	/* Empty list */
	if (*head == NULL)
	{
		return (-1);
	}

	/* Remove at the begining of the list */
	if (index == 0)
	{
		tmp = (*head)->next;
		free(*head);
		*head = tmp;
		if (tmp != NULL)
		{
			tmp->prev = NULL;
		}
		return (1);
	}

	/* Remove at position `index` of the list */
	saved_head = *head;
	p = 0;
	while (p < index && *head != NULL)
	{
		*head = (*head)->next;
		p++;
	}
	/* Index out of range */
	if (p != index)
	{
		*head = saved_head; /* Assign saved node to head */
		return (-1);
	}
	else
	{
		/* Delete node at that position */
		(*head)->prev->next = (*head)->next;
		if ((*head)->next)
		{
			(*head)->next->prev = (*head)->prev;
		}
		free(*head);
		*head = saved_head;
	}
	return (1);
}
