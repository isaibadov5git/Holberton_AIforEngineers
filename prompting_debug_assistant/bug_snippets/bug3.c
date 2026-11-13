#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* create_greeting(const char* name) {
    // BUG: Runtime exception (buffer overflow). 
    // Missed the +1 for the null terminator ('\0'). "Hello, " is 7 chars.
    char *greeting = malloc(7 + strlen(name)); 
    
    if (greeting != NULL) {
        sprintf(greeting, "Hello, %s", name);
    }
    
    return greeting;
}
