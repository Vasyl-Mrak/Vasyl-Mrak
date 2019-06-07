from random import randint
N = 100
arr = []
for i in range(N):
    arr.append(randint(1, 999))
print (range(len(arr)))
wl = open('wl.txt', 'w')
for i in arr:
    wl.write("%d " % i)
wl.close()
print("List created")
