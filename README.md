# My Kaggle Solutions

## Useful Snippets

**Memory Reduction**
```python3
def reduce_memory_dataframe(df, verbose=True):
    # Reduce the DataFrame's Memory by altering the data types of the columns
    
    num_types = ['int8', 'int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_memory = df.memory_usage().sum()
    
    for col in df.columns:
        if df[col].dtypes in num_types:
            c_min = df[col].min()
            c_max = df[col].max()
            
            if 'int' in df[col].dtypes:
                if c_min > np.iinfo(np.int8) and c_max < np.iinfo(np.int8):
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16) and c_max < np.iinfo(np.int16):
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32) and c_max < np.iinfo(np.int32):
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64) and c_max < np.iinfo(np.int64):
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.iinfo(np.float16) and c_max < np.iinfo(np.float16):
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.iinfo(np.float32) and c_max < np.iinfo(np.float32):
                    df[col] = df[col].astype(np.float32)
                elif c_min > np.iinfo(np.float64) and c_max < np.iinfo(np.float64):
                    df[col] = df[col].astype(np.float64)
                    
    end_memory = df.memory_usage().sum()
    
    if verbose:
        print(f"Memory Reduced by {round((end_memory - start_memory) / start_memory, 2)} from {start_memory} to {end_memory}")
        
    return df
```
