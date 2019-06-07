import socket, json

sock = socket.socket()
sock.connect(('localhost', 9090))
wl = open('wl.txt', 'r')
arr = wl.read().split(' ')
print ("read data from file: OK")
wl.close()
arri = []
for i in range(len(arr)):
    t = int(arr[i])
    arri.append(t)
ar = json.dumps({"a": arri})
sock.send(ar.encode())
print ("send data: OK")

data = sock.recv(1024)
data = json.loads(data.decode())
print ("back data: OK")
barr = data.get("a")
wl1 = open('wl1.txt', 'w')
for i in barr:
    wl1.write("%d " % i)
wl1.close()
print ("write data: OK")
sock.close()

print ("client stoped")
