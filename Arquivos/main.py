file = open('db.txt', 'r+')
print(file.readline())
file.seek(0)
print(file.read().split("\n"))
for linha in file.readline():
    print(linha)

# file.write("Teste")
# file.seek(20,0)
# file.truncate()
# print(file.tell())
# print(file.read())
file.close()