#include "lists.h"

/**
 *insert_node - insert a new number into a sorted single
 *@head: first node
 *@number: new number to insert
 *Return: new inserted node
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *previous;
listint_t *current;

current = *head;
previous = *head;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL);
}

if (*head == NULL)
{
*head = new_node;
}
else
{
new_node->n = number;
new_node->next = NULL;
while (current->n < number)
{
previous = current;
current = current->next;
if (current == NULL)
{
previous->next = new_node;
}
else if (current->n >= number){
    previous->next = new_node;
    new_node->next = current;
}
}
}
return (new_node);
}
