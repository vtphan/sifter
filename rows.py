'''
Author: Vinhthuy Phan, 2014
'''
import csv

#-----------------------------------------------------------------------------
class Row(object):
   def __init__(self, keys, values):
      if len(keys) != len(values):
         raise Exception("Discrepancies in keys and values:\n%s\n%s\n" % (keys, values))

      self.data = {}
      for i, k in enumerate(keys):
         try:
            self.data[k] = float(values[i])
         except:
            self.data[k] = values[i]

   def __getitem__(self, key):
      if key in self.data:
         return self.data[key]
      return None


#-----------------------------------------------------------------------------
class Rows(object):
   def __init__(self, header, rows):
      self.rows = [ Row(header, r) for r in rows ]
      self.keys = [ r[0] for r in rows ]
      self.header = header

   def __len__(self):
      return len(self.rows)

   ''' self[key] returns column "key" '''
   def __getitem__(self, key):
      return [r[key] for r in self]

   ''' enumerate through self.rows '''
   def __iter__(self):
      self.i = -1
      return self

   def next(self):
      if self.i < len(self.rows)-1:
         self.i += 1
         return self.rows[self.i]
      else:
         raise StopIteration

   ''' return a dict keyed by values of "col" '''
   def cluster(self, col):
      if col not in self.header:
         return None
      c = {}
      for r in self:
         key = r[col]
         if key not in c:
            c[key] = Rows(self.header, [])
            c[key].keys = self.keys
         c[key].rows.append(r)
      return c

   def ignore(self, *val):
      try:
         idx = set([ self.keys.index(v) for v in val ])
         n = Rows(self.header, [])
         n.rows = [ self.rows[i] for i in range(len(self.rows)) if i not in idx ]
         n.keys = [ self.keys[i] for i in range(len(self.keys)) if i not in idx ]
         n.header = self.header
         return n
      except:
         return self



#-----------------------------------------------------------------------------

def read(filename, sep='\t', skip_header=0):
   ''' Default setting assumes the file is tab-delimited '''
   rows = []
   with open(filename, 'rU') as f:
      reader = csv.reader(f, delimiter=sep)
      for row in reader:
         if skip_header > 0:
            skip_header -= 1
         elif row and row[0][0] != '#':
            rows.append(row)
   return Rows(rows.pop(0), rows)

#-----------------------------------------------------------------------------

if __name__ == '__main__':
   data = read("data.txt")
   print data['D12']
   print data.ignore('NT_167185.1.fasta','NT_167196.1.fasta')['D12']
   # print data['ID']
