TSV: parser of token-separated-value files with headers
=======================================================

Parsing token-separated-values (tsv) files.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

Input:
   + First row must be a header specifying all fields.
   + Subsequent rows have tab-delimited fields, consistent with the header.

.. code-block:: pycon
	rows = TSV("customer.txt", '\t')
	for r in rows:
		print r['FIRSTNAME'], r['LASTNAME'], r['COMPANY']

