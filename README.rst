Parsing token-separated-values (tsv) files with fields specified in headers.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

Input:
   + First row must be a header specifying all fields.
   + Subsequent rows have tab-delimited fields, consistent with the header.


.. code-block:: python
	import reader
   	data = Read("customer.txt", "\t")
   	print data.keys
   	print data['COMPANY']
	print data['FIRSTNAME']
   	print data['AGE']

