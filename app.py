from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    # Render sẽ cung cấp cổng (Port) tự động qua biến môi trường
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)