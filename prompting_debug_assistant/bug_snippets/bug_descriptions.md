## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The loop starts one index too late, missing the first item of the requested sublist.

## Bug 2 – bug2.js
**Intended Behavior**: Find and return the first even number in an array.  
**Issue Type**: Logical error.  
**Notes**: Uses `return` inside a `forEach` callback, which doesn't exit the outer function. It always returns `null`.

## Bug 3 – bug3.c
**Intended Behavior**: Allocate and return a greeting string for a given name.  
**Issue Type**: Runtime exception (Buffer Overflow).  
**Notes**: `malloc` does not allocate space for the null terminator `\0`, leading to memory corruption.

## Bug 4 – bug4.py
**Intended Behavior**: Add an item to an inventory list and return it. If no list is provided, create a new one.  
**Issue Type**: Misuse of data types (Mutable default argument).  
**Notes**: The default list is created only once when the function is defined, causing state to persist across calls.

## Bug 5 – bug5.js
**Intended Behavior**: Fetch user data from an API and return the parsed JSON.  
**Issue Type**: Syntax error.  
**Notes**: The `await` keyword is used inside a regular, non-async function, which throws a SyntaxError during parsing.
