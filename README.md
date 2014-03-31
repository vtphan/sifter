rows.py parses a delimited text files into "rows".  Delimited text files can be comma-separated
or tab-separated files.


### Reading delimited text files

Read in a comma-separated text file

```
	import rows

	crime_data = read("crimeRatesByState2005.csv", ',')
```

Read a tab-separated file, skip 3 lines in the beginning of file

```
	some_data = read("data.txt", sep='\t', skip_header=3)   
```

### Getting specific column(s)

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
