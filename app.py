from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

import uvicorn
from fastapi import FastAPI

from TwitterHandler.Kafka.stream import Streamer 


app = FastAPI()
streamer = Streamer()


@app.get('/')
async def index():
    return {"Hello": "From index"}


@app.get('/start')
async def start_twitter_stream(topic: str):
    streamer.start_stream(topic)
    return {"Status": "started"}


@app.get('/stop')
async def stop_twitter_stream():
    streamer.stop_stream()
    return {"Status": "stopped"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)