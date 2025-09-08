import base64
import getpass

class Config:
    def __init__(self):
        # Direct values assigned (for demo purposes only)
        self.secret_key = "mySecretKey123!"
        self.password = "SuperSecurePass!"
        
        # Create a BaseAuth string from direct user/pass
        user = "demoUser"
        pwd = "demoPass123"
        token = "mysceretetocket-09#45f"
        baseAuth = "mybaseauthca894j8nergrengSDNFUISNGWRFG"

    def display_info(self):
        print("Configuration loaded successfully.")
        print(f"Secret Key (masked): {self._mask(self.secret_key)}")
        print(f"Password (masked): {self._mask(self.password)}")
        print(f"BaseAuth Token: {baseAuth}")

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
