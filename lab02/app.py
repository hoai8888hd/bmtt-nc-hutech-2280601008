from flask import Flask, render_template, request, json
from cipher.caesar import caesarcipher
from cipher.vigenere import vigenerecipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import playfaircipher


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt",methods = ['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = caesarcipher()
    encrypted_text = Caesar.encrypt_text(text,key)
    return f"text: {text}<br/>key:{key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt",methods = ['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = caesarcipher()
    decrypted_text = Caesar.decrypt_text(text,key)
    return f"text: {text}<br/>key:{key}<br/>decrypted text: {decrypted_text}"

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere_encrypt",methods = ['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = vigenerecipher()
    encrypted_text = vigenere.vigenere_encrypt(text,key)
    return f"text: {text}<br/>key:{key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere_decrypt",methods = ['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = vigenerecipher()
    decrypted_text = vigenere.vigenere_decrypt(text,key)
    return f"text: {text}<br/>key:{key}<br/>decrypted text: {decrypted_text}"

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')
@app.route("/railfence_encrypt",methods = ['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key =int( request.form['inputKeyPlain'])
    RF= RailFenceCipher()
    encrypted_text = RF.railfence_encrypt(text,key)
    return f"text: {text}<br/>key:{key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence_decrypt",methods = ['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    RF = RailFenceCipher()
    decrypted_text = RF.railfence_decrypt(text,key)
    return f"text: {text}<br/>key:{key}<br/>decrypted text: {decrypted_text}"

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route("/create_playfair_matrix",methods=['POST'])
def create_playfair_matrix():
    text = request.form['inputPlainText']
    playfair=playfaircipher()
    create_text = playfair.create_playfair_matrix(text)
    return f"text: {text}<br/>key:{create_text}"

@app.route("/playfair_encrypt",methods = ['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key =request.form['inputKeyPlain']
    playfair=playfaircipher()
    create_text = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text,create_text)
    return f"text: {text}<br/>key:{key}<br/>encrypted text: {encrypted_text}"
@app.route("/playfair_decrypt",methods = ['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key =request.form['inputKeyCipher']
    playfair=playfaircipher()
    create_text = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text,create_text)
    return f"text: {text}<br/>key:{key}<br/>decrypted text: {decrypted_text}"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)