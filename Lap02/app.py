from flask import Flask, render_template, request

from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


def render_cipher_page(cipher_name, cipher_url, result=None, input_text=None, key=None):
    return render_template(
        "cipher_form.html",
        cipher_name=cipher_name,
        cipher_url=cipher_url,
        result=result,
        input_text=input_text,
        key=key
    )


def call_method(obj, method_names, *args):
    for method_name in method_names:
        if hasattr(obj, method_name):
            method = getattr(obj, method_name)
            return method(*args)

    raise Exception("Không tìm thấy hàm mã hóa/giải mã phù hợp trong class.")


# =========================
# CAESAR CIPHER
# =========================

@app.route("/caesar")
def caesar():
    return render_cipher_page("CAESAR CIPHER", "caesar")


@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["plain_text"]
    key = int(request.form["key"])

    cipher = CaesarCipher()
    result = call_method(
        cipher,
        ["encrypt_text", "encrypt"],
        text,
        key
    )

    return render_cipher_page("CAESAR CIPHER", "caesar", result, text, key)


@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["cipher_text"]
    key = int(request.form["key"])

    cipher = CaesarCipher()
    result = call_method(
        cipher,
        ["decrypt_text", "decrypt"],
        text,
        key
    )

    return render_cipher_page("CAESAR CIPHER", "caesar", result, text, key)


# =========================
# VIGENERE CIPHER
# =========================

@app.route("/vigenere")
def vigenere():
    return render_cipher_page("VIGENERE CIPHER", "vigenere")


@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["plain_text"]
    key = request.form["key"]

    cipher = VigenereCipher()
    result = call_method(
        cipher,
        ["vigenere_encrypt", "encrypt_text", "encrypt"],
        text,
        key
    )

    return render_cipher_page("VIGENERE CIPHER", "vigenere", result, text, key)


@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["cipher_text"]
    key = request.form["key"]

    cipher = VigenereCipher()
    result = call_method(
        cipher,
        ["vigenere_decrypt", "decrypt_text", "decrypt"],
        text,
        key
    )

    return render_cipher_page("VIGENERE CIPHER", "vigenere", result, text, key)


# =========================
# RAIL FENCE CIPHER
# =========================

@app.route("/railfence")
def railfence():
    return render_cipher_page("RAIL FENCE CIPHER", "railfence")


@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["plain_text"]
    key = int(request.form["key"])

    cipher = RailFenceCipher()
    result = call_method(
        cipher,
        ["rail_fence_encrypt", "encrypt_text", "encrypt"],
        text,
        key
    )

    return render_cipher_page("RAIL FENCE CIPHER", "railfence", result, text, key)


@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["cipher_text"]
    key = int(request.form["key"])

    cipher = RailFenceCipher()
    result = call_method(
        cipher,
        ["rail_fence_decrypt", "decrypt_text", "decrypt"],
        text,
        key
    )

    return render_cipher_page("RAIL FENCE CIPHER", "railfence", result, text, key)


# =========================
# PLAYFAIR CIPHER
# =========================

@app.route("/playfair")
def playfair():
    return render_cipher_page("PLAYFAIR CIPHER", "playfair")


@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["plain_text"]
    key = request.form["key"]

    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    result = cipher.playfair_encrypt(text, matrix)

    return render_cipher_page("PLAYFAIR CIPHER", "playfair", result, text, key)


@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["cipher_text"]
    key = request.form["key"]

    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    result = cipher.playfair_decrypt(text, matrix)

    return render_cipher_page("PLAYFAIR CIPHER", "playfair", result, text, key)


# =========================
# TRANSPOSITION CIPHER
# =========================

@app.route("/transposition")
def transposition():
    return render_cipher_page("TRANSPOSITION CIPHER", "transposition")


@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["plain_text"]
    key = int(request.form["key"])

    cipher = TranspositionCipher()
    result = cipher.encrypt(text, key)

    return render_cipher_page("TRANSPOSITION CIPHER", "transposition", result, text, key)


@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["cipher_text"]
    key = int(request.form["key"])

    cipher = TranspositionCipher()
    result = cipher.decrypt(text, key)

    return render_cipher_page("TRANSPOSITION CIPHER", "transposition", result, text, key)


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)