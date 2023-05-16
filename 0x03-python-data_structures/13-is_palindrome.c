#include <stdio.h>
#include "lists.h"

int num_of_nodes(listint_t *head)
{
//this is to count the numbers
	listint_t *curr;
	if (head == NULL)
	{
		return 0;
	}

	int count = 0;
	curr = head;
	while (curr != NULL)
	{
		count++;
		curr = curr->next;
	}
	return count;

}
int is_palindrome(listint_t **head)
{
	listint_t *curr;
//traversing the list to the middle
	int list_middle;
	curr = *head;

	list_middle = num_of_nodes(*head) / 2;
	int dict1[100], i = 0;//dict stores the values of the travesed nodes
	while (i < list_middle)
	{
		dict1[i] = curr->n;
		curr = curr->next;
		i++;
	}
//reversing the linked list to the middle from last
	int dict2[100];//dict2 is for storing the the data of the reversed node up to the middle.
	listint_t *prev = NULL, *next;
	
	int j = list_middle - 1;
	
	while (j > list_middle)//loop from last to middle of list
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
		dict2[j] = prev->n;
		j--;
	}
	//check if list is palindrome or not
	for (i = 0; i != (list_middle * 2); i++)
	{
		if (dict1[i] != dict2[i])
		{
			printf("is  palindrome");
		}
		else
		{
			printf("is not palindrome");
		}
	}
	return 0;
	


}

