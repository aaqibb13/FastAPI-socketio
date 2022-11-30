import socketio
# import asyncio

# asyncio Client
sio = socketio.Client() 

@sio.event
def connect_error(e):
    print(f"The connection failed: {e}")


@sio.event
def disconnect():
    print("I'm disconnected!")

    
def main(user: str, message: str):
    print(f"user: {user}")
    sio.connect("http://localhost:8080/ws")
    sio.emit("data", data={"user_id": user})
    sio.emit("send_message", data={"message": message})
    sio.wait()

if __name__ == "__main__":
    user = input("Input user_id: \n")
    message = input("Input message: \n")
    main(user=user, message=message)