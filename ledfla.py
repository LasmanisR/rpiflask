import RPi.GPIO as GPIO
from flask import Flask

GPIO.setmode(GPIO.BCM)

for pin:
   GPIO.setup(2,GPIO.OUT)
   GPIO.setup(3,GPIO.OUT)
   GPIO.output(2, GPIO.LOW)
   GPIO.output(3, GPIO.LOW)

@app.route("/")
def main():
   
   for pin:
      pin['state'] = GPIO.input(2)
      pin['state'] = GPIO.input(3)
   templateData = {
      'pin' : pin
      }

   return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
   changePin = int(changePin)

   deviceName = pchangePin['name']
   if action == "on":
      GPIO.output(changePin, GPIO.HIGH)
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   for pin in pins:
      pin['state'] = GPIO.input(2)
      pin['state'] = GPIO.input(3)

   templateData = {
      'pin' : pin
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0')