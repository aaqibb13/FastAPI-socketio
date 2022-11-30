# FastAPI-socketio
This is a test Socket.IO client and server (both standard and asynchronous versions) wrapped with FastAPI

- Standard and Async Client and Server Event examples:

   - Standard examples: [Standard version](https://github.com/aaqibb13/FastAPI-socketio/tree/main/standard_examples)
    
   - Async examples are here: [Async version](https://github.com/aaqibb13/FastAPI-socketio/tree/main/async_examples)

- How do you run and test the project locally in a directory of your choice:

      git clone https://github.com/aaqibb13/FastAPI-socketio/tree/main/async_examples

- Running the server:
You can run the async_server/standard server either using `uvicorn` as follows:
      
  ```python
     uvicorn --reload async_examples/async_server --port 8000
  ```
 
or by simply executing the corresponding python file:

  ```python
     python async_examples/async_server.py
  ```
`Note: You don't need to specify a port, by default uvicorn runs on 127.0.0.1 and port 8000`

- Running the client:
  
    ```python
       python async_examples/async_client.py
    ```
