"""Create the app Instance"""
from fastapi import FastAPI
from service.app.infrastructure.cron import schedule_cron_job

def create_app() -> FastAPI:
    """Create the app instance"""
    from service.app.infrastructure.router import router

    app: FastAPI = FastAPI()

    app.include_router(router)

    schedule_cron_job()

    return app
