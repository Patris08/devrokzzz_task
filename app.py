from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """
    Main endpoint of the application.

    Returns:
        str: Simple message confirming the app is running.
    """
    return "DevOps task is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run the application on all network interfaces at port 5000