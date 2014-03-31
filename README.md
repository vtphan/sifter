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

All values in column "state"
```
	states = crime_data['state']
```
