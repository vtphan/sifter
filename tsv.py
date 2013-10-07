'''
Parsing token-separated-values (tsv) files.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

Input:
   + First row must be a header specifying all fields.
   + Subsequent rows have tab-delimited fields, consistent with the header.

Example:
   rows = TSV("Customers2.txt", '\t')
   for r in rows:
      print r['FIRSTNAME'], r['LASTNAME'], r['COMPANY']
'''

#-----------------------------------------------------------------------------
class Row:
   def __init__(self, header, token):
      self.token = token
      self.fields = {}
      for idx, t in enumerate(header.strip().split(token)):
         if t not in self.fields:
            self.fields[t] = idx
      self.r = None

   def set(self, line):
      self.r = line.strip("\n").split(self.token)
      if len(self.r) != len(self.fields):
         raise Exception("Header and row have different lengths.")

   def __getitem__(self, key):
      return self.r[self.fields[key]] if self.r else None

#-----------------------------------------------------------------------------
class TSV:
   ''' Default setting assumes the file is tab-delimited '''
   def __init__(self, filename, token='\t'):
      self.lines = open(filename, 'rU').readlines()
      self.reset()
      self.row = Row(self.lines.pop(0), token)

   def reset(self):
      self.i = -1

   def __iter__(self):
      return self

   def next(self):
      if self.i < len(self.lines)-1:
         self.i += 1
         self.row.set(self.lines[self.i])
         return self.row
      else:
         raise StopIteration

#-----------------------------------------------------------------------------

if __name__ == '__main__':
   rows = TSV("Customers2.txt")
   for r in rows:
      print r['FIRSTNAME'], r['LASTNAME'], r['COMPANY']

