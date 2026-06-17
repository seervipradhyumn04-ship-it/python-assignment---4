file = open("student.txt", "w")
file.write("Rahul 85\n")
file.write("Priya 90\n")
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()
