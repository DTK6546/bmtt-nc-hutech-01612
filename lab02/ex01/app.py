from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router routes for caesar cipher
@app.route("/caesar", methods=['GET', 'POST'])
def caesar():
    encrypted_message = None
    decrypted_message = None

    if request.method == 'POST':
        # Lấy dữ liệu từ form
        if 'inputPlainText' in request.form:  # Nếu là yêu cầu mã hóa
            text = request.form['inputPlainText']
            key = int(request.form['inputKeyPlain'])
            Caesar = CaesarCipher()

            encrypted_message = Caesar.encrypt_text(text, key)

        elif 'inputCipherText' in request.form:  # Nếu là yêu cầu giải mã
            text = request.form['inputCipherText']
            key = int(request.form['inputKeyCipher'])
            Caesar = CaesarCipher()

            decrypted_message = Caesar.decrypt_text(text, key)

    return render_template('caesar.html', encrypted_message=encrypted_message, decrypted_message=decrypted_message)

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
