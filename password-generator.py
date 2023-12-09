import string, secrets

alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for i in range(10))

print(f"new password generated: {password}")
