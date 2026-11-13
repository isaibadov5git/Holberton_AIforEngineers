## Bug 1 – bug1_fixed.py
**Test Script**:
python
assert get_last_n_items([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert get_last_n_items([1, 2, 3], 5) == [1, 2, 3]
print("Bug 1 fixed!")

- **Input**: `[1, 2, 3, 4, 5], n=3`
- **Expected Output**: `[3, 4, 5]`
- **Actual Output**: `[3, 4, 5]` ✅
- **Confirmation**: Running the assertions passes successfully without off-by-one errors.

## Bug 2 – bug2_fixed.js
**Test Script**:
javascript
const result = findFirstEven([1, 3, 4, 5]);
console.assert(result === 4, "Should return 4");
console.log("Result:", result);
- **Input**: `[1, 3, 4, 5]`
- **Expected Output**: `4`
- **Actual Output**: `4` ✅
- **Confirmation**: Script executes and prints 4, successfully returning out of the `for...of` loop.

## Bug 3 – bug3_fixed.c
**Test Script**:
c
int main() {
char *greet = create_greeting("Alice");
printf("%s\n", greet);
free(greet);
return 0;
}
- **Input**: `"Alice"`
- **Expected Output**: `Hello, Alice` (with exact memory allocation of 13 bytes).
- **Actual Output**: `Hello, Alice` ✅
- **Confirmation**: Code compiles and runs. `malloc` allocates enough bytes, preventing overflow and segmentation faults.

## Bug 4 – bug4_fixed.py
**Test Script**:
python
inv1 = add_item_to_inventory("Sword")
inv2 = add_item_to_inventory("Shield")
assert inv1 == ["Sword"]
assert inv2 == ["Shield"]
print("Bug 4 fixed!")
- **Input**: Call 1 with `"Sword"`, Call 2 with `"Shield"`
- **Expected Output**: `["Sword"]` then `["Shield"]`
- **Actual Output**: `["Sword"]` and `["Shield"]` ✅
- **Confirmation**: Asserts pass. Independent calls no longer share a mutable list.

## Bug 5 – bug5_fixed.js
**Test Script**:
javascript
async function runTest() {
// Mocking global fetch for testing
global.fetch = async () => ({
ok: true,
json: async () => ({ id: 1, name: "Test User" })
});
const data = await fetchUserData(1);
console.log("Resolved Data:", data);
}
runTest();
- **Input**: `fetchUserData(1)`
- **Expected Output**: `{ id: 1, name: 'Test User' }`
- **Actual Output**: `{ id: 1, name: 'Test User' }` ✅
- **Confirmation**: By wrapping the test in an async caller, the exact resolved JSON is printed. The syntax error is gone.

