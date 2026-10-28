from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name)

if __name__ == '__main__':
    # تشغيل السيرفر على جميع عناوين الشبكة المحلية
    app.run(host='0.0.0.0', port=5000)