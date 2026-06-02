import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối các nút bấm
        self.ui.btn_generatekey.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        response = requests.get('http://127.0.0.1:5000/api/rsa/generate_keys')
        if response.status_code == 200:
            data = response.json()
            msg = QMessageBox()
            msg.setText(data["message"])
            msg.exec_()

    def call_api_encrypt(self):
        payload = {'message': self.ui.txt_plaintext.toPlainText(), 'key_type': 'public'}
        response = requests.post('http://127.0.0.1:5000/api/rsa/encrypt', json=payload)
        if response.status_code == 200:
            self.ui.txt_ciphertext.setText(response.json()['encrypted_message'])

    def call_api_decrypt(self):
        payload = {'ciphertext': self.ui.txt_ciphertext.toPlainText(), 'key_type': 'private'}
        response = requests.post('http://127.0.0.1:5000/api/rsa/decrypt', json=payload)
        if response.status_code == 200:
            self.ui.txt_plaintext.setText(response.json()['decrypted_message'])

    def call_api_sign(self):
        payload = {'message': self.ui.txt_information.toPlainText()}
        response = requests.post('http://127.0.0.1:5000/api/rsa/sign', json=payload)
        if response.status_code == 200:
            self.ui.txt_signature.setText(response.json()['signature'])

    def call_api_verify(self):
        payload = {'message': self.ui.txt_information.toPlainText(), 'signature': self.ui.txt_signature.toPlainText()}
        response = requests.post('http://127.0.0.1:5000/api/rsa/verify', json=payload)
        if response.status_code == 200:
            is_valid = response.json().get('is_verified')
            QMessageBox.information(self, "Verify", "Success" if is_valid else "Fail")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())