## Breaking changes

- Removed `equals` and `get_hash_code` methods from all data classes. Use the standard Python `==` operator and `hash()` built-in instead.

## Improvements

- Methods that previously had multiple overloads are now exposed as a single method with union-typed parameters (e.g. `float | int | str`). This aligns with Python conventions and avoids name collisions.
