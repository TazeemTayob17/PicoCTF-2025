# WebDecode – picoCTF

**Category:** Web Exploitation  
**Points:** *[fill in if you know]*  
**Date Completed:** 2025-09-02  

---

## 📝 Challenge Description
We are given a website with three sections (Home, Contact, About). The goal is to inspect the site and retrieve the hidden flag.

---

## 🔍 Enumeration & Initial Thoughts
- Used **browser Developer Tools** to inspect the source of each page.  
- The **Home** and **Contact** pages didn’t contain anything useful.  
- On the **About** page, noticed a variable named `notify_true` with encoded information.  

---

## ⚙️ Exploitation
1. Copied the contents of the `notify_true` variable.  
2. Opened **Burp Suite Decoder**.  
3. Decoded the string to reveal the flag.  

---

## 🏁 Flag
picoCTF{web_succ3ssfully_d3c0ded_f6f6b78a}

yaml
Copy code

---

## 📚 Key Takeaways
- Always inspect page source and JavaScript variables when analyzing web challenges.  
- Browser DevTools are powerful for quick reconnaissance.  
- Burp Suite Decoder is a handy tool for testing different encodings.  
