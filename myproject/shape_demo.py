import pandas as pd

# CORRECT: include the .csv extension
df = pd.read_csv('product_catalog_2024.csv', encoding_errors='ignore')

# 1) .shape is a PROPERTY (attribute), no parentheses -> correct
print('df.shape (correct):', df.shape)

print()

# 2) Calling it like a method -> TypeError
try:
    df.shape()
except Exception as e:
    print('df.shape() (wrong):', type(e).__name__, '-', e)

print()

# 3) Missing .csv extension -> FileNotFoundError
try:
    pd.read_csv('product_catalog_2024', encoding_errors='ignore')
except Exception as e:
    print("read_csv('product_catalog_2024') (wrong):", type(e).__name__, '-', e)
