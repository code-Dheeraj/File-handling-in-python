# reading from the file 
f = open("temp1.txt",'r')
s = f.read()
print(s)
f.close()

# reading upto n character 
f = open("temp1.txt",'r')
s = f.read(20)
print(s)
f.close()

# readline() -> to read line by line
f = open("temp1.txt",'r')
s= f.readline()
t= f.readline()
u= f.readline()
print(s,end="")
print(t)  # if u dont use end="" you will get an extra empty line because of '\n' character at the end of readline()
print(u)
f.close()


reading entire using readline

f = open("temp1.txt",'r')
while True:
    data = f.readline()
    if(data==''):
        break
    else:
        print(data,end='')
        
f.close()

