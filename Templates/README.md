# Templates for faster coding

## Optuna

### Random Forest
```python3
def objective_rf(trial):
    params = dict()
    params['n_estimators'] = trial.suggest_int('n_estimators', 100, 2000, step=100)
    params['max_features'] = trial.suggest_categorical('max_features', ['auto', 'sqrt', 'log2', None])
    params['max_depth'] = trial.suggest_int('max_depth', 2, 5, step=1)
    params['min_samples_split'] = trial.suggest_int('min_samples_split', 2, 10, step=1)
    params['min_samples_leaf'] = trial.suggest_int('min_samples_leaf', 1, 10, step=1)
    params['bootstrap'] = trial.suggest_categorical('bootstrap', [True, False])

    model = RandomForestRegressor(**params, n_jobs=-1)
    model.fit(model.predict(X_train), y_train)

    return mean_squared_error(model.predict(X_valid), y_valid, squared=False)
```

### Extrme Gradient Boosting
```python3
def objective_xgb(trial):
    params = dict()
    params['n_estimators'] = trial.suggest_int('n_estimators', 100, 2000, step=50)
    params['learning_rate'] = trial.suggest_float('learning_rate', 0.1, 0.4, step = 0.1)
    params['max_depth'] = trial.suggest_int('max_depth', 1, 5, step=1)
    params['subsample']= trial.suggest_float('subsample', 0.3, 0.8, step=0.1 )
    params['colsample_bytree'] = trial.suggest_float('colsample_bytree', 0.3, 0.8, step = 0.1)
    params['objective'] = 'reg:linear'
    params['verbosity'] = 0
    params['silent'] = True

    model = XGBRegressor(**params, n_jobs=-1)
    model.fit(model.predict(X_train), y_train)

    return mean_squared_error(model.predict(X_valid), y_valid, squared=False)
```

### LightGBM
```python3
def objective_lgb(trial):
    params = dict()
    params['n_estimators'] = trial.suggest_int('n_estimators', 100, 2000, step=50)
    params['learning_rate'] = trial.suggest_float('learning_rate', 0.1, 0.4, step = 0.1)
    params['max_depth'] = trial.suggest_int('max_depth', 1, 5, step=1)
    params['subsample']= trial.suggest_float('subsample', 0.3, 0.8, step=0.1 )
    params['colsample_bytree'] = trial.suggest_float('colsample_bytree', 0.3, 0.8, step = 0.1)
    params['objective'] = 'regression'
    params['verbosity'] = 0
    params['silent'] = True

    model = LGBMRegressor(**params, n_jobs=-1)
    model.fit(model.predict(X_train), y_train)

    return mean_squared_error(model.predict(X_valid), y_valid, squared=False)
```

### Catboost
```python3
def objective_cat(trial):
    params = dict()
    params['iterations'] = trial.suggest_int('iterations', 100, 2000, step=50)
    params['learning_rate'] = trial.suggest_float('learning_rate', 0.1, 0.4, step = 0.1)
    params['depth'] = trial.suggest_int('depth', 1, 5, step=1)
    params['l2_leaf_reg'] = trial.suggest_float('l2_leaf_reg', 0.3, 0.8, step = 0.1)
    params['border_count'] = trial.suggest_int('border_count', 2, 10, step = 1)
    params['loss_function'] = 'RMSE'
    params['eval_metric'] = 'RMSE'

    model = CatBoostRegressor(**params, n_jobs=-1)
    model.fit(model.predict(X_train), y_train)

    return mean_squared_error(model.predict(X_valid), y_valid, squared=False)
```

### K-Nearest Neighbors
```python3
def objective_knn(trial):
    params = dict()
    params['n_neighbors'] = trial.suggest_int('n_neighbors', 1, 50, step=1)
    params['weights'] = trial.suggest_categorical('weights', ['uniform', 'distance'])
    params['algorithm'] = trial.suggest_categorical('algorithm', ['auto', 'ball_tree', 'kd_tree', 'brute'])
    params['leaf_size'] = trial.suggest_int('leaf_size', 1, 100, step=1)
    params['p'] = trial.suggest_int('p', 1, 5, step=1)

    model = KNeighborsRegressor(**params, n_jobs=-1)
    model.fit(model.predict(X_train), y_train)

    return mean_squared_error(model.predict(X_valid), y_valid, squared=False)
```
