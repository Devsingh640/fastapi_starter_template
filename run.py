import uvicorn
from configuration import settings


if __name__=="__main__":
    try:

        uvicorn.run(app="main:application",
                    host=settings.APPLICATION_HOST,
                    port=settings.APPLICATION_PORT,
                    reload=settings.APPLICATION_RELOAD_FLAG)


    except Exception as error:
        print("ERROR: ",error)

