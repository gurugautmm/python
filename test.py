import getpass

class Config:
    def __init__(self):
        # Direct values assigned (for demo purposes only)
        self.secret_key = "mySecretKey123!"
        self.password = "SuperSecurePass!"
        self.baseauth = "QmFzaWNBdXRoVG9rZW5FeGFtcGxlMTIz"  # pre-generated BaseAuth token

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
    
    # Authenticate with stored password
    runtime_pass = getpass.getpass("Enter runtime password: ")
    if runtime_pass == cfg.password:
        print("Password authentication successful.")
    else:
        print("Invalid password.")

    cfg.display_info()
