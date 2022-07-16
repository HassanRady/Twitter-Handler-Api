import uvicorn
from fastapi import FastAPI

from TwitterHandler.Kafka.stream import Streamer 


app = FastAPI()
streamer = Streamer()


@app.get('/')
async def index():
    return {"Hello": "From index"}


@app.get('/start_stream')
async def start_stream(query: str):
    streamer.start_stream(query)
    return {"Stream": "Started!!!"}


@app.get('/stop_stream')
async def stop_stream():
    streamer.stop_stream()
    return {"Stream": "Stopped!!!"}

@app.get('/other')
async def other():
    return {"Hello": "From other"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)