# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return rounded average COP for online readings with an isolated history list.
- **Current Issue**: Mutable default argument leaks state and zero electrical input causes `ZeroDivisionError`.

## bug2.js
- **Intended Behavior**: Asynchronously fetch active sensors with temperature above 25°C and return the populated list.
- **Current Issue**: `forEach(async ...)` returns an empty array before promises resolve and uses loose equality (`== 1`).

## bug3.c
- **Intended Behavior**: Copy `count` integer readings into a buffer and return their floating-point average.
- **Current Issue**: Off-by-one loop (`i <= count`) causes buffer overflow and integer division truncates decimals.

## bug4.py
- **Intended Behavior**: Return unacknowledged alerts enriched with default metadata without mutating input.
- **Current Issue**: Mutating `alerts` during iteration skips elements and shallow reference reuse overwrites entries.

## bug5.js
- **Intended Behavior**: Return the top `limit` highest temperatures in descending order without mutating input.
- **Current Issue**: Default `.sort()` sorts numbers as strings in place and `slice(0, limit + 1)` returns an extra item.
