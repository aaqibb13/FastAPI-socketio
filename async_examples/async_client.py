import socketio
import asyncio

# asyncio Client
sio = socketio.AsyncClient()

@sio.event
async def connect_error(e):
    print(f"The connection failed: {e}")


@sio.event
async def disconnect(sio, sid):
    print(f"sio: {sio} and sid: {sid}")
    print("I'm disconnected!")

@sio.event
async def new_message(data):
    print(f"new_message from server:")
    print(f"data: {data}")
    return data

@sio.event
async def notifications(data):
    print(f"notifications: {data}")
    return data
    
async def main():
    token = "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmYyMTRjNTUtMWNkNC00YmM1LTg0MWQtZjFjMmQ2NmZkODcxIiwidG9rZW5faWQiOiI0YjcyODI3MS04MWJhLTQ5NTUtOWYxMi0wNjgxNzNiMGQ1ZTMifQ.NR2RJ-qI-6e8O80X92HdXe1m0zS8dNmj3M7y4DdYu8w"
    print(f"Token is: {token}")
    await sio.connect("http://localhost:8000/", headers={"AUTHORIZATION": token})
    await sio.emit("send_message", data={
        "message": {
            "_id": "09372465-dv63-avc5-9yu4-93bhyt75a008",
            "sender": "7820a8a3-ad2a-40ba-bc59-0ba6cf0386d6",
            "receiver": "6375e368-4b27-4687-8a2c-3bf5168a332a",
            "text": "Venkatesh is a client sending the message to Neymar Jr",
            "status": "SENT",
            "user": {
                "_id": "7820a8a3-ad2a-40ba-bc59-0ba6cf0386d6",
                "name": "Venkatesh Babu"
            },
        }
    })
    await sio.wait()

if __name__ == "__main__":
    asyncio.run(
            main()
            )

