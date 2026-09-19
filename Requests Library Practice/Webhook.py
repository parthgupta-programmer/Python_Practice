from flask import Flask,request
import requests

# A webhook is a way for an application to send data to another application whenever a particular event happens.

app=Flask(__name__) # Creates the flask web app.

@app.route('/webhook',methods=['POST']) # It creates the webhook endpoint that accepts POST requests.
def webhook():
    data=request.json # Recieve the request.

    print('Webhook recieved') 
    print(data) # This reads the JSON body sent by the webhook provider.

    # It tells the sender that : I recieved your webhook successfully. 
    return {'Status':'Recieved'},200 


if __name__ == '__main__':
    app.run(debug=True)








