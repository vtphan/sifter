Parsing token-separated-values (tsv) files with fields specified in headers.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

#### matreader.py:

```
	data = read("data.txt")                           # Read a tab-separate file.
	print data['D12']                                 # This is the list of data in column 'D12'.

	data = read("data.txt", sep=',', skip_header=5)   # Read a comma-separated file, skip 5 lines in the beginning of file


	# Filtering 	
	filtered_data = data.ignore('NT_167185.1.fasta','NT_167196.1.fasta')   # Filtered out some rows
	print filtered_data['D12']
	
	# More general ways of filter
	# All values in column D12
	data = [r['D12'] for r in data]

	# Values in column D12 for rows with specific values in ID
	data = [r['D12'] for r in data if r['ID'] in ('NT_167185.1.fasta','NT_167196.1.fasta')]

	# Values in column D12 for rows for which values in column D25 > 0.95
	data = [r['D12'] for r in data if r['D25'] > 0.95]
```

#### reader.py:

```
   	data = Read("data.txt", "\t")     # Default separator is '\t', but user-specifiable
   	print data['D12']                 # Each column is a list
	print data['D50']	
   	print data['AE017198.fasta']      # Each row is also a list
```

