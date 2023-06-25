from fastapi import FastAPI
from routers import users
import time
import datetime

app = FastAPI()
app.include_router(users.router, tags=['users'])


@app.middleware('http')
async def procces_time_header(request, call_next):
    # before
    start_time = time.time()  # give me the right time
    response = await call_next(request)  # do process and response to client
    process_time = time.time() - start_time  # calculate the process time
    response.headers['X_process_time'] = str(process_time)
    # after
    return response


@app.on_event('startup')
def startup_event():
    with open('server_log_time.log', 'a') as log:
        log.write(f"Applications started in : {datetime.datetime.now()} \n")


@app.on_event('shutdown')
def shutdown_event():
    with open('server_log_time.log', 'a') as log:
        log.write(f"Applications shutdown in : {datetime.datetime.now()} \n")
