from tkinter import *
import os
import re
import time
import sys

root = Tk()
root.geometry("500x400")
root.title("Ping tool")


def pingEvent():
    print('Loading..',end='')
    network_address = networkEntry.get()
    prefix = prefixEntry.get()
    firs_address = int(firstEntry.get())
    last_address = int(lastEntry.get())
    addresses_list = []
    up_hosts = []
    global max_range
    max_range = list(range(int(firs_address), int(last_address) + 1, 1))

    if prefix == '24':
        if checkState.get() == 1:
            firs_address = 1
            last_address = 255
        max_range = list(range(firs_address, last_address + 1, 1))
        for i in max_range:
            address = re.findall(r'[0-9]+[.][0-9]+[.][0-9]+', network_address)
            addresses_list.append(address[0] + '.' + str(i))

    elif prefix == '16':
        if checkState.get() == 1:
            firs_address = 1
            last_address = 255
        max_range = list(range(int(firs_address), int(last_address) + 1, 1))
        for i in max_range:
            address = re.findall(r'^[0-9]+[.][0-9]+', network_address)
            addresses_list.append(address[0] + '.' + str(i) + '.0')
        for i in max_range:
            address = re.findall(r'[0-9]+[.][0-9]+[.][0-9]+', network_address)
            addresses_list.append(address[0] + '.' + str(i))

    elif prefix == '8':
        if checkState.get() == 1:
            firs_address = 1
            last_address = 255
        max_range = list(range(int(firs_address), int(last_address) + 1, 1))
        for i in max_range:
            address = re.findall(r'^[0-9]+', network_address)
            addresses_list.append(address[0] + '.' + str(i) + '.0' + '.0')
        for i in max_range:
            address = re.findall(r'^[0-9]+[.][0-9]+', network_address)
            addresses_list.append(address[0] + '.' + str(i) + '.0')
        for i in max_range:
            address = re.findall(r'[0-9]+[.][0-9]+[.][0-9]+', network_address)
            addresses_list.append(address[0] + '.' + str(i))

    # pinging stage.
    for ip in addresses_list:
        result = os.popen(f"ping {ip} -n 2").read()
        if "Request timed out" in result:
            print('.', end='')
            filetxt = open("output.txt", "a")
            filetxt.write('IP: ' + ip + '\t' + ' State: down.' + '\n')
            filetxt.close()
        elif "Destination host unreachable" in result:
            print('..', end='')
            filetxt = open("output.txt", "a")
            filetxt.write('IP: ' + ip + '\t' + ' State: down.' + '\n')
            filetxt.close()
        else:
            print('...', end='')
            filetxt = open("output.txt", "a")
            filetxt.write('IP: ' + ip + '\t' + ' State: up.' + '\n')
            filetxt.close()
            up_hosts.append(ip)
    print('')
    with open("output.txt") as file:
        output = file.read()
    print(output)
    with open("output.txt", "w"):  # Clearing txt content.
        pass
    print('Hosts that are reachable ', end='')
    print(up_hosts)


networkLabel = Label(root, text='Network address').place(x=30, y=50)
firstAdLabel = Label(root, text='First address').place(x=30, y=100)
lastAdLabel = Label(root, text='Last address').place(x=30, y=135)

pingButton = Button(root, text='Ping', command=pingEvent).place(x=30, y=170)
noteLabel = Label(root, text='Note: After issuing a ping please wait till its done.').place(x=30, y=210)
resultLabel = Label(root, text='The result is printed in the CLI').place(x=30, y=240)
prefixLabel = Label(root, text='Prefix').place(x=260, y=50)

checkState = IntVar()
checkBox = Checkbutton(root, text='Ping all hosts on this subnet', variable=checkState)
checkBox.place(x=190, y=115)

networkEntry = Entry(root, width=15)
networkEntry.place(x=130, y=50)
networkEntry.insert(0, "192.168.100.0")

prefixEntry = Entry(root, width=5)
prefixEntry.place(x=300, y=50)
prefixEntry.insert(0, "24")

firstEntry = Entry(root, width=5)
firstEntry.place(x=110, y=100)
firstEntry.insert(0, "1")

lastEntry = Entry(root, width=5)
lastEntry.place(x=110, y=135)
lastEntry.insert(0, "254")
# 192.168.0.0 \16
root.mainloop()
