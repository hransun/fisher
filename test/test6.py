import time, threading

from werkzeug.local import Local, LocalStack

'''
class A:
    b=1
'''
my_stack = LocalStack()
my_stack.push(1)

print('in main thread top is :' + str(my_stack.top))

def worker():

    print('in new thread top is :' + str(my_stack.top))
    my_stack.push(2)
    print('in new thread top is :' + str(my_stack.top))


new_t = threading.Thread(target=worker, name='michael thread')
new_t.start()
time.sleep(2)

print('in main thread b is :' + str(my_stack.top))