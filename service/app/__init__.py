"""Create the app Instance"""
from fastapi import FastAPI, BackgroundTasks
from service.app.infrastructure.cron import delete_old_urls

def create_app() -> FastAPI:
    """Create the app instance"""
    from service.app.infrastructure.router import router

    app: FastAPI = FastAPI()

    @app.on_event("startup")
    async def startup_event():
        background_tasks = BackgroundTasks()
        background_tasks.add_task(delete_old_urls)
        await background_tasks()

    app.include_router(router)

    return app
