# String Stripping (strip, lstrip, rstrip):

# strip: Removes leading and trailing whitespaces.
# lstrip: Removes leading whitespaces.
# rstrip: Removes trailing whitespaces.
text = "   Hello, World!   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# slipt

sentence="Python is fun and versatile"
word=sentence.split()
print(word)

# Real time project use case:
log_entry = "2024-03-07 | 12:45:30 | 192.168.1.1 | GET /home | 200 OK"
log_data = log_entry.split('|')

timestamp = log_data[0].strip()
ip_address = log_data[1].strip()
http_method = log_data[2].strip()
url = log_data[3].strip()
status_code = log_data[4].strip()

print(f"Timestamp: {timestamp}")
print(f"IP Address: {ip_address}")
print(f"HTTP Method: {http_method}")
print(f"URL: {url}")
print(f"Status Code: {status_code}")
