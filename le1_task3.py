import re

def validator(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return "Valid email"
    else:
        return "Invalid email"

email1 = "ankitrai326@gmail.com"
email2 = "my.ownsite@our-earth.org"
email3 = "ankitrai326.com"
email4 = "maha453.hi_dgf.com"

print(validator(email1))
print(validator(email2))
print(validator(email3))
print(validator(email4))
