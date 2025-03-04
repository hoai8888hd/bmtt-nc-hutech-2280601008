print("nhap van ban: ")
vanban = []
while True:
    line = input()
    if line.lower() == "done":
        break
    vanban.append(line)
print("cac dong cua van ban: ")
for line in vanban:
    print(line.upper())