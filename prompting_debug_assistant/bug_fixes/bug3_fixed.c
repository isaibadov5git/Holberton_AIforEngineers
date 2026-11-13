#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* create_greeting(const char* name) {
    printf("Allocating memory for greeting...\n");
    
    // FIXED: Added + 1 for the null terminator ('\0').
    char *greeting = malloc(7 + strlen(name) + 1); 
    
    if (greeting != NULL) {
        sprintf(greeting, "Hello, %s", name);
        printf("Greeting created successfully.\n");
    } else {
        printf("Memory allocation failed!\n");
    }
    
    return greeting;
}
