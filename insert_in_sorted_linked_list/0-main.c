#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 *main - check the code for Holberton School students.
 *
 *Return: Always 0.
 */
int main(void)
{
listint_t *head;
head = NULL;
add_nodeint_end(&head, 0);
add_nodeint_end(&head, 1);
add_nodeint_end(&head, 2);
add_nodeint_end(&head, 3);
add_nodeint_end(&head, 4);
add_nodeint_end(&head, 98);
add_nodeint_end(&head, 402);
add_nodeint_end(&head, 1024);
print_listint(head);
printf("-----------------\n");
insert_node(&head, 27);
print_listint(head);
printf("-----------------\n");
insert_node(&head, 20);
print_listint(head);
printf("-----------------\n");
insert_node(&head, 5);
print_listint(head);
printf("-----------------\n");
insert_node(&head, 500);
print_listint(head);
printf("-----------------\n");
insert_node(&head, 0);
print_listint(head);
printf("-----------------\n");
insert_node(&head, 10000);
print_listint(head);
free_listint(head);
return (0);
}
