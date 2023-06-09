"""Start the Service"""
import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "service:deploy_local_app",
        reload=False,
        factory=True,
        access_log=True,
        use_colors=True,
        port=8000
    )
