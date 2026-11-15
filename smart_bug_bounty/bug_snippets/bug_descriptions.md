# Bug Descriptions

## bug1.py
- **Intended Behavior**: Calculate the rounded average Coefficient of Performance (COP) for online thermal readings and append valid COP values to a per-call history list without crashing when input readings are empty or have zero electrical input.
- **Current Issue**: Uses a mutable default argument (`history=[]`) that leaks state across function calls, throws a `ZeroDivisionError` when `electric_kw` is `0` or no `"ONLINE"` readings exist, and raises a `KeyError` if optional keys are missing.

## bug2.js
- **Intended Behavior**: Asynchronously fetch sensor details for every station ID in `stationIds`, filter for active sensors (`status === true` or `"ACTIVE"`) with temperatures above `25°C`, and return the populated array once all requests resolve.
- **Current Issue**: Uses `Array.prototype.forEach` with an `async` callback, causing `fetchActiveSensors` to return an empty array `[]` immediately before any `await apiClient.getSensor(id)` promises settle, and uses loose equality (`== 1`) which causes unintended type coercion.

## bug3.c
- **Intended Behavior**: Copy up to `count` integer temperature readings into a local buffer and return their exact floating-point arithmetic mean.
- **Current Issue**: Off-by-one loop condition (`i <= count`) reads out of bounds on `readings[5]` and triggers a stack buffer overflow on `buffer[5]`, while `sum / count` performs truncating integer division instead of floating-point division.

## bug4.py
- **Intended Behavior**: Return a new list of unacknowledged alert dictionaries enriched with default metadata without mutating the caller's input list or overwriting previous items.
- **Current Issue**: Mutates the `alerts` list in place while iterating over it (causing elements immediately following an acknowledged alert to be skipped), and assigns `entry = default_config` by reference so every item in `cleaned` points to the exact same overwritten dictionary.

## bug5.js
- **Intended Behavior**: Return the top `limit` highest numeric temperatures in descending order without mutating the original `readings` array.
- **Current Issue**: `readings.sort()` mutates the caller's array in place and sorts numbers lexicographically as UTF-16 strings (putting `102.4` before `24.8` and `9.5` last), and `slice(0, limit + 1)` has an off-by-one error returning `limit + 1` elements.
