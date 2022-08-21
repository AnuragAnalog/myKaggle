# My Kaggle Solutions

## Useful Snippets

### Preprocessing
**Extended Label Encoder**

class LabelEncoderExt(TransformerMixin, BaseEstimator):
    def __init__(self, classes=None):
        self.classes = classes

    def fit(self, y):
        if self.classes is None:
            self.classes = np.unique(y)

        self.encoding = {k: v for v, k in enumerate(self.classes, start=0)}

    def transform(self, y):
        return y.map(self.encoding)

    def fit_transform(self, y):
        self.fit(y)

        return self.transform(y)

**Extended One Hot Encoder**


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
            
            if str(df[col].dtype).find('int') != 1:
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            elif str(df[col].dtype).find('float') != 1:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                elif c_min > np.finfo(np.float64).min and c_max < np.finfo(np.float64).max:
                    df[col] = df[col].astype(np.float64)
                    
    end_memory = df.memory_usage().sum()
    
    if verbose:
        print(f"Memory Reduced by {round((start_memory - end_memory) / start_memory, 2)} from {start_memory} to {end_memory}")
        
    return df
```
