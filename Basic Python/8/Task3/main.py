import glob

files = []
for file in glob.glob("*.txt"):
    if file != 'exit.txt':
        files.append(file)

strings = []
for name in files:
    with open(name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        count = len(lines)
        strings.append([name, count, ''.join(lines)])

strings.sort(key=lambda x: x[1])
with open('exit.txt', 'w', encoding='utf-8') as file:
    for value in strings:
        file.write(value[0]+'\n')
        file.write(str(value[1])+'\n')
        file.write(value[2]+'\n')