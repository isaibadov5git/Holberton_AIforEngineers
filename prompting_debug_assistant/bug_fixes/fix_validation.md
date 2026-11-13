## Bug 1 – bug1_fixed.py
**Input**: `get_last_n_items([1, 2, 3, 4, 5], 3)`  
**Expected Output**: `[3, 4, 5]`  
**Actual Output**: `[3, 4, 5]` ✅  

## Bug 2 – bug2_fixed.js
**Input**: `findFirstEven([1, 3, 4, 5])`  
**Expected Output**: `4`  
**Actual Output**: `4` ✅  

## Bug 3 – bug3_fixed.c
**Input**: `create_greeting("Alice")`  
**Expected Output**: `"Hello, Alice"` without memory corruption.  
**Actual Output**: `"Hello, Alice"` successfully formatted with no buffer overflow. ✅  

## Bug 4 – bug4_fixed.py
**Input**: `add_item_to_inventory("Sword")` then `add_item_to_inventory("Shield")`  
**Expected Output**: `["Sword"]` then `["Shield"]` (isolated lists).  
**Actual Output**: `["Sword"]` and `["Shield"]` correctly return separate lists. ✅  

## Bug 5 – bug5_fixed.js
**Input**: `fetchUserData(1)`  
**Expected Output**: Function parses without SyntaxError and returns a Promise resolving to JSON.  
**Actual Output**: Promise successfully executes and returns mocked JSON data. ✅
