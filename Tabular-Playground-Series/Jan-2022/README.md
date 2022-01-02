# January 2022 Challenge

## Data Description

For this challenge, you will be predicting a full year worth of sales for three items at two stores located in three different countries. This dataset is completely fictional, but contains many effects you see in real-world data, e.g., weekend and holiday effect, seasonality, etc. The dataset is small enough to allow you to try numerous different modeling approaches.

Good luck!

### Files

* train.csv - the training set, which includes the sales data for each date-country-store-item combination.
* test.csv - the test set; your task is to predict the corresponding item sales for each date-country-store-item combination. Note the Public leaderboard is scored on the first quarter of the test year, and the Private on the remaining.
* sample_submission.csv - a sample submission file in the correct format

**Kaggle Download API Command**

`kaggle competitions download -c tabular-playground-series-jan-2022`

## Evaluation

Submissions are evaluated on [SMAPE](https://en.wikipedia.org/wiki/Symmetric_mean_absolute_percentage_error) between forecasts and actual values. We define SMAPE = 0 when the actual and predicted values are both 0.

### Submission File

For each `row_id` in the test set, you must predict the corresponding `num_sold`. The file should contain a header and have the following format:

```
row_id,num_sold
26298,100
26299,100
26300,100
etc.
```

## Timeline

* Start Date - January 1, 2022
* Entry deadline - Same as the Final Submission Deadline
* Team Merger deadline - Same as the Final Submission Deadline
* Final submission deadline - January 31, 2022

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.
