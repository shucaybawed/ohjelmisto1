from flask import Flask, jsonify

app = Flask(__name__)

def on_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/alkuluku/<int:luku>")
def tarkista(luku):
    return jsonify({"Number": luku, "isPrime": on_alkuluku(luku)})

if __name__ == "__main__":
    app.run(port=3000)
