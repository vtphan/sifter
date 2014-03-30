'''
Author: Vinhthuy Phan
Deprecated: use matreader.py instead

Parsing token-separated-values (tsv) files.
Token is a tab by default, but configurable to others, e.g. comma or semicolon.

Input:
   + First row must be a header specifying all fields.
   + Subsequent rows have tab-delimited fields, consistent with the header.

Example:
   import tsv
   rows = tsv.Read("customer.txt", '\t')
   for r in rows:
      print r['FIRSTNAME'], r['LASTNAME'], r['COMPANY']
'''

#-----------------------------------------------------------------------------
class Row:
   def __init__(self, header, sep):
      self.sep = sep
      self.fields = {}
      h = header.split(sep)
      self.columns = len(h)
      for idx, key in enumerate(h):
         if key not in self.fields:
            self.fields[key] = idx
      self.r = None

   def set(self, line):
      self.r = line.split(self.sep)
      if len(self.r) != self.columns:
         print "Error: column mismatch (%d != %d): %s" % (self.columns, len(self.r), self.r)

   def __getitem__(self, key):
      if self.r:
         v = self.r[self.fields[key]]
         try:
            v = float(v)
         except:
            pass
         return v

      return None


#-----------------------------------------------------------------------------
class Read:
   ''' Default setting assumes the file is tab-delimited '''
   def __init__(self, filename, token='\t'):
      with open(filename, 'rU') as f:
         self.lines = f.readlines()
      h = self.lines.pop(0).strip()
      while not h:
         h = self.lines.pop(0).strip()
      self.row = Row(h, token)

   def __contains__(self, key):
      return key in self.row.fields

   def __len__(self):
      return len(self.lines)

   def __iter__(self):
      self.i = -1
      return self

   def next(self):
      if self.i < len(self.lines)-1:
         self.i += 1
         line = self.lines[self.i].strip("\n")
         if line and line[0]!='#':  # ignore empty lines and commented lines (start with #)
            self.row.set(line)
            return self.row
         else:
            return self.next()
      else:
         raise StopIteration

#-----------------------------------------------------------------------------

if __name__ == '__main__':
   rows = Read("complexity.txt")
   print [r['D12'] for r in rows]

