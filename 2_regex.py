import re

text = """
Contact us at info@example.com or support@domain.org.
Call +91-9876543210 or (123) 456-7890.
Event date: 2025-09-28, or 28/09/2025.
"""

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
phones = re.findall(r"\+?\d{1,3}[-.\s]?\(?\d+\)?[-.\s]?\d+[-.\s]?\d+", text)
dates = re.findall(r"\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2}", text)

print("Emails:", emails)
print("Phones:", phones)
print("Dates:", dates)