import pickle, shelve

# pickle - Pickle in Python is primarily used in serializing and
# deserializing a Python object structure. In other words, \
# it's the process of converting a Python object into a byte
# stream to store it in a file/database, maintain program
# state across sessions, or transport data over the network

# shelve - The shelve module in Python's standard library is
# a simple yet effective tool for persistent data storage
# when using a relational database solution is not required.
# The shelf object defined in this module is dictionary-like object
# which is persistently stored in a disk file.

print('Store data in file')
data1 = ['qwe','wer','ewq',['qwe1','qwe2']]
#data2 - TypeError: unhashable type: 'set'
data2 = {'qweq','ewq','wer'}
# data2 = {'qweq','ewq','wer',{'qwe','ewq'},['asd','dsa'],{'qwe':'asd'}}
data3 = {'qwe':'ewq','asd':['zxc','czx']}
data4 = ('wer','rew','asd',('sdfsdfs','sdfsdf'))
file = open('storage.dat','wb') #wb - File mode, write and binary. The same as usual but with 'B'
pickle.dump(data1, file)
pickle.dump(data2, file)
pickle.dump(data3, file)
pickle.dump(data4, file)
file.close()

print('Load stored data')
file = open('storage.dat', 'rb')
data_load1 = pickle.load(file)
data_load2 = pickle.load(file)
data_load3 = pickle.load(file)
data_load4 = pickle.load(file)
print(data_load1)
print(data_load2)
print(data_load3)
print(data_load4)