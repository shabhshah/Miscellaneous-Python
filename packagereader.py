#Rishabh Shah
#2016
#Creating a file to batch install packages on Ubuntu

fh = open("package.txt","a")
fh.write("sudo apt-get install ")

for line in open("packages.txt"):
    line = line.strip()
    parts = line.split()

    importantPart = parts[0]

    fh.write(importantPart + " ")

fh.close()