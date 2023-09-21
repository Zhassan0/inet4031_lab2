#!/usr/bin/env python3
f = open("fileprocessor.input")
with f as file:
    # Create an empty list to store the lines
    lines = []
    for line in file:
        line=line.strip()
        if '#' not in line:
            lines.append(line)
print(lines)
userlist=[]
for x in lines:
    word=x.split(":")
    userlist.append(word)
print(userlist)
#start printing
print("Printing out User Data:")
for x in userlist:
    print("the user ", *x[0],"has a password of ",*x[1],"and has userid",*x[2]," and groupid",*x[3])
print("End of User Data")
