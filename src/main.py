"""
main.py
- Read from input file
- Perform attack on RSA algorithm to get original message
"""

from Crypto.Util.number import *

from Services.io import *
from attack import *
from mpmath import mp

mp.dps = 1024

# Read parameter from input file
version, n, e, c = parse_input_file()

# Try to attack RSA according to the version used
if version == "A":
    m = rsa_version_A_attack(n, e, c)
elif version == "B":
    m = rsa_version_B_attack(n, e, c)
elif version == "C":
    m = rsa_version_C_attack(n, c)
elif version == "D":
    m = rsa_version_D_attack(e, c)
elif version == "E":
    m = rsa_version_E_attack(n, e, c)

# Print the message
print(f"Original message: {long_to_bytes(m).decode()}")