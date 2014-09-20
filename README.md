This modules parses a delimited text files into data objects.  Delimited text files can be comma-separated or tab-separated files.

Delimited files must have a well-defined format, where the first row must specify names of all columns.
There must be no missing values.

You can select rows based on desirable contions on columns.


### Reading delimited text files

Read in a comma-separated text file

```
	import sifter

	crime_data = rows.read("crimeRatesByState2005.csv", ',')
```

Read a tab-separated file, skip 3 lines in the beginning of file

```
	some_data = read("data.tsv", '\t', skip_header=3)
```

### Selecting columns and rows

Short cut to getting a list of all values in column "state"
```
	states = crime_data['state']
```

A more expressive way of getting a list of all values in column "state"
```
	states = [ r['state'] for r in crime_data ]
```

### Selecting rows satisfied specified conditions on column(s)

Get of all values in column "state" where values in column "murder" (of the same rows) are higher than 5.0
```
	states = [ r['state'] for r in crime_data if r['murder'] > 5.0 ]
```

A list of states with murder rate < 3.0 and rate robbery < 100.0
```
	states = [ (r['state'],r['murder'],r['robbery']) for r in crime_data if r['murder'] < 3.0 and r['robbery'] < 100.0 ]
```

### Grouping data by column values

group_by returns a dictionary whose keys are values in the given column name.

```
   groups = crime_data.group_by('politics')
```

Checking if selected data satisfy certain conditions

```
   all( r['murder'] > 1.0 for r in groups['Red'] )
   any( r['murder'] > 8.0 for r in groups['Red'] )
```

