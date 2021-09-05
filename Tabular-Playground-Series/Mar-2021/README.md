# March Challenge

## Data Description

For this competition, you will be predicting a binary target based on a number of feature columns given in the data. All of the feature columns, `cat0` - `cat18` are categorical, and the feature columns `cont0` - `cont10` are continuous.

### Files

* train.csv - the training data with the `target` column
* test.csv - the test set; you will be predicting the `target` for each row in this file (the probability of the binary target)
* sample_submission.csv - a sample submission file in the correct format

**Kaggle Download API Command**

`kaggle competitions download -c tabular-playground-series-mar-2021`

## Evaluation

Submissions are evaluated on [area under the ROC curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) between the predicted probability and the observed target.

### Submission File

For each row in the test set, you must predict the probability of a binary target as described on the data tab, each on a separate row in the submission file. The file should contain a header and have the following format:

For each ID in the test set, you must predict a probability for the TARGET variable. The file should contain a header and have the following format:

```
id,target
5,0.5
6,0.1
8,0.9
etc.
```

## Timeline

* Start Date - March 1, 2021
* Entry deadline - Same as the Final Submission Deadline
* Team Merger deadline - Same as the Final Submission Deadline
* Final submission deadline - March 31, 2021

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.