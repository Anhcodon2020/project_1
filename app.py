from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Chào mừng bạn đến với ScanFile trên Render!</h1><p>Project đã chạy thành công.</p>'

if __name__ == '__main__':
    # Render sẽ cung cấp cổng (Port) tự động qua biến môi trường
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)