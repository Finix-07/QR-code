from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()
    data = request.form.get('link')
    img = qrcode.make(data, version=2, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    img.save(memory, 'PNG')
    memory.seek(0)  

    base64_img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')
    

    return render_template('index.html', data=base64_img)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

