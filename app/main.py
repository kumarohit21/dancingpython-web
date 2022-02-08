from sys import prefix
from webbrowser import get
from api.api import api_router
from fastapi import FastAPI
from tags import tag_dict
import uvicorn

def get_application():
    application = FastAPI(
        title = "Employee-APP",
        version="0.0.1-SNAPSHOT",
        openapi_tags=tag_dict,
        docs_url="/empapp/docs",
        openapi_url="/empapp/openapi.json"
    )
    application.include_router(api_router, prefix="/empapp")
    return application

application = get_application()

if __name__ == "__main__":
    uvicorn.run("main:application", host="127.0.0.1", port=5000, log_level="info")