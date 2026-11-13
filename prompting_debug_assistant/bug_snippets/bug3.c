#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* create_greeting(const char* name) {
    printf("Allocating memory for greeting...\n");
    
    // BUG: Runtime exception (buffer overflow). 
    // Missed the +1 for the null terminator ('\0'). "Hello, " is 7 chars.
    // If name is "Alice" (5 chars), malloc allocates 12 bytes.
    // But "Hello, Alice" + '\0' requires 13 bytes.
    char *greeting = malloc(7 + strlen(name)); 
    
    if (greeting != NULL) {
        // sprintf will write the null terminator into unallocated memory
        sprintf(greeting, "Hello, %s", name);
        printf("Greeting created successfully.\n");
    } else {
        printf("Memory allocation failed!\n");
    }
    
    return greeting;
}
