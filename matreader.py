'''
Author: Vinhthuy Phan, 2014
'''

#-----------------------------------------------------------------------------
class Row:
   def __init__(self, keys, values, sep):
      ks = [ i.strip() for i in keys.split(sep) ]
      vs = [ i.strip() for i in values.split(sep) ]
      self.data = {}
      for i, k in enumerate(ks):
         try:
            self.data[k] = float(vs[i])
         except:
            self.data[k] = vs[i]

   def __getitem__(self, key):
      if key in self.data:
         return self.data[key]
      return None


#-----------------------------------------------------------------------------
class Rows:
   def __init__(self, header, lines, sep):
      self.rows = [ Row(header, line, sep) for line in lines ]
      self.keys = [ line.split(sep)[0].strip() for line in lines ]
      self.sep = sep
      self.header = header

   def __len__(self):
      return len(self.rows)

   def __iter__(self):
      self.i = -1
      return self

   def next(self):
      if self.i < len(self.rows)-1:
         self.i += 1
         return self.rows[self.i]
      else:
         raise StopIteration

   def ignore(self, *val):
      try:
         idx = set([ self.keys.index(v) for v in val ])
         n = Rows(self.header, [], self.sep)
         n.rows = [ self.rows[i] for i in range(len(self.rows)) if i not in idx ]
         n.keys = [ self.keys[i] for i in range(len(self.keys)) if i not in idx ]
         return n
      except:
         return self

   def __getitem__(self, key):
      return [r[key] for r in self]


#-----------------------------------------------------------------------------

def read(filename, sep='\t', skip_header=0):
   ''' Default setting assumes the file is tab-delimited '''
   with open(filename, 'rU') as f:
      lines = [ line.strip() for line in f.readlines() ]
      lines = lines[skip_header : ]
      # remove empty lines and comments (lines starting with #) in data
      lines = [ line for line in lines if line and line[0]!='#']

   header = lines.pop(0).strip()
   return Rows(header, lines, sep)

#-----------------------------------------------------------------------------

if __name__ == '__main__':
   data = read("data.txt")
   print data['D12']
   print data.ignore('NT_167185.1.fasta','NT_167196.1.fasta')['D12']
   # print data['ID']
