#Program to decode picoCTF New caesar challenge given encrypted text and encryption method
import string

# constants
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


# decode function
def b16_decode(cipher):
    dec = ""
    # loop through the cipher 2 characters at a time
    for c in range(0, len(cipher), 2):
        # turn the two characters into one binary string
        b = ""
        b += "{0:04b}".format(ALPHABET.index(cipher[c]))
        b += "{0:04b}".format(ALPHABET.index(cipher[c + 1]))
        # turn the binary string to a character and add
        dec += chr(int(b, 2))

    # return
    return dec


# unshift the text
def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


# encrypted flag
enc = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"

# loop through all possible keys
for key in ALPHABET:
    # initialize string
    s = ""

    # loop through the encrypted text
    for i, c in enumerate(enc):
        # unshift it based on key
        s += unshift(c, key[i % len(key)])

    # decode
    s = b16_decode(s)

    # print key
    print(s)

    #Take the most realistic of the outputs
    #Hence, flag is picoCTF{et_tu?_5723f4e71a0736d3b1d19dde4279ac03}