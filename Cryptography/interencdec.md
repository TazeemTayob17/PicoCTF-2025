# interencdec — picoCTF 2024 (Cryptography, Easy)

**Category:** Cryptography — `base64` → `base64` → `Caesar`  
**Points:** Easy  
**Author:** NGIRIMANA SCHADRACK

---

## Challenge description

> _Can you get the real meaning from this file?_  
> Download the file and decode it.

<img width="670" height="482" alt="Screenshot (81)" src="https://github.com/user-attachments/assets/01189113-2010-49a2-83ae-93266534a1ef" />

---

## Solution (step-by-step)

### 1. Open the provided file

Opening the file included with the challenge reveals a single Base64 string:

<img width="674" height="216" alt="Screenshot (82)" src="https://github.com/user-attachments/assets/5ed94882-b183-4d63-9729-d8ece3558f91" />

```
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVR0clgya3lNRFJvYjVTJvMmZRPT0nCg==
```

---

### 2. First Base64 decode

I pasted the string into a Base64 decoder (https://www.base64decode.org/) and decoded it — the result contained Python-like `b'...` bytes syntax:

<img width="794" height="503" alt="Screenshot (83)" src="https://github.com/user-attachments/assets/460893bc-6085-4d6d-a740-8d7a23a2a0f3" />


Decoded result (literal):

```
b'd3BqdkpBTXtqaGx6aHlfazNqeTI3YTNrX2kyMDRoa2o2fQ=='
```

**Interpretation:** the decoded output is another Base64 string, but appears wrapped in a Python `b'...'` literal. So we need to strip the `b'` and trailing `'`.

---

### 3. Strip `b'...'` wrapper and decode again

Remove the `b'` and trailing `'` to get:

```
d3BqdkpBTXtqaGx6aHlfazNqeTI3YTNrX2kyMDRoa2o2fQ==
```

Decode this second time from Base64 to get a readable string:

<img width="791" height="542" alt="Screenshot (84)" src="https://github.com/user-attachments/assets/d8dac684-be44-4086-8c3b-3643a690a81c" />


Result:

```
wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}
```

This looks extremely close to a picoCTF flag format (`picoCTF{...}`) but the prefix is garbled. That suggested a simple substitution/cipher remained — likely a Caesar/ROT shift.

---

### 4. Caesar cipher brute force / decrypt

I ran the string through a Caesar cipher brute-force (https://www.dcode.fr/caesar-cipher) and inspected the outputs. One of the shifts produced the proper flag format:

<img width="788" height="601" alt="Screenshot (85)" src="https://github.com/user-attachments/assets/5e83f464-8a56-4920-8ba3-6a1f06d74ac2" />


Decrypted (correct) flag:

```
picoCTF{caesar_d3cr9pt3d_b204adc6}
```

---

## Reproducible commands

If you want to reproduce the steps locally, here are compact commands and scripts you can run.

**1) First Base64 decode (Python):**

```bash
python3 - <<'PY'
import base64
s = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVR0clgya3lNRFJvYjVTJvMmZRPT0nCg=="
d1 = base64.b64decode(s)
print(d1)         # shows b'...'
# remove leading b' and trailing ' if present:
if d1.startswith(b"b'") and d1.endswith(b"'\n"):
    inner = d1[2:-2].decode()
else:
    # decode as bytes to string, remove possible leading b' and quotes
    inner = d1.decode().strip()
print(inner)
PY
```

**2) Second Base64 decode (Python):**

```bash
python3 - <<'PY'
import base64
inner = "d3BqdkpBTXtqaGx6aHlfazNqeTI3YTNrX2kyMDRoa2o2fQ=="
d2 = base64.b64decode(inner).decode()
print(d2)   # prints: wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}
PY
```

**3) Caesar brute force (Python) — find shift that yields `picoCTF{` prefix:**

```bash
python3 - <<'PY'
import string

def caesar(s, shift):
    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch)-97 - shift) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch)-65 - shift) % 26 + 65))
        else:
            res.append(ch)
    return ''.join(res)

s = "wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}"
for shift in range(26):
    candidate = caesar(s, shift)
    if candidate.startswith("picoCTF{") or "picoCTF" in candidate:
        print("shift:", shift, "=>", candidate)
# Expected output: shift: 3 => picoCTF{caesar_d3cr9pt3d_b204adc6}
PY
```

---

## Final Flag

```
picoCTF{caesar_d3cr9pt3d_b204adc6}
```

---

## Takeaways / Notes

- This challenge is a simple multi-layer decoding exercise: **Base64 → Base64 → Caesar**.
- Watch out for literal `b'...'` wrappers when decoding — these often come from printing raw Python `bytes` objects and must be stripped before further decoding.
- When a decoded result looks like gibberish but matches a known flag format pattern (e.g., `picoCTF{...}`), try common classical ciphers such as Caesar/ROT or simple substitutions.
- Automating a brute-force Caesar check (as shown above) is useful when the shift value is unknown.
