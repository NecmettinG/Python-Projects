# main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import json
from datetime import datetime

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = [] #Empty list with WebSocket instance elements.
        self.connection_count = 0

    async def connect(self, websocket: WebSocket): #For websocket connection.
        await websocket.accept() #websocket.accept() method accepts incoming WebSocket connection. The method comes from WebSocket class.
        self.active_connections.append(websocket) #appending active WebSocket connection to active_connections list.
        self.connection_count += 1 #incrementing the active connection counter.
        print(f"New connection established. Total connections: {self.connection_count}")

    def disconnect(self, websocket: WebSocket): #for websocket disconnection.
        self.active_connections.remove(websocket) #removes the innactive WebSocket connection from active_connections list.
        self.connection_count -= 1 #decrementing the active connection counter.
        print(f"Connection closed. Total connections: {self.connection_count}")

    async def broadcast(self, message: str): #This method is for broadcasting text messages to all active clients.
        print(f"Broadcasting message: {message}")
        for connection in self.active_connections: #connection will hold each WebSocket instances from the list.
            await connection.send_text(message) #connection.send_text(message) will send text message to client. The method comes from WebSocket class.

manager = ConnectionManager() #manager is an instance of ConnectionManager class.

@app.get("/")
async def get():
    return {"message": "WebSocket Server is running"} 

@app.websocket("/ws/{client_id}") #This decorator is for defining websocket endpoint. This endpoint handles WebSocket lifecycle, from connection to disconnection.
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket) #we used manager instance's connect method and sent websocket instance to the method. We will accept that websocket.
    print(f"Client {client_id} connected")
    print(f"websocket {websocket} is accepted.")

    try:
        while True:
            data = await websocket.receive_text() #websocket.receive_text() is for receiving text messages from client.
            print(data)
            print(type(data))

            try:
                message_data = json.loads(data) #json.loads(data) is for deserializing data (a str, bytes or bytearray instance containing a JSON document) to a Python object.
                print(message_data)
                print(type(message_data))
                timestamp = datetime.now().strftime("%H:%M:%S")
                message_data.update({ #message_data is a python object. It is a dictionary and we add client_id and timestamp keys.
                    "client_id": client_id,
                    "timestamp": timestamp
                })
                print(message_data)
                print(f"Received from client {client_id}: {message_data['message']}")
                await manager.broadcast(json.dumps(message_data)) #json.dumps(message_data) serializes message_data to a JSON formatted str.
                #we will send all keys and values to broadcast method. (message, client_id and timestamp.) WE ARE SENDING A STRING BTW!

            except json.JSONDecodeError: #If we get json decoding exception:
                print(f"Received plain text from client {client_id}: {data}") #data is a str, bytes or bytearray instance containing a JSON document.
                await manager.broadcast(f"Client {client_id}: {data}") #we will send this string to broadcast method.

    except WebSocketDisconnect: #WebSocketDisconnect class is for websocket disconnection.
        manager.disconnect(websocket) #we are going to remove disconnected websocket from the list.
        disconnect_message = f"Client #{client_id} left the chat"
        print(disconnect_message)
        await manager.broadcast(json.dumps({
            "client_id": "system",
            "message": disconnect_message,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "type": "disconnect"
        }))