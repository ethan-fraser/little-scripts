
def compress(data):
    """ Compresses data into LZW encoded form. Returns encoded data as a hyphen seperated string. """
    d = {}
    for i in data:
        if i not in d:
            d[i] = ord(i)
    code = 256
    output = ""
    w = ""
    for k in data:
        joined = w + k
        if joined in d.keys():
            w = joined
        else:
            d[joined] = code
            code += 1
            output += str(d[w]) + "-"
            w = k
    output += str(d[w])
    return output

def decompress(data):
    """ Decompresses data outputed by compress(), i.e. a string of hyphen separated numerals. """
    d = {}
    for i in data.split("-"):
        i = int(i)
        if i not in d and i < 256:
            d[i] = chr(i)
    last_code = 255
    output = ""
    entry = ""
    for code in [int(x) for x in data.split("-")]:
        prev = entry
        if code in d.keys():
            entry = d[code]
        else:
            entry = prev + prev[0]
        output += entry
        d[last_code] = prev + entry[0]
        last_code += 1
    return output


if __name__ == "__main__":
    data = input("Enter input: ").strip()

    print("\ncompressing...")
    cmp = compress(data)
    print(cmp)
    len_data = len(data)
    len_cmp = len("".join(["x" for i in range(len(cmp.split("-")))]))
    percentage = (float(len_cmp)/float(len_data))*100
    print(f"\nOriginal length: {len_data}\nCompressed length: {len_cmp} ({percentage:.2f}%)")

    print("\ndecompressing...")
    print(decompress(cmp))
