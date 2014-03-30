'''
Author: Vinhthuy Phan, 2014
'''

class Read:
   def __init__(self, filename, sep="\t"):
      with open(filename, 'rU') as f:
         # remove all empty and comments (starting with #) in data
         self.lines = [ line.rstrip() for line in f.readlines() if line.strip() and (line.strip()[0] != '#')]

      self.col_keys = []
      # self.col_data = {}
      self.row_keys = []
      self.row_data = {}
      self.col_num = 0

      if self.lines:
         # Process first line
         self.col_keys = [ k.strip() for k in self.lines.pop(0).split(sep) ]
         self.cols = len(self.col_keys)

         self.row_keys = [ self.col_keys[0] ]
         self.row_data = { self.row_keys[0] : self.col_keys[1:] }

         # self.col_data = { k : [] for k in self.col_keys }

         # Process lines starting from the second line
         for line in self.lines:
            values = [ v.strip() for v in line.split(sep) ]

            if len(values) != self.col_num:
               raise Exception("Missing values", len(values), self.col_num, line)

            for i,v in enumerate(values):
               if not v:
                  raise Exception("Mising value", i, values)

               try:
                  v = float(v)
               except:
                  pass

               # self.col_data[ self.col_keys[i] ].append( v )

               if i == 0:
                  self.row_keys.append(v)
                  self.row_data[v] = []
               else:
                  self.row_data[ self.row_keys[-1] ].append(v)


   def __contains__(self, key):
      return key in self.col_data or key in self.row_data

   def __getitem__(self, key):
      if key in self.col_data:
         return self.col_data[key]
      if key in self.row_data:
         return self.row_data[key]
      raise Exception("Unknown key", key)

   def __len__(self):
      return len(self.lines)



#-----------------------------------------------------------------------------

if __name__ == '__main__':
   import sys
   data = Read(sys.argv[1])
   print data[sys.argv[2]]
