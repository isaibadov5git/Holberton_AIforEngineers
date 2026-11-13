## Bug Report – bug1.py
- **Summary**: Function returns the wrong sublist due to an off-by-one error.
- **Root Cause**: The `range` start index incorrectly added `1` (`len(items) - n + 1`), skipping the first element of the target sublist.
- **Resolution**: Removed the `+ 1` from the range start, as suggested by AI. No manual edits were required.
- **Lesson Learned**: Always manually trace or print loop boundaries when working with index calculations to avoid off-by-one mistakes.

## Bug Report – bug2.js
- **Summary**: Function always returns `null` instead of the first even number.
- **Root Cause**: Using `return` inside a `forEach` loop only exits the inner callback function, not the parent function.
- **Resolution**: AI suggested replacing `forEach` with a standard `for...of` loop, allowing the `return` statement to correctly exit the outer function.
- **Lesson Learned**: Be cautious with array methods like `forEach` when flow control (like early returns or `break`) is needed.

## Bug Report – bug3.c
- **Summary**: Memory corruption / buffer overflow when creating a greeting string.
- **Root Cause**: The `malloc` call allocated space for the characters but forgot the extra 1 byte needed for the string's null terminator (`\0`).
- **Resolution**: AI suggested adding `+ 1` to the `malloc` size calculation. Manually verified with C string standards.
- **Lesson Learned**: Always account for the hidden `\0` byte when dynamically allocating memory for strings in C.

## Bug Report – bug4.py
- **Summary**: Inventory items persist across independent function calls.
- **Root Cause**: Using a mutable object (`[]`) as a default argument means the list is instantiated only once at function definition time, not per call.
- **Resolution**: AI suggested replacing the default `inventory=[]` with `inventory=None`, and initializing it to `[]` inside the function body.
- **Lesson Learned**: Never use mutable types (lists, dictionaries) as default arguments in Python.

## Bug Report – bug5.js
- **Summary**: Script throws a `SyntaxError` and fails to parse.
- **Root Cause**: The `await` keyword was used inside a standard, synchronous function. `await` is only valid inside `async` functions.
- **Resolution**: AI suggested adding the `async` keyword to the `fetchUserData` function declaration.
- **Lesson Learned**: Always pair `await` with `async` when writing asynchronous JavaScript code.
