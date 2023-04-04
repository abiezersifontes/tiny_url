"""Routes for Url"""
from fastapi.routing import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from service.app.infrastructure.schema import UrlData
from service.app.application.service_url import ServiceUrl
from service.app.infrastructure.repositories.zookeeper_repo import ZookeeperRepo
from service.app.infrastructure.repositories.redis import RedisRepo
from service.app.infrastructure.repositories.mongo_db import MongoDB

router = APIRouter()


@router.post("/url")
async def create_url(body: UrlData):
    """create a short url for the long one and save them at the db"""
    # call the the service function
    url = ServiceUrl(conf_repository=ZookeeperRepo(), store=MongoDB(), cache=RedisRepo()).generate_url(url=str(body.url))
    # return new url created
    return JSONResponse({"tiny_url": url}, 201)


@router.get("/url/{url_str}")
async def get_url(url_str):
    """Return a redirect response 307"""
    res = await ServiceUrl(
        conf_repository=ZookeeperRepo(), store=MongoDB(), cache=RedisRepo()
    ).get_url(url_str=url_str)
    if res:
        return RedirectResponse(res)
    return HTMLResponse("<h1>There is no Url<h1>")



@router.delete("/url/{url_str}")
async def delete_url(url_str):
    """delete the record in the database for the previusly created url"""
    res = ServiceUrl(
        conf_repository=ZookeeperRepo(), store=MongoDB(), cache=RedisRepo()
    ).delete_url(url_str=url_str)

    return JSONResponse({"deleted":res})
