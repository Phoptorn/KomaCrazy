from tools import *

@app.route('/')
def page():
    return 'ยินดีต้อนรับ'

@app.route('/register')
def page1():
    data = request.args
    list_data = {
        "id": data["id"],
        "password": data["password"]
    }
    return jsonify(list_data)

if __name__ == '__main__':
    app.run(host,port)