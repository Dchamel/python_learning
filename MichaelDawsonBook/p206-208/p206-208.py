import shelve
from time import perf_counter
t1 = perf_counter()
s = shelve.open('storage')
# s['q'] = ['qwe','qwe1','qwe2']
# s['w'] = ['wer','wer1','wer2']
# s['e'] = ['ert','ert1','ert2']
# s.sync()
print(s['q'])
t2 = perf_counter()
print(f'{t2-t1:.10f} sec')
