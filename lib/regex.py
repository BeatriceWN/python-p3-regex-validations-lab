import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

import re

#matches names like 
#John Cena
#Anya Taylor-Joy
#D'Angelo
#Mary-Kate O'Neill
# - Capital letter, then lowercase letters
# - A space
# - Another capital letter, then lowercase letters
name = r"^[A-Z][a-z]*(?:['-][A-Z][a-z]*)*(?: [A-Z][a-z]*(?:['-][A-Z][a-z]*)*)*$"
name_regex = re.compile(name)

#phone numbers:
# - (123) 456-7890
# - 123-456-7890
# - 5555555555
phone_number = r"^(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$"
phone_regex = re.compile(phone_number)


#matches emails like:
#john.cena@wwe.com 
#first.last@domain.co.uk
#123john.cena@wwe.com 
email_address = r"^[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
email_regex = re.compile(email_address)

