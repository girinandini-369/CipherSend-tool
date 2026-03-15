# app.py
from flask import Flask, request, send_file, render_template
import os
from crypto_utils import encrypt_file, decrypt_file
from db_utils import init_db, log_file

# --- Setup ---
folders = ["uploads","encrypted","decrypted"]
for f in folders: os.makedirs(f, exist_ok=True)

init_db()
app = Flask(__name__, template_folder="templates", static_folder="static")

# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def enc():
    f = request.files['file']
    pw = request.form['password']
    path = os.path.join("uploads", f.filename)
    f.save(path)
    enc_fn = encrypt_file(path, f.filename, pw)
    log_file(f.filename, enc_fn, pw)
    return render_template("index.html", msg=f"✅ Encrypted {f.filename}", link=f"/download/encrypted/{enc_fn}", category="success")

@app.route("/decrypt", methods=["POST"])
def dec():
    f = request.files['file']
    pw = request.form['password']
    path = os.path.join("uploads", f.filename)
    f.save(path)
    try:
        dec_fn = decrypt_file(path, pw)
        return render_template("index.html", msg=f"🔓 Decrypted {dec_fn}", link=f"/download/decrypted/{dec_fn}", category="success")
    except Exception:
        return render_template("index.html", msg="❌ Decryption failed. Wrong key?", category="error")

@app.route("/download/<folder>/<fn>")
def download(folder, fn):
    return send_file(os.path.join(folder, fn), as_attachment=True)

if __name__=="__main__":
    app.run(debug=True)