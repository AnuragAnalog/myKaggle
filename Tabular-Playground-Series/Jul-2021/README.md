# August Challenge

## Data Description

In this competition you are predicting the values of air pollution measurements over time, based on basic weather information (temperature and humidity) and the input values of 5 sensors.

The three target values to you to predict are: `target_carbon_monoxide`, `target_benzene`, and `target_nitrogen_oxides`

### Files

* train.csv - the training data, including the weather data, sensor data, and values for the 3 targets
* test.csv - the same format as `train.csv`, but without the target value; your task is to predict the value for each of these targets.
* sample_submission.csv - a sample submission file in the correct format.

**Kaggle Download API Command**

`kaggle competitions download -c tabular-playground-series-jul-2021`

## Evaluation

Submissions are evaluated using the mean column-wise root mean squared logarithmic error.

The RMSLE for a single column calculated as:

$\sqrt{\frac{1}{n}\sum_{i=1}^{n}(log(p_i + 1) - log(a_i + 1))^{2}}$

where:

$n$ is the total number of observations

$p_i$ is your prediction

$a_i$ is the actual value

$log(x)$ is the natural logarithm of $x$

The final score is the mean of the RMSLE over all columns, in this case, 3.

### Submission File
For each ID in the test set, you must predict a probability for the TARGET variable. The file should contain a header and have the following format:

```
date_time,target_carbon_monoxide,target_benzene,target_nitrogen_oxides
2011-01-01 01:00:00,2.0,10.0,300.0
2011-01-01 02:00:00,2.0,10.0,300.0
2011-01-01 03:00:00,2.0,10.0,300.0
etc.
```

## Timeline

* Start Date - July 1, 2021
* Entry deadline - Same as the Final Submission Deadline
* Team Merger deadline - Same as the Final Submission Deadline
* Final submission deadline - July 31, 2021

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.