## without any GUI 


import re

text_email = input("Enter the text to scan: ")
text_phone = input("Enter the phone number: ")
text_url = input("Enter the URL: ")


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
    if number.startswith("+91"):
        phones.append(number)
    else:
        phones.append("+91" + number)

print("\nEmails Found:" if emails else "\nNo valid email addresses found.")
if emails:
    print(emails)

print("\nPhone Numbers Found:" if phones else "\nNo valid phone numbers found.")
if phones:
    print(phones)

print("\nURLs Found:" if urls else "\nNo valid URLs found.")
if urls:
    print(urls)
