def first(st):
    ar = st.split(' ')
    for i in range(len(ar)):
        ar[i]=ar[i][::-1]
    print(' '.join(ar),end='')
def second(st):
    ar = st.split(' ')
    for i in range(len(ar)):
        ar[i]=ar[i][::-1]
    print(' '.join(ar))
if __name__ =="__main__":
    import threading 
    import os
    
    # creating thread
    para = str(input())
    mid = len(para)//2
    import time
    t=time.time()
    t1 = threading.Thread(target=first, args=(para[:mid],))
    t2 = threading.Thread(target=second, args=(para[mid:],))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    t3=time.time()
    print((t3-t )*1000)
