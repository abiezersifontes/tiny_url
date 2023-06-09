"""Routes for Url"""
import asyncio
from fastapi.routing import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from service.app.infrastructure.schema import UrlData
from service.app.application.service_url import ServiceUrl
from service.app.infrastructure.repositories.zookeeper_repo import ZookeeperRepo
from service.app.infrastructure.repositories.redis import RedisRepo
from service.app.infrastructure.repositories.urls_mongo import UrlsMongo
from service.app.infrastructure.repositories.stats_mongo import StatsRepository

router = APIRouter()


@router.post("/")
async def create_url(body: UrlData):
    """create a short url for the long one and save them at the db"""
    # call the the service function
    url = await ServiceUrl(conf_repository=ZookeeperRepo(), store=UrlsMongo(), cache=RedisRepo()).generate_url(url=str(body.url))
    # return new url created
    return JSONResponse({"tiny_url": url}, 201)


@router.get("/{url_str}")
async def get_url(url_str):
    """Return a redirect response 307"""
    stats = StatsRepository()
    res = await ServiceUrl(
        conf_repository=ZookeeperRepo(), store=UrlsMongo(), cache=RedisRepo()
    ).get_url(url_str=url_str)
    if res:
        asyncio.create_task(stats.add_hit(url_str, 200))
        return RedirectResponse(res)
    asyncio.create_task(stats.add_miss(url_str, 400))
    return HTMLResponse("<h1>There is no Url<h1>")



@router.delete("/{url_str}")
async def delete_url(url_str):
    """delete the record in the database for the previusly created url"""
    res = await ServiceUrl(
        conf_repository=ZookeeperRepo(), store=UrlsMongo(), cache=RedisRepo()
    ).delete_url(url_str=url_str)

    return JSONResponse({"deleted":res})

@router.get("/stats/all")
async def get_stats():
    """Return the stats of the service"""
    stats = StatsRepository()
    return JSONResponse(await stats.get_stats())
