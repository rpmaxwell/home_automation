from flask import Flask, render_template, Response, request, jsonify
from dht11 import DHT11
import os

pin_map = {
        "lamp": 3,
        "temperature": 2
}

app = Flask(__name__)

app.secret_key = os.environ['SECRET_KEY']


@app.route("/", methods=['GET', 'POST'])
def lamp():
    pin = pin_map['lamp']
    if request.method == 'POST':
        lamp_manager.lamp_control(pin) 
    return render_template('lights.html')

@app.route("/lamp_controller/", methods=['GET', 'POST'])
def lamp_endpoint():
    if request.method == 'GET':
        pin = pin_map['lamp']
        lamp_manager.lamp_control(pin)
        return "hello, world!"

@app.route("/lamp_status/")
def lamp_status():
    import lamp_manager
    pin = pin_map['lamp']
    lamp_state = lamp_manager.lamp_status(pin)
    return str(lamp_state)

@app.route("/climate/")
def get_temp():
    pin = pin_map['temperature']
    instance = DHT11(pin=pin)
    r = instance.read()
    return jsonify(
        temperature=r.temperature,
        humidity=r.humidy
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
