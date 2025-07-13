import re
import tkinter as tk
from tkinter import messagebox, font

def extract_patterns():
    text_email = email_entry.get()
    text_phone = phone_entry.get()
    text_url = url_entry.get()

    text = text_email + " " + text_phone + " " + text_url
    text = re.sub(r'www,([a-zA-Z0-9\-]+),([a-z]{2,})', r'www.\1.\2', text)

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"
    phone_pattern = r"(?:\+91[-\s]?)?[6-9][0-9]{9}"
    url_pattern = r"\b(?:https?://|www\.)[a-zA-Z0-9\-]+\.[a-z]{2,}(?:/[^\s]*)?\b"

    emails = re.findall(email_pattern, text)
    raw_phones = re.findall(phone_pattern, text)
    urls = [match.group(0) for match in re.finditer(url_pattern, text)]

    phones = []
    for number in raw_phones:
        number = number.strip().replace(" ", "").replace("-", "")
        if not number.startswith("+91"):
            number = "+91" + number
        phones.append(number)

    result = ""
    result += " Emails Found:\n" + ("\n".join(emails) if emails else "No valid emails found.") + "\n\n"
    result += " Phone Numbers Found:\n" + ("\n".join(phones) if phones else "No valid phone numbers found.") + "\n\n"
    result += " URLs Found:\n" + ("\n".join(urls) if urls else "No valid URLs found.")

    messagebox.showinfo("Extraction Results", result)

# Setup 
window = tk.Tk()
window.title("Pattern Recognizer")
window.geometry("450x380")
window.configure(bg="#f2f2f2")

header_font = font.Font(family="Helvetica", size=14, weight="bold")
label_font = font.Font(family="Arial", size=10)

# Title 
tk.Label(window, text="Pattern Recognition using Regex", font=header_font, bg="#f2f2f2", fg="#333").pack(pady=10)

# Email Entry
tk.Label(window, text="Enter Email Text:", font=label_font, bg="#f2f2f2").pack(anchor="w", padx=20)
email_entry = tk.Entry(window, width=50, font=label_font)
email_entry.pack(padx=20, pady=5)

# Phone Entry
tk.Label(window, text="Enter Phone Number:", font=label_font, bg="#f2f2f2").pack(anchor="w", padx=20)
phone_entry = tk.Entry(window, width=50, font=label_font)
phone_entry.pack(padx=20, pady=5)

# URL Entry
tk.Label(window, text="Enter URL:", font=label_font, bg="#f2f2f2").pack(anchor="w", padx=20)
url_entry = tk.Entry(window, width=50, font=label_font)
url_entry.pack(padx=20, pady=5)

extract_btn = tk.Button(window, text="🔍 Extract Patterns", command=extract_patterns, bg="#4CAF50", fg="white", font=label_font)
extract_btn.pack(pady=20)


window.mainloop()
