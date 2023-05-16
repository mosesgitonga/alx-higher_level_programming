#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head;
    listint_t *fast = *head;

    // Move fast pointer by two nodes and slow pointer by one node
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    // Reverse the second half of the linked list
    listint_t *prev = NULL;
    listint_t *next = NULL;
    while (slow != NULL)
    {
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    // Compare the first half and reversed second half
    listint_t *first_half = *head;
    listint_t *second_half = prev;
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
            return 0;
        first_half = first_half->next;
        second_half = second_half->next;
    }

    return 1;
}

