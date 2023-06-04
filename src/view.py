# cording: utf-8
from flask import Flask, render_template
# appという名前で Flask をインスタンス化
app = Flask(__name__)

# --- view側の設定 ---
# ルートディレクトリにアクセスした場合の挙動
@app.route('/')
# def以下がアクセス後の操作
def index():
    # return 'Hello World2!'
    return render_template('index.html')
# エントリーポイントの設定
if __name__ == '__main__':
    app.run()
    
