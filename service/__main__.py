"""Start the Service"""
import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "service:deploy_local_app",
        reload=True,
        factory=True,
        access_log=True,
        use_colors=True
    )
