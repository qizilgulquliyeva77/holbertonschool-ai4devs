## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error / Logical error.  
**Notes**: The function fails and slices incorrectly when n == len(items).  

## Bug 2 – bug2.js
**Intended Behavior**: Parse JSON user configuration data and return an uppercase API key.  
**Issue Type**: Runtime exception / Type checking anomaly.  
**Notes**: Throws a TypeError if the incoming valid JSON string resolves to null.  

## Bug 3 – bug3.py
**Intended Behavior**: Track state by appending an action to a local list instance per invocation.  
**Issue Type**: Misuse of data types / Mutable default arguments.  
**Notes**: Reuses the same list reference across distinct function calls, polluting different user sessions.  

## Bug 4 – bug4.c
**Intended Behavior**: Copy string safely from source to bound destination buffer.  
**Issue Type**: Memory buffer overflow / Index bounds violation.  
**Notes**: Missing explicit length validation checks and utilizes unsafe boundary limits inside the index loop.  
