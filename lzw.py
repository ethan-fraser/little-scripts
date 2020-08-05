
data = input("Enter input: ").strip().lower()

# init dictionary 
d = {}
for i in data:
    if i not in d.keys():
        d[i] = ord(i)
code = 256

output = ""

w = data[0]
for i, c in enumerate(data):
    if i == 0:
        continue
    if (w + c) in d.keys():
        w += c
    else:
        output += str(d[w]) + "-"
    d[w+c] = code
    code += 1
    w = c
output += str(d[w])
print(output)

# decode and print
d2 = {y:x for x,y in d.items()}
output2 = ""
for key in output.split("-"):
    output2 += d2[int(key)] + "-"
print(output2)

print(d)
