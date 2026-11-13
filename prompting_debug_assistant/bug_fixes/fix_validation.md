## Bug 1 – bug1_fixed.py
- **Input**: `get_last_n_items([1, 2, 3, 4, 5], 3)`
- **Expected Output**: `[3, 4, 5]`
- **Actual Output**: `[3, 4, 5]`
- **Confirmation**: The fix works ✔. Testing with edge cases like `n=5` returns `[1, 2, 3, 4, 5]`. The off-by-one error is completely resolved.

## Bug 2 – bug2_fixed.js
- **Input**: `findFirstEven([1, 3, 4, 5])`
- **Expected Output**: `4`
- **Actual Output**: `4`
- **Confirmation**: The fix works ✔. Console execution confirms it immediately stops iterating after finding `4`. Changing `forEach` to `for...of` successfully allows the `return` statement to exit the parent function.

## Bug 3 – bug3_fixed.c
- **Input**: `create_greeting("Alice")`
- **Expected Output**: `Hello, Alice` (with exact memory allocation of 13 bytes).
- **Actual Output**: `Hello, Alice` (verified via stdout).
- **Confirmation**: The fix works ✔. Compiling and running the C code executes cleanly without segmentation faults. Allocating `7 + strlen(name) + 1` correctly accounts for the `\0` terminator, preventing the buffer overflow. 

## Bug 4 – bug4_fixed.py
- **Input**: `add_item_to_inventory("Sword")` followed by `add_item_to_inventory("Shield")`
- **Expected Output**: Call 1 returns `["Sword"]`. Call 2 returns `["Shield"]`.
- **Actual Output**: Call 1 returned `["Sword"]`. Call 2 returned `["Shield"]`.
- **Confirmation**: The fix works ✔. Removing the mutable default list `[]` and replacing it with `None` stops the data from persisting across independent function calls.

## Bug 5 – bug5_fixed.js
- **Input**: `fetchUserData(1)`
- **Expected Output**: A resolved Promise, with no `SyntaxError` during script load.
- **Actual Output**: `Promise { <pending> }` which correctly resolves to fetched JSON data.
- **Confirmation**: The fix works ✔. Adding the `async` keyword allows the JS engine to parse the `await` keyword correctly. The script executes and successfully fetches the data.
