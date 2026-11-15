# Fix Validation Report

## bug1.py (`bug1_fixed.py`)
- **Original Issue**: Mutable default argument (`history=[]`) leaked state across calls and zero electrical input or empty readings raised `ZeroDivisionError`.
- **Fix Applied**: Changed default parameter to `history=None`, guarded against `electric_kw <= 0`, and returned `0.0, history` when `valid_cops` is empty.
- **Test Results**: All 4 test cases passed (standard COP calculation, zero-watt input skipped, empty readings list handled safely, isolated history across consecutive calls).

## bug2.js (`bug2_fixed.js`)
- **Original Issue**: `forEach(async ...)` returned an empty array before API promises resolved and used loose equality (`== 1`).
- **Fix Applied**: Replaced `forEach` with `Promise.all(stationIds.map(...))` and enforced strict equality (`response.status === 1`).
- **Test Results**: All 3 test cases passed (resolved async sensor objects returned accurately, sensors below 25°C excluded, string `"1"` status rejected).

## bug3.c (`bug3_fixed.c`)
- **Original Issue**: Off-by-one loop (`i <= count`) caused out-of-bounds read/stack overflow and integer division truncated fractional averages.
- **Fix Applied**: Changed loop boundary to `i < count`, added bounds check (`count <= 0 || count > 5`), and cast numerator via `(double)sum / count`.
- **Test Results**: Compiled cleanly with `gcc -Wall -Wextra -Werror` (zero warnings) and passed 3 test cases (`{24, 25, 26, 25, 27}` returns `25.40` without overflow).

## bug4.py (`bug4_fixed.py`)
- **Original Issue**: Mutating `alerts` in place during iteration skipped adjacent elements and shallow dictionary reference reuse overwrote previous items.
- **Fix Applied**: Iterated without mutating `alerts`, replaced mutable default argument with `None`, and cloned metadata per item using `base_config.copy()`.
- **Test Results**: All 3 test cases passed (consecutive acknowledged alerts skipped cleanly, distinct dictionary IDs preserved in output, original list unmutated).

## bug5.js (`bug5_fixed.js`)
- **Original Issue**: Default `.sort()` mutated the input array and sorted numbers lexicographically as strings, while `slice(0, limit + 1)` returned an extra item.
- **Fix Applied**: Cloned input via `[...readings]`, applied numeric descending comparator `(a, b) => b - a`, and sliced with `.slice(0, limit)`.
- **Test Results**: All 3 test cases passed (`[9.5, 28.1, 102.4, 31.0, 24.8, 19.2]` with `limit = 3` returned `[102.4, 31, 28.1]` and left `tunnelTemps` unmutated).
