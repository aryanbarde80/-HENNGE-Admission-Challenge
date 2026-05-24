
import requests
import json
import base64
import hmac
import hashlib
import time
import struct

def get_totp_token(secret, digits=10, interval=30):
    t = int(time.time()) // interval
    msg = struct.pack(">Q", t)
    hmac_hash = hmac.new(secret.encode('ascii'), msg, hashlib.sha512).digest()
    offset = hmac_hash[-1] & 0x0F
    truncated_hash = hmac_hash[offset:offset+4]
    code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
    totp = str(code % (10 ** digits)).zfill(digits)
    return totp

def submit():
    url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"
    email = "aryanbarde80@gmail.com"
    gist_url = "https://gist.github.com/aryanbarde80/1ce8320c838ef24691848652e86e49c4"
    
    shared_secret = email + "HENNGECHALLENGE004"
    totp_password = get_totp_token(shared_secret)
    
    auth_str = f"{email}:{totp_password}"
    auth_b64 = base64.b64encode(auth_str.encode('ascii')).decode('ascii')
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_b64}"
    }
    
    payload = {
        "github_url": gist_url,
        "contact_email": email,
        "solution_language": "python"
    }
    
    print(f"Submitting to {url}...")
    print(f"Payload: {json.dumps(payload)}")
    
    response = requests.post(url, headers=headers, json=payload)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    submit()
