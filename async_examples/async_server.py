import socketio
import uvicorn
import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(
    title="Socket.IO",
    openapi_url=f"/api/v1/openapi.json",
    debug=False
)


sio = socketio.AsyncServer(
        async_mode="asgi"
        )
sio_app = socketio.ASGIApp(sio)


app.mount("/", sio_app)

@sio.event
async def connect(sid, environ):
    print(f'connect with sid: {sid} on environ: {environ}')
    print(f"header is: ", environ.get("HTTP_AUTHORIZATION"))
    print("After connect")

@sio.event
async def disconnect(sid):
    print(f'disconnect {sid}')

@sio.event
async def send_message(sid, data):
    sender = data["sender"]
    message = data["message"]
    print({f"session id for sender {sender}: {sid}"})

    print(f"message is: {message}")


if __name__ == "__main__":
    print(f"here", os.getenv("HOST"))
    print(f"here", os.getenv("PORT"))
    uvicorn.run(
        app=app,
        host=os.getenv("HOST"),
        port=os.getenv("PORT")
    )