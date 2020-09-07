import time, threading

from werkzeug.local import Local
'''
class A:
    b=1
'''
my_obj = Local()
my_obj.b =1

def worker():
    my_obj.b =2
    print('in new thread b is :' + str(my_obj.b))

new_t = threading.Thread(target=worker, name='michael thread')
new_t.start()
time.sleep(2)

print('in main thread b is :' + str(my_obj.b))