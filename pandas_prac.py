import pandas as pd
# df = pd.read_csv('titanic.csv')
# print(df.info())
my_series = pd.Series([10, 20, 30, 40, 50])
print(my_series)
print(my_series[2])

# changing indexing style
l = [1, 3, 5]
my_series = pd.Series(l, index=['X', 'Y', 'Z'])
print(my_series)

# dictionary to series
dit = {'Name' : 90, 'Place' : 78, 'Animal' : 45, 'Thing' : 100}
my_series = pd.Series(dit)
print(my_series)

# dictionary functions
a = dit.pop('Name')
print(a, dit)
dit.update({'Name' : 56})
print(dit)
dit.clear()
print(dit)
dit.update({'Name' : 56, 'Place' : 78, 'Animal' : 45, 'Thing' : 100})
print(dit.keys())
print(dit.values())
print(dit.get('Place'))
b = dit.popitem()
print(b, dit)
dit2 = dit.copy()
print(dit, dit2)

# data frame creation
# python dictionary
dit = {'Name': ['John', 'Elena', 'Jeremy'],
       'Age': [123, 17, 16],
       'Place': ['Gilbert house', 'Mystic Falls', 'Mystic Falls']}
df = pd.DataFrame(dit)
print(df)

# python list
li = [['John',  123,  'Gilbert house'],
      ['Elena',   17,   'Mystic Falls'],
      ['Jeremy',   16,   'Mystic Falls']]
df = pd.DataFrame(li, columns=['Name', 'Age', 'Place'])
print(df)

# empty dataframe
df1 = pd.DataFrame()
print(df1)

# indexing
df.set_index('Name', inplace=True)
print(df)

# range index
df = pd.DataFrame(dit, index=pd.RangeIndex(0, 3, name='Index'))
print(df)

# rename and reset the index
df.rename(index={0: 'A', 1: 'B', 2: 'C'}, inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)

# accessing the row
row = df.iloc[1]
print(row)

# index jaano
print(df.index)
print(df.index.values)

# array pandas
li = [1, 3, 2, 6]
arr = pd.array(li)
print(arr)

arr = pd.array([4.5, 6.7, 2.3], dtype='float')
print(arr)
