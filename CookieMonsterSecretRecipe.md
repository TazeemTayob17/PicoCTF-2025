# Cookie Monster Secret Recipe

**Category:** Web Exploitation  

---

## 📝 Challenge Description
We are given a website and need to retrieve the hidden flag.

<img width="671" height="588" alt="Screenshot (68)" src="https://github.com/user-attachments/assets/f489cfb9-3666-4e89-a672-8c271315604c" />

## Challenge Website

<img width="1366" height="687" alt="Screenshot (69)" src="https://github.com/user-attachments/assets/cc129d22-0c6f-495a-87b6-1ef437d8df28" />


---

## 🔍 Enumeration & Initial Thoughts
- Inspected the web page using browser DevTools.  
- Navigated to the **Application → Storage → Cookies** section.  
- Found a variable named `secret_recipe` containing an encoded string.  

<img width="1366" height="683" alt="Screenshot (72)" src="https://github.com/user-attachments/assets/b31be7d6-4dab-4d3b-a3ad-ddd6c9a7abd4" />


---

## ⚙️ Exploitation
1. Copied the value of the `secret_recipe` cookie.  
2. Applied **URL decoding** to make sure the string was in its proper form.  
3. Used **Burp Suite Decoder** to fully decode the string.  
4. Retrieved the flag from the decoded output. 

<img width="1366" height="711" alt="Screenshot (73)" src="https://github.com/user-attachments/assets/352e64b0-c3ee-426c-82ef-98ff403941e0" />


---

## 🏁 Flag
picoCTF{c00k1e_m0nster_l0ves_c00kies_2C8040EF}

---

## 📚 Key Takeaways
- Always inspect cookies and local storage when analyzing web applications.  
- Encoded data (URL/Base64/etc.) can often hide sensitive information.  
- Burp Suite Decoder is a reliable tool for testing multiple decoding steps quickly.
