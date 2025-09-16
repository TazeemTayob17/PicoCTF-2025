from pwn import *

def conn():
    r = remote("titan.picoctf.net", 63057)
    r.recvuntil(b"E --> encrypt D --> decrypt.")
    return r

c_password = 2575135950983117315234568522857995277662113128076071837763492069763989760018604733813265929772245292223046288098298720343542517375538185662305577375746934
r = conn()

def encrypt(plain):
    r.sendline(b"E")
    r.recvuntil(b"enter text to encrypt (encoded length must be less than keysize): ")
    r.sendline(plain)
    print(r.recvuntil(b"ciphertext (m ^ e mod n) "))

    return r.recvline().strip().decode()

def decrypt(cipher):
    r.sendline(b"D")
    r.recvuntil(b"Enter text to decrypt: ")
    r.sendline(cipher)
    print(r.recvuntil(b"decrypted ciphertext as hex (c ^ d mod n): "))

    return r.recvline().strip().decode()

c_two = encrypt(b"\x02")
c_two = int(c_two)

print(c_two*c_password)

# encryption of plain t: C = t^e mod n
# decrypting the ciphertext C: C^d mod n = t^e^d mod n = t mod n

# if C_2 is the ciphertext of \x02, and C_password is the ciphertext of the password t
# then (C_2 * C_password)^d mod n = (2^e*t^e)^d mod n = (2^e^d)(t^e^d) mod n = 2t mod n

attack = decrypt(str(c_two*c_password).encode()).encode()
attack = int(attack, 16)
attack = attack // 2

print(attack.to_bytes((attack.bit_length() + 7) // 8, "big"))

# password is 60f50
# use openssl to decrypt the secret.enc file:
# openssl enc -aes-256-cbc -d -in secret.enc