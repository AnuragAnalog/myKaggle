# September Challenge

## Data Description

For this competition, you will predict whether a customer made a `claim` upon an insurance policy. The ground truth claim is binary valued, but a prediction may be any number from `0.0` to `1.0`, representing the probability of a claim. The features in this dataset have been anonymized and may contain missing values.

### Files

* train.csv - the training data with the target claim column
* test.csv - the test set; you will be predicting the claim for each row in this file
* sample_submission.csv - a sample submission file in the correct format

**Kaggle Download API Command**

`kaggle competitions download -c tabular-playground-series-sep-2021`

## Evaluation

Submissions are evaluated on [area under the ROC curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) between the predicted probability and the observed target.

### Submission File
For each `id` in the test set, you must predict a probability for the `claim` variable. The file should contain a header and have the following format:

```
id,claim
957919,0.5
957920,0.5
957921,0.5
etc.
```

## Timeline

* Start Date - September 1, 2021
* Entry deadline - Same as the Final Submission Deadline
* Team Merger deadline - Same as the Final Submission Deadline
* Final submission deadline - September 30, 2021

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.