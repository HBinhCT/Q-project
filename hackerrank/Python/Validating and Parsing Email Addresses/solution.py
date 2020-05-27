import email.utils
import re

pattern = r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
for _ in range(int(input())):
    email_info = email.utils.parseaddr(input())
    if re.match(pattern, email_info[1]):
        print(email.utils.formataddr(email_info))
