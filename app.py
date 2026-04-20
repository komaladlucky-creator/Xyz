from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Create static folder if not exists
if not os.path.exists("static"):
    os.makedirs("static")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        signal_type = request.form.get('signal')

        t = np.linspace(0, 1, 1000)
        carrier = np.cos(2 * np.pi * 50 * t)
        message = np.cos(2 * np.pi * 5 * t)

        if signal_type == "AM":
            modulated = (1 + message) * carrier
            title = "Amplitude Modulation"
        elif signal_type == "FM":
            modulated = np.cos(2 * np.pi * 50 * t + message)
            title = "Frequency Modulation"
        else:
            modulated = carrier
            title = "Carrier Signal"

        plt.figure()
        plt.plot(t, modulated)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")

        filepath = "static/output.png"
        plt.savefig(filepath)
        plt.close()

        return render_template("index.html", plot=filepath)

    return render_template("index.html", plot=None)

if __name__ == '__main__':
    app.run(debug=True)
