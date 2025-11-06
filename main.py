from fastapi import FastAPI
from configuration import settings
from routers import init_routes

application = FastAPI()
init_routes(application)


@application.get("/")
def index():
    return {"message":"application get route"}

@application.get("/api-configuration")
def api_configuration():
    return {"message":"Your API Configuration",
            "host":settings.APPLICATION_HOST,
            "port":settings.APPLICATION_PORT,
            "reload":settings.APPLICATION_RELOAD_FLAG,
            }