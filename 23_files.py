
file = open("./text.txt")

# print(file.read())

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.close()

with open("./text.txt") as file:
    print(file.read())



