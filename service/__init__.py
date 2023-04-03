"""Deploy the Service"""
import os
from fastapi import FastAPI


def deploy_local_app() -> FastAPI:
    """Deploy the Service"""
    os.putenv("SERVICE_DEPLOY__MODE", "local")

    from service.app import create_app
    app: FastAPI = create_app()

    return app
