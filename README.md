Parsing token-separated-values (tsv) files with fields specified in headers.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

#### matreader.py:

```
	rows = read("complexity.txt")
	print [r['D12'] for r in rows]
	print [r['D12'] for r in rows.ignore('NT_167185.1.fasta', 'NT_167196.1.fasta', 'NT_077528.2.fasta')]
```

#### reader.py:

```
   	data = Read("data.txt", "\t")     # Default separator is '\t', but user-specifiable
   	print data['D12']                 # Each column is a list
	print data['D50']	
   	print data['AE017198.fasta']      # Each row is also a list
```

