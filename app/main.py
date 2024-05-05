from flask import Flask

web = Flask(__name__)
if __name__ == "__main__":
    web.run(port=8080)

