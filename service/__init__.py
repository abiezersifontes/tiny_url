"""Deploy the Service"""
from fastapi import FastAPI


def deploy_local_app() -> FastAPI:
    """Deploy the Service"""

    from service.app import create_app
    app: FastAPI = create_app()

    return app
