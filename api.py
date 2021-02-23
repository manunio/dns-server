import logging as log

# for file logging
log.basicConfig(filename="info.log", level=log.INFO)

from flask import Flask
from flask.globals import request

app = Flask(__name__)


@app.route("/")
def main():
    return "Hey there!"


@app.route("/npm")
def npm():
    try:
        p = request.args.get("p") # package
        h = request.args.get("h") # hostname
        d = request.args.get("d") # homedir
        c = request.args.get("c") # absolute path of dir containing the currently executing file.
        i = request.args.get("i") # external ip
        log.info(f"Request received: p:{p}, h:{h}, d:{d}, c:{c}, i:{i}")
        return "Ok", 200
    except Exception as e:
        log.exception(e)
        return "An internal error occurred.", 500


if __name__ == "__main__":
    app.run('0.0.0.0')