## Python version support updated

The supported Python version range is now correctly documented as >=3.7, <3.14 (Python 3.7 to 3.13).

## Fixed: batch assignment on system variable collections

Calling `read()` on a batch assignment returned by `integer_system_variables.create_batch_assignment()` raised an `AttributeError`. The returned object was not wrapped in the correct Python type. This is now fixed.
