# DO NOT USE IN PRODUCTION.
# This file intentionally includes hardcoded secrets for testing secret detection tools.

import base64

# Simple credentials / secrets
SECRET_KEY = "mySecretKey123!"
password = "P@ssw0rd123!"                   # hardcoded password
baseauth = "QmFzaWM6ZGVtb1VzZXI6ZGVtb1Bhc3M="  # base64("demoUser:demoPass")

# Cloud / API keys (FAKE VALUES)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

GOOGLE_API_KEY = "AIzaSyA-1234567890abcdefGHIJKLMNOPQR"
STRIPE_SECRET_KEY = "sk_live_51H8xKfXXXXXXXXXXXXXXXXXXXXXXXX"
SLACK_BOT_TOKEN = "xoxb-123456789012-1234567890123-abcdefghijklmnopqrstuvwx"

# DB connection string with embedded password (FAKE)
DATABASE_URL = "postgresql://test_user:SuperSecurePass!@localhost:5432/appdb"

# OAuth-style client info (FAKE)
OAUTH_CLIENT_ID = "1234567890-abcdefghi.apps.googleusercontent.com"
OAUTH_CLIENT_SECRET = "GOCSPX-abcdefghijklmnopqrstuvwx123456"

# SSH private key (truncated, FAKE)
FAKE_SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEA1nQ7f6mQ7gqk3Z2u3bY0q1xQ3F2b0cJKlYQ6Yk9y1rEXAMPLE
f7l9qjJ4m4N4eVv2V3fQHc5jA4eS2n1YbO5jVb1XyDkC2i5g9R3k1sQ==
-----END OPENSSH PRIVATE KEY-----"""

def demo():
    # Simulate using a secret (to avoid “unused variable” warnings)
    basic_header = "Basic " + baseauth
    masked = "*" * (len(password) - 3) + password[-3:]
    print("Loaded config:")
    print("  SECRET_KEY:", "*" * (len(SECRET_KEY) - 3) + SECRET_KEY[-3:])
    print("  password (masked):", masked)
    print("  Authorization:", basic_header[:20] + "... (truncated)")
    # decode just to "use" the value; not needed for detection
    print("  decoded baseauth:", base64.b64decode(baseauth).decode("utf-8"))

if __name__ == "__main__":
    demo()
