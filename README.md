# Cloudfide Virtual Column Utility

This project provides a utility function to add a virtual column to a pandas DataFrame based on a mathematical expression involving existing columns.

## Files

- [`solution.py`](solution.py): Contains the [`add_virtual_column`](solution.py) function.
- [`test_virtual_column 1.py`](test_virtual_column 1.py): Unit tests for the virtual column function.

## Usage

Import the function and use it with your DataFrame:

```python
import pandas as pd
from solution import add_virtual_column

df = pd.DataFrame([[1, 2]], columns=["a", "b"])
df_new = add_virtual_column(df, "a + b", "c")
print(df_new)
```

## Running Tests

To run the tests, use:

```sh
pytest "test_virtual_column 1.py"
```

## Function Details

### [`add_virtual_column`](solution.py)

Adds a new column to a DataFrame based on a mathematical expression.

**Parameters:**
- `df`: Input pandas DataFrame.
- `role`: String expression (e.g., `"col1 + col2"`).
- `new_column`: Name for the new column.

Returns a new DataFrame with the added column, or an empty DataFrame if the input is
