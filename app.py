from flask import Flask, render_template

app = Flask("__main__")

@app.route("/")
def home():
    return render_template("index.html", hostname="Switch 1")

if __name__ == "__main__":
    app.run(debug=True)