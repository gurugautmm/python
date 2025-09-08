import os
import base64
import getpass

class Config:
    def __init__(self):
        # Load from environment variables for security
        self.secret_key = os.getenv("SECRET_KEY", "default_secret")
        self.password = os.getenv("APP_PASSWORD", "default_password")

        # Encode Basic Auth credentials
        user = os.getenv("BASIC_USER", "admin")
        pwd = os.getenv("BASIC_PASS", "password123")
        token = f"{user}:{pwd}".encode("utf-8")
        self.baseauth = base64.b64encode(token).decode("utf-8")

    def display_info(self):
        print("Configuration loaded successfully.")
        print(f"Secret Key (masked): {self._mask(self.secret_key)}")
        print(f"Password (masked): {self._mask(self.password)}")
        print(f"BaseAuth Token: {self.baseauth}")

    def _mask(self, value):
        """Mask sensitive info except last 3 chars"""
        if len(value) <= 3:
            return "***"
        return "*" * (len(value) - 3) + value[-3:]

if __name__ == "__main__":
    cfg = Config()
    
    # Example: override password securely at runtime
    runtime_pass = getpass.getpass("Enter runtime password: ")
    if runtime_pass == cfg.password:
        print("Password authentication successful.")
    else:
        print("Invalid password.")

    cfg.display_info()
