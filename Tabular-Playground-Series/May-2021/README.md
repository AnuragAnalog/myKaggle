# May Challenge

## Data Description

The dataset is used for this competition is synthetic, but based on a real dataset and generated using a [CTGAN](https://github.com/sdv-dev/CTGAN). The original dataset deals with predicting the category on an eCommerce product given various attributes about the listing. Although the features are anonymized, they have properties relating to real-world features.

### Files

* train.csv - the training data, one product (`id`) per row, with the associated features (`feature_*`) and class label (`target`)
* test.csv - the test data; you must predict the probability the `id` belongs to each class
* sample_submission.csv - a sample submission file in the correct format

**Kaggle Download API Command**

`kaggle competitions download -c tabular-playground-series-may-2021`

## Evaluation

Submissions are evaluated using multi-class logarithmic loss. Each row in the dataset has been labeled with one true `Class`. For each row, you must submit the predicted probabilities that the product belongs to each class label. The formula is:

where $N$ is the number of rows in the test set, $M$ is the number of class labels, $log$ is the natural logarithm, $y_{ij}$ is 1 if observation $i$ is in class $j$ and 0 otherwise, and $p_{ij}$ is the predicted probability that observation $i$ belongs to class $j$.

The submitted probabilities for a given product are not required to sum to one; they are rescaled prior to being scored, each row is divided by the row sum. In order to avoid the extremes of the $log$ function, predicted probabilities are replaced with $max(min(p, 1 - 10^{-15}), 10^{-15})$.

### Submission File
You must submit a csv file with the product `id` and the predicted probability that the product belongs to each of the classes seen in the dataset. The order of the rows does not matter. The file must have a header and should look like the following:

```
id,Class_1,Class_2,Class_3,Class_4
100000,0.1,0.3,0.2,0.4
100001,0.5,0.1,0.1,0.3
100002,0.4,0.4,0.1,0.1
etc.
```

## Timeline

* Start Date - May 1, 2021
* Entry deadline - Same as the Final Submission Deadline
* Team Merger deadline - Same as the Final Submission Deadline
* Final submission deadline - May 31, 2021

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.