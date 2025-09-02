
**Challenge Title: ** Inspect HTML
**Category:** Web Exploitation     

---

## 📝 Challenge Description
We are given a simple website and need to retrieve the hidden flag.

<img width="673" height="589" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/39a43f39-80bd-4bea-9fd0-c00029b82bd7" />

## Challenge Website

<img width="1366" height="653" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/b475ada8-0b2d-459d-86fe-d6d510e26750" />


---

## 🔍 Enumeration & Initial Thoughts
- Opened the website in the browser.  
- The page looked static with no obvious interactive elements.  
- Suspected the flag might be hidden in the HTML source code.  

---

## ⚙️ Exploitation
1. Right-clicked on the page and selected **"View Page Source"** (or used DevTools).  
2. Searched for keywords like `flag` or `picoCTF`.  
3. Found the flag embedded in a hidden comment within the HTML.

<img width="1366" height="674" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/b2c6b151-f822-434f-9e22-48051279cfa4" />


---

## 🏁 Flag
picoCTF{1n5p3t0r_0f_h7ml_fd5d57bd}


---

## 📚 Key Takeaways
- Always check HTML source for hidden data (comments, scripts, unused tags).  
- Many beginner CTF challenges test whether you know how to inspect client-side code.  
