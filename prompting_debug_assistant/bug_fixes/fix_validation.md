## Bug 1 – bug1_fixed.py
- **Input**: [1, 2, 3, 4, 5], n=3
- **Expected Output**: [3, 4, 5]
- **Actual Output**: [3, 4, 5] ✅
- **Test Executed**: Ran `print(get_last_n_items([1, 2, 3, 4, 5], 3))` in Python.
- **Fix Confirmation**: The function no longer skips the first element of the sublist.

## Bug 2 – bug2_fixed.js
- **Input**: [1, 3, 4, 5]
- **Expected Output**: 4
- **Actual Output**: 4 ✅
- **Test Executed**: Ran `console.log(findFirstEven([1, 3, 4, 5]));` in Node.js.
- **Fix Confirmation**: Replaced forEach with a standard loop; the function returns successfully.

## Bug 3 – bug3_fixed.c
- **Input**: "Alice"
- **Expected Output**: "Hello, Alice"
- **Actual Output**: "Hello, Alice" ✅
- **Test Executed**: Compiled with GCC and ran a `main` function calling `printf("%s\n", create_greeting("Alice"));`
- **Fix Confirmation**: Memory allocation is now correct, buffer overflow is resolved.

## Bug 4 – bug4_fixed.py
- **Input**: Call 1 with "Sword", Call 2 with "Shield"
- **Expected Output**: Call 1 returns ["Sword"], Call 2 returns ["Shield"]
- **Actual Output**: Call 1 returned ["Sword"], Call 2 returned ["Shield"] ✅
- **Test Executed**: Ran `print(add_item_to_inventory("Sword")); print(add_item_to_inventory("Shield"));` sequentially.
- **Fix Confirmation**: Function correctly maintains separate inventory lists per call.

## Bug 5 – bug5_fixed.js
- **Input**: userId = 1
- **Expected Output**: Parsed JSON object.
- **Actual Output**: Parsed JSON object. ✅
- **Test Executed**: Ran `fetchUserData(1).then(data => console.log(data));` in Node environment.
- **Fix Confirmation**: SyntaxError is resolved; async function correctly awaits the fetch operation.
