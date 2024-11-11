# app.py
# pip install Flask==2.2.2 "connexion[swagger-ui]==2.14.1"

# from flask import Flask, render_template # версия 0
from flask import render_template
import connexion

# app = Flask(__name__) # версия 0
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

# версия 0: выводит "Hello, World!" по адресу http://127.0.0.1:8000
# версия >=1: выводит "Hello, World!" по адресу http://127.0.0.1:8000
#   и структуру PEOPLE по адресу http://127.0.0.1:8000/api/people
#   и Swagger UI по адресу http://127.0.0.1:8000/api/ui