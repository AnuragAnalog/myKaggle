# August Challenge

## Data Description

For this competition, you will be predicting a target `loss` based on a number of feature columns given in the data. The ground truth `loss` is integer valued, although predictions can be continuous.

### Files

* train.csv - the training data with the target `loss` column
* test.csv - the test set; you will be predicting the `loss` for each row in this file
* sample_submission.csv - a sample submission file in the correct format

**Kaggle Download API Command**

`kaggle competitions download -c tabular-playground-series-aug-2021`

## Evaluation

Submissions are scored on the root mean squared error. RMSE is defined as:

$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$

where  is the predicted value,  is the ground truth value, and  is the number of rows in the test data. 

### Submission File
For each row `id` in the test set, you must predict the value of the target `loss` as described on the data tab, each on a separate row in the submission file. The file should contain a header and have the following format:

```
id,loss
250000,0.0
250001,10.3
250002,42.42
etc.
```

## Timeline

* Start Date - August 1, 2021
* Entry deadline - Same as the Final Submission Deadline
* Team Merger deadline - Same as the Final Submission Deadline
* Final submission deadline - August 31, 2021

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.