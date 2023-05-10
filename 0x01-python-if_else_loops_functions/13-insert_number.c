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
	listint_t *fastptr, *slowptr, *prevSlowptr;
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
	
	fastptr = *head;
	slowptr = *head;
	prevSlowptr = NULL;

	while (fastptr != NULL && fastptr->next != NULL)
	{
		fastptr = fastptr->next->next;
		prevSlowptr = slowptr;
		slowptr = slowptr->next;
	}
	new_node->next = slowptr;
	prevSlowptr->next = new_node;

	return (new_node);
}
