## Bug 1 – bug1.py
**AI Diagnosis**: The `range` function starts at `len(items) - n + 1`, which skips the first element of the desired sublist, resulting in an off-by-one error.
**Suggested Fix**: Change the loop to `for i in range(len(items) - n, len(items)):`.
**Alternative Fixes Tested**: Using Python list slicing instead: `return items[-n:]`.
**Result**: Both fixes work, but the list slicing approach is much more efficient and standard for Python.

## Bug 2 – bug2.js
**AI Diagnosis**: The `return num` statement is inside a `forEach` callback. It only exits the callback for that specific iteration, not the parent `findFirstEven` function, causing the function to always return `null`.
**Suggested Fix**: Replace the `forEach` loop with a standard `for...of` loop so the `return` statement properly exits the outer function.
**Alternative Fixes Tested**: Using the built-in array method: `return numbers.find(num => num % 2 === 0) || null;`.
**Result**: Both fixes resolve the logic error. The `.find()` method is generally preferred for this use case in JavaScript.

## Bug 3 – bug3.c
**AI Diagnosis**: The `malloc` call allocates exactly enough space for the string characters but forgets to allocate an extra byte for the null terminator (`\0`). This leads to a buffer overflow when `sprintf` writes the string.
**Suggested Fix**: Add `+ 1` to the allocation: `char *greeting = malloc(7 + strlen(name) + 1);`.
**Alternative Fixes Tested**: None.
**Result**: The fix works as expected and resolves the memory corruption issue.

## Bug 4 – bug4.py
**AI Diagnosis**: Using a mutable list `[]` as a default argument means the list is created only once when the function is defined. Successive calls without providing the `inventory` argument will incorrectly share the exact same list.
**Suggested Fix**: Set the default argument to `None`, and initialize the list inside the function if it is missing.
**Alternative Fixes Tested**: None.
**Result**: The fix works perfectly. Changing the definition to `def add_item_to_inventory(item, inventory=None):` and adding `if inventory is None: inventory = []` ensures a fresh list is created per call.

## Bug 5 – bug5.js
**AI Diagnosis**: The `await` keyword is being used inside `fetchUserData`, which is declared as a synchronous function. This throws a `SyntaxError` immediately upon parsing.
**Suggested Fix**: Add the `async` keyword to the function declaration: `async function fetchUserData(userId)`.
**Alternative Fixes Tested**: Refactoring the code to use `.then()` promise chaining instead of `async/await`.
**Result**: Adding the `async` keyword is the cleanest fix and keeps the code readable, resolving the syntax error entirely.
