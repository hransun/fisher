import threading,time

def worker():
    print("worker michael")
    t = threading.current_thread()
    time.sleep(3)
    print(t.getName())



new_t = threading.Thread(target=worker,name ='michael thread')
new_t.start()

print("main print")
t = threading.current_thread()
print(t.getName())