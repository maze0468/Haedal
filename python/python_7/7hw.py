from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def introduce():
    return "2021116124 경제통상학부 이주영"

@app.route("/me/")
def itsme():
    return render_template('index.html', itsme_img='drawnbyme.jpg')

if __name__ == "__main__":
    app.run(debug=True)
