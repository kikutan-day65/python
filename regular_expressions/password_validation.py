"""
check password validation:
    - at least 8 char long
    - contain any sort letters, numbers $%#@
    - has to end with a number
"""
import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = "jdkfaSlh54352@%6"

check = pattern.fullmatch(password)
print(check)