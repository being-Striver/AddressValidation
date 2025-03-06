import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "city": ["New York", "Boston", "Chicago"],
    "job": ["Engineer", "Doctor", "Artist"]
})

# Search for string "o" in multiple columns
search_str = "Doc"

df_filtered = df[df.apply(lambda row: row.astype(str).str.contains(search_str, case=False, na=False).any(), axis=1)]

print(df_filtered)
