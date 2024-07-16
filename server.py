from flask import Flask
from routes import routes
from multiprocessing import Process
from flask_cors import CORS




app = Flask(__name__)
app.register_blueprint(routes)
CORS(app) 

@app.route("/")
def home():
    return "API do Amor ao Próximo"

def run_server():
    app.run(debug=False, use_reloader=False)

if __name__ == '__main__':
    server_process = Process(target=run_server)
    server_process.start()
    server_process.join()
