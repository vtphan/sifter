rows.py parses a delimited text files into "rows".  Delimited text files can be comma-separated
or tab-separated files.

Delimited files must have a well-defined format, where the first row must specify names of all columns.
There must be no missing values.

You can select rows based on desirable contions on columns.


### Reading delimited text files

Read in a comma-separated text file

```
	import rows

	crime_data = rows.read("crimeRatesByState2005.csv", ',')
```

Read a tab-separated file, skip 3 lines in the beginning of file

```
	some_data = read("data.txt", sep='\t', skip_header=3)   
```

### Selecting all rows and only rows satisfied specified conditions on column(s)

Short cut to getting a list of all values in column "state"
```
	states = crime_data['state']
```

A more expressive way of getting a list of all values in column "state"
```
	states = [ r['state'] for r in crime_data ]
```

Get of all values in column "state" where values in column "murder" (of the same rows) are higher than 5.0
```
	states = [ r['state'] for r in crime_data if r['murder'] > 5.0 ]
```

A list of states with murder rate < 3.0 and rate robbery < 100.0
```
	states = [ (r['state'],r['murder'],r['robbery']) for r in crime_data if r['murder'] < 3.0 and r['robbery'] < 100.0 ]
```
