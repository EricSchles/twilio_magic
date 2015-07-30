from flask import Flask, request, redirect
import twilio.twiml 
import datetime
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    # Get the caller's phone number from the incoming Twilio request
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    print from_number
    # if the caller is someone we know:
    if from_number in callers:
        # Greet the caller by name
        resp.say("Hello " + callers[from_number])
    else:
        resp.say("Hello Monkey")
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
