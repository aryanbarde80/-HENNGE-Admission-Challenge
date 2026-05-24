
import hmac
import hashlib
import time
import struct
import base64

def get_totp_token(secret, digits=10, interval=30):
    # TOTP is based on HOTP
    # secret is already the combined string as per requirements
    
    # Get the time step
    t = int(time.time()) // interval
    
    # Convert time step to 8-byte big-endian integer
    msg = struct.pack(">Q", t)
    
    # Use HMAC-SHA-512 as per requirements
    hmac_hash = hmac.new(secret.encode('ascii'), msg, hashlib.sha512).digest()
    
    # Dynamic truncation
    offset = hmac_hash[-1] & 0x0F
    truncated_hash = hmac_hash[offset:offset+4]
    
    # Convert to integer
    code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
    
    # Get the last 'digits' digits
    totp = str(code % (10 ** digits)).zfill(digits)
    
    return totp

if __name__ == "__main__":
    user_email = "aryanbarde80@gmail.com"
    shared_secret = user_email + "HENNGECHALLENGE004"
    print(get_totp_token(shared_secret))
