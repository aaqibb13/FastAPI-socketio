import socketio


sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ, data):
    print(f'connect with sid: {sid} on environ: {environ}, with data {data}')
    if data:        
        print(f"data is: {data}")
    print("After connect")

@sio.event
def disconnect(sid):
    print(f'disconnect {sid}')

@sio.event
def data(sid, data):
    print(f"sid is: {sid}")
    print(f"data is: {data}")
    return data

@sio.event
def send_message(sid, data):
    print(f" message for sid: {sid} is: {data}")
    return data