# Structured Bug Reports

## Bug Report – bug1.py
- **Summary**: Off-by-one error in list slicing logic.
- **Root Cause**: The conditional guard `if start_index == 0:` forced an artificial offset calculation via `items[start_index + 1:]`, causing the function to drop the first element entirely when `n == len(items)`.
- **Resolution**: Removed the redundant branch logic. Implemented a simplified `max(0, len(items) - n)` bounding constraint to compute the slice index.
- **Lesson Learned**: Python native slicing handles zero indices safely. Avoid writing manual conditional overrides for index boundaries without mathematical verification.

## Bug Report – bug2.js
- **Summary**: Runtime crash (TypeError) caused by unexpected null type payloads.
- **Root Cause**: `JSON.parse("null")` evaluates to primitive `null`. Attempting to access property nested variables `.apiKey` directly on a null value triggers an application exception. Loose validation `== undefined` also failed to catch alternative truthy edge cases.
- **Resolution**: Implemented strong boolean sanity guards checking `if (!config || !config.apiKey)`. Added a manual safety wrapper using a standard defensive `try...catch` block.
- **Lesson Learned**: Always sanitize external raw JSON serialization outputs before inspecting inner payload structures.

## Bug Report – bug3.py
- **Summary**: Shared state contamination across isolated state contexts due to mutable parameters.
- **Root Cause**: The function utilized a mutable object list literal default parameter `current_logs=[]`. Python evaluates function signatures exactly once during binding, causing separate isolated session tracks to use and pollute the exact same tracking reference.
- **Resolution**: Replaced the default parameter initialization state with a clean `None` sentinel value. Added an internal runtime check inside the function to instantiate a fresh list instantiation (`current_logs = []`) locally when required.
- **Lesson Learned**: Never use mutable types (lists, dicts, sets) as default parameters in Python signatures.

## Bug Report – bug4.c
- **Summary**: Memory stack buffer overflow vulnerability via unvalidated iteration conditions.
- **Root Cause**: The string parsing copy traversal loop constraint `i <= src_len` violated index parameters by overstepping structural target thresholds. It allowed characters to write outside expected destinations and failed to mandate null-terminator positioning.
- **Resolution**: Restructured the incremental loop criteria using bounded tracking gates `i < src_len && i < (dest_size - 1)`. Added an explicit statement string assignment `dest[i] = '\0'` right outside execution lines.
- **Lesson Learned**: Explicitly pass destination capacity metadata buffers inside low-level tracking operations to completely eliminate out-of-bounds security holes.
