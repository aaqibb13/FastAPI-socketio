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

    
async def main():
    token = "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZDhkNWJkZTktZjQxNy00MTJkLThiNGMtYTUxM2IyODJmN2VkIiwidG9rZW5faWQiOiJhMGEzNjQ4NS1jZTc1LTQyODYtYTE2OC02YTEyNzA2YWMwODAifQ.Lddze6HPfaBXS49h0ov09eOxCuOZZutChbnogp8p5nQ"
    print(f"Token is: {token}")
    await sio.connect("http://localhost:8000", headers={"AUTHORIZATION": token})
    await sio.emit("send_message", data={
        "message": {
            "_id": "23372465-dv63-4h49-9yu4-93bhyt75a87y",
            "sender": "f9972465-db63-45c9-9c44-93bbce75af4c",
            "receiver": "fb55d1a7-e275-4bd5-bc10-60755ed7cc1c",
            "text": "some message",
            "status": "SENT",
            "user": {
                "_id": "some_id",
                "name": "someone's name"
            },
            "oldId": "dsfxdf-asd-sdsdc-asdcr-uegga"
        }
    })
    await sio.wait()

if __name__ == "__main__":
    asyncio.run(
            main()
            )