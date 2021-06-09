from tkinter import *
import socket

root = Tk()
root.geometry("500x250")
root.title("TCP ports tool")

socket.setdefaulttimeout(.5)


def checkAllEvent():
    ip = ipEntry.get()
    open_ports = []
    start_port = startEntry.get()
    end_port = endEntry.get()
    for i in list(range(int(start_port), int(end_port)+1, 1)):
        DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (ip@, port#).
        result = DEVICE_SOCKET.connect_ex((ip, i))
        if result == 0:
            print('Port ' + str(i) + ' is open.')
            open_ports.append(str(i))
            DEVICE_SOCKET.close()
        else:
            print('Port ' + str(i) + ' is close.')
            DEVICE_SOCKET.close()
    print('The open ports are: ', end='')
    print(open_ports)


def checkEvent():
    ip = ipEntry.get()
    port = int(portEntry.get())
    DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # (ip@, port#).
    result = DEVICE_SOCKET.connect_ex((ip,port))

    if result == 0:
       print('Port ' + str(port) + ' is open.')
       DEVICE_SOCKET.close()
    else:
       print('Port ' + str(port) + ' is close.')
       DEVICE_SOCKET.close()


ipLabel = Label(root, text='Target address').place(x=30, y=50)
portLabel = Label(root, text='Port number').place(x=30, y=100)

checkButton = Button(root, text='Check single port', command=checkEvent).place(x=40, y=130)
checkAllButton = Button(root, text='Check multiple ports', command=checkAllEvent).place(x=250, y=130)
noteLabel = Label(root, text='Note: the result is printed on the CLI.').place(x=30, y=210)
rangeLabel = Label(root, text='Range').place(x=280, y=70)
startLabel = Label(root, text='Start').place(x=220, y=100)
endLabel = Label(root, text='End').place(x=300, y=100)

ipEntry = Entry(root, width=15)
ipEntry.place(x=130, y=50)
ipEntry.insert(0, "192.168.100.1")

portEntry = Entry(root, width=5)
portEntry.place(x=110, y=100)
portEntry.insert(0, "80")

startEntry = Entry(root, width=5)
startEntry.place(x=250, y=100)
startEntry.insert(0, "1")

endEntry = Entry(root, width=5)
endEntry.place(x=330, y=100)
endEntry.insert(0,"80")

root.mainloop()