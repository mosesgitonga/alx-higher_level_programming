#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserting a node
 * @head: first node
 * @number: number to be added
 * Return: newnnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
	}
	else
	{
		listint_t *curr = malloc(sizeof(listint_t));

		curr = *head;

		while (curr->next != NULL)
		{
			curr = curr->next;
		}
		curr->next = new_node;

	}
	return (new_node);
}
