# WebDecode – picoCTF

**Category:** Web Exploitation    
**Date Completed:** 2025-09-02  

---

## 📝 Challenge Description
We are given a website with three sections (Home, Contact, About). The goal is to inspect the site and retrieve the hidden flag.

<img width="666" height="574" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/95546c69-7416-4b92-940e-732624950254" />

## Challenge Website

<img width="1351" height="674" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/d32e0e88-9bd7-4196-b79b-06a7bef2e22a" />

---

## 🔍 Enumeration & Initial Thoughts
- Used **browser Developer Tools** to inspect the source of each page.  
- The **Home** and **Contact** pages didn’t contain anything useful.  
- On the **About** page, noticed a variable named `notify_true` with encoded information.

<img width="1366" height="674" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/e22e5aad-989b-4642-b5d3-76264d46aa4b" />


---

## ⚙️ Exploitation
1. Copied the contents of the `notify_true` variable.  
2. Opened **Burp Suite Decoder**.  
3. Decoded the string to reveal the flag.  

<img width="1366" height="706" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/346fb4d2-f499-416a-8946-c7ea8d6b6ba8" />


---

## 🏁 Flag
picoCTF{web_succ3ssfully_d3c0ded_f6f6b78a}

---

## 📚 Key Takeaways
- Always inspect page source and variables when analyzing web challenges.  
- Browser DevTools are powerful for quick reconnaissance.  
- Burp Suite Decoder is a handy tool for testing different encodings.  
