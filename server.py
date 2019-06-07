import socket, json
from random import randint
 
 
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
print ("Server started")
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("server received data: OK")
    data = json.loads(data.decode())
    arr = data.get("a")
    sel_sort(arr)
    print ("server processed data: OK")
    ar = json.dumps({"a": arr})
    conn.send(ar.encode())
    print("server send data: OK")

conn.close()
print ("server stoped")
