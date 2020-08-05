def encode(bitstring: str, runlen: int) -> str:
    """convert bitstring to bitwise run-length encoded equivalent"""
    encoded_bitstring = ""
    format_str = '0' + str(runlen) + 'b'
    num_zeroes = 0
    max_val = (2**runlen) - 1
    for i in range(len(bitstring)):
        if bitstring[i] == "1" or i == len(bitstring)-1:
            # for if the last bit is 0
            if bitstring[i] == "0":
                num_zeroes += 1
            # encode zeroes to bits
            if num_zeroes < max_val:
                encoded_bitstring += format(num_zeroes, format_str) + " "
            else:
                while num_zeroes >= max_val:
                    num_zeroes -= max_val
                    encoded_bitstring += "1"*runlen + " "
                encoded_bitstring += format(num_zeroes, format_str) + " "
            # done encoding
            num_zeroes = 0
        else:
            num_zeroes += 1

    if bitstring[len(bitstring)-1] == "1":
        encoded_bitstring += "0"*runlen + " "

    # since the last character will always be " "
    return encoded_bitstring[:len(encoded_bitstring)-1]

def decode(bitstring: str) -> str:
    """
        convert compressed bitstring back to original string.
        assumes `bitstring` is space separated into its run-lengths (e.g. 4 bit blocks for 4-bit run length
        encoding - "0101 1010")
    """
    decoded_bitstring = ""
    blocks = bitstring.split(" ")
    runlen = len(blocks[0])
    max_val = 2**runlen - 1
    for i in range(len(blocks)-1):
        num_zeroes = int(blocks[i], 2)
        decoded_bitstring += "0"*num_zeroes
        if num_zeroes < max_val:
            decoded_bitstring += "1"
    return decoded_bitstring

def perc(cmp: str, orig: str) -> float:
    """helper for calculating percentage of compressed data compared to original"""
    # get rid of space sepatators
    cmp = "".join(cmp.split(" "))
    orig = "".join(orig.split(" "))
    # calculate percentage
    return (float(len(cmp))/float(len(orig))) * 100

if __name__ == "__main__":
    data = "1" + ("0"*36) + "1" + ("0"*23) + "111" + ("0"*48) + "1" + ("0"*31) + "1" + ("0"*3)
    cmp = encode(data, 5)
    cmp_len = len("".join(cmp.split(" ")))
    data2 = "0"*14 + "1" + "0"*9 + "11" + "0"*20 + "1" + "0"*30 + "11" + "0"*11
    cmp2 = encode(data2, 4)
    cmp2_len = len("".join(cmp2.split(" ")))
    print(cmp)
    print(f"original: {len(data)}, cmp: {cmp_len}, {perc(cmp, data):.2f}%\n")
    print(cmp2)
    print(f"original: {len(data2)}, cmp: {cmp2_len}, {perc(cmp2, data2):.2f}%\n")

    print(decode(cmp2))

