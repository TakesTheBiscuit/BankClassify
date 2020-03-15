
### Many accounts analysis
You are able to use this with many accounts. An example `example_full.py` exists.
`example_full.py` uses `Classify` which in turn loads all subdirectories inside `input_directory`, for example:

```
input
  - barclays_TakesTheBiscuit
    - month1.csv
    - month2.csv
  - lloyds_SomeOtherAccount
    - month1.csv
    - month2.csv
```

We ingest csv files from these sub directories, using the first part (before `_`) to identify the account type. See 'supported banks' elsewhere.

Training data is then stored back to a directory `cache` with one file per account, following the example input directory layout above:

```
cache
  - barclays_TakesTheBiscuit.csv
  - lloyds_SomeOtherAccount
```

In practice: each month you would simply drop your new months .csv file into the right input sub directory and run: `python3 Classify.py` to ingest the files and analyse them.

Output: the training data files from cache above are for classifying statements - outputs are provided into an output directory, continuing the example above:

```
ouput
  - barclays_TakesTheBiscuit
    - income_month1.csv
    - outgoing_month1.csv
    - income_month2.csv
    - outgoing_month2.csv

  - lloyds_SomeOtherAccount
    - income_month1.csv
    - outgoing_month1.csv
    - income_month2.csv
    - outgoing_month2.csv
```