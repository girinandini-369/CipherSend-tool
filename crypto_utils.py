# crypto_utils.py
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from hashlib import sha256
import os

def pw_to_key(pw):
    return sha256(pw.encode()).digest()

def encrypt_file(path, fn, pw, enc_folder="encrypted"):
    data = open(path,"rb").read()
    key = pw_to_key(pw)
    cipher = AES.new(key,AES.MODE_CFB)
    ciphertext = cipher.encrypt(data)
    hash_digest = SHA256.new(data).digest()
    enc_fn = fn + ".enc"
    with open(os.path.join(enc_folder, enc_fn),"wb") as f:
        f.write(cipher.iv + hash_digest + ciphertext)
    return enc_fn

def decrypt_file(path, pw, dec_folder="decrypted"):
    with open(path,"rb") as f:
        iv = f.read(16)
        orig_hash = f.read(32)
        ciphertext = f.read()
    key = pw_to_key(pw)
    cipher = AES.new(key,AES.MODE_CFB,iv=iv)
    data = cipher.decrypt(ciphertext)
    if SHA256.new(data).digest() != orig_hash:
        raise ValueError("Wrong key or corrupted file!")
    dec_fn = os.path.basename(path).replace(".enc","")
    open(os.path.join(dec_folder, dec_fn),"wb").write(data)
    return dec_fn