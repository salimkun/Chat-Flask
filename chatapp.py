
import json
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'bucinkochengorenss'
socketio = SocketIO(app)
list_message = []

@app.route( '/' )
def index():
    return render_template( './ChatAppPage.html' )

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )
  if 'user_name' in json:
      list_message.append(json)

@app.route( '/chat', methods=['POST', 'GET'] )
def chat():
    if request.method == 'POST':
        data = sending()
    if request.method == 'GET':
        data = inbox()    
    return data

def sending():
    if request.json:
        username = json.loads(request.data).get('user_name')
        message = json.loads(request.data).get('message')
    else:
        username = request.form.get('user_name')
        message = request.form.get('message')
    
    data_json = {
        'user_name': username,
        'message': message
    }

    socketio.emit( 'my response', data_json, broadcast=True)
    data = {
        'code': 200,
        'message': 'message sent'
    }
    if 'user_name' in data_json:
        list_message.append(data_json)
    return data

def inbox():
    data = {
        'code': 200,
        'bundle_message': list_message
    }
    return data 

if __name__ == '__main__':
    socketio.run( app, port=5000, debug = True )
