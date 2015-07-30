from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this li
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    # Get the caller's phone number from the incoming Twilio request
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")    
    if from_number:
        return str(from_number)
    else:
        return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
