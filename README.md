Parsing token-separated-values (tsv) files with fields specified in headers.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

#### matreader.py:

```
	# read a tab-separate file.
	data = read("data.txt")   

	print data['D12']	# This is the list of data in column 'D12'.
	print [row['D12'] for row in data]   # same as above

	data = read("data.txt", sep=',', skip_header=5)   # Read a comma-separated file, skip 5 lines in the beginning of file

	
	# first column stores row keys, some of which can be filtered out (ignored)
	filtered_data = data.ignore('NT_167185.1.fasta','NT_167196.1.fasta')
	print filtered_data['D12']
```

#### reader.py:

```
   	data = Read("data.txt", "\t")     # Default separator is '\t', but user-specifiable
   	print data['D12']                 # Each column is a list
	print data['D50']	
   	print data['AE017198.fasta']      # Each row is also a list
```

