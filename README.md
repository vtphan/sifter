Parsing token-separated-values (tsv) files with fields specified in headers.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

Input:
   + First row must be a header specifying all fields.
   + Subsequent rows have tab-delimited fields, consistent with the header.

#### Example:

```
	import reader
   	data = Read("data.txt", "\t")	# default separator is '\t', but user-specifiable
   	print data['D12']  		# each column is a list
	print data['D50']	
   	print data['AE017198.fasta']	# each row is also a list
```
