Parsing token-separated-values (tsv) files with fields specified in headers.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

#### matreader.py:

```
	# read a delimited text file separated by "sep", and ignore number of lines in header.
	data = read("data.txt", sep='\t', skip_header=0)   

	# iterate through rows
	print [row['D12'] for row in data]
	print [row['D12'] for ror in data.ignore('NT_167185.1.fasta', 'NT_167196.1.fasta')]
	
	# same as above, but more concise
	print data['D12']
	print data.ignore('NT_167185.1.fasta','NT_167196.1.fasta')['D12']
```

#### reader.py:

```
   	data = Read("data.txt", "\t")     # Default separator is '\t', but user-specifiable
   	print data['D12']                 # Each column is a list
	print data['D50']	
   	print data['AE017198.fasta']      # Each row is also a list
```

