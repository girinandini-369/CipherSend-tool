# 🔐 Cipher Send – File Encryption System

A web-based application to upload, encrypt, and decrypt files securely using a password-based encryption system.

---

## 🚀 Overview

Cipher Send lets users upload any file, protect it with a password, and download the encrypted version — or reverse the process to recover the original. All file operations are logged to a local database for traceability.

---

## ⚙️ Features

- 📁 Upload and encrypt any file type
- 🔑 Password-based encryption and decryption
- 📥 Download encrypted or decrypted files directly from the browser
- 🗃️ SQLite logging of all file operations
- 🌐 Clean, minimal web interface

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Encryption | `crypto_utils` (custom module) |
| Database | SQLite, `db_utils` (custom module) |
| Frontend | HTML, CSS |

---

## 🧠 How It Works

1. User uploads a file via the web interface
2. User provides a password for encryption
3. `crypto_utils` encrypts the file using the password
4. Encrypted file is made available for download
5. For decryption, user re-uploads the encrypted file with the original password
6. `db_utils` logs each operation (filename, action, timestamp) to SQLite

---

## 📁 Project Structure

```
cipher-send/
├── app.py              # Flask app – routes and request handling
├── crypto_utils.py     # Encryption and decryption logic
├── db_utils.py         # Database logging helpers
├── database.db         # SQLite database (auto-created)
├── templates/
│   └── index.html      # Frontend UI
├── static/
│   └── style.css       # Stylesheet
├── uploads/            # Temporary file storage
└── requirements.txt
```

---

## 🌐 Live Demo

Deployed on Render:
🔗 [https://ciphersend-tool.onrender.com/](https://ciphersend-tool.onrender.com/)

---

## ▶️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd cipher-send
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

```
http://localhost:5000
```

### requirements.txt

```
flask
cryptography
```

---

## ⚠️ Limitations

- Encrypted files are stored temporarily — no persistent cloud storage
- Password is not hashed or stored; losing it means the file cannot be recovered
- Not suitable for very large files due to in-memory processing
- Single-user design; no authentication or user accounts

---

## 🔮 Future Improvements

- [ ] Add AES-256 encryption with key derivation (PBKDF2 / bcrypt)
- [ ] User authentication and personal file history
- [ ] Cloud storage integration (AWS S3 / Google Drive)
- [ ] File size limit enforcement and progress indicator
- [ ] Secure file expiry and auto-deletion after download

---
