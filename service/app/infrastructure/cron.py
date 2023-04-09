from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from service.app.infrastructure.repositories.urls_mongo import UrlsMongo
from service.app.infrastructure.repositories.zookeeper_repo import ZookeeperRepo

async def delete_old_urls():
    # Connect to the MongoDB and Zookeeper repositories
    mongo = UrlsMongo()
    zk = ZookeeperRepo()

    # Calculate the date one year ago
    one_year_ago = datetime.utcnow() - timedelta(days=365)

    # Delete the old URLs from the MongoDB repository
    mongo.collection.delete_many({'created': {'$lt': one_year_ago}})

    # Reset the counter in the Zookeeper repository if possible
    current_start, current_end = zk.get_range()
    if current_start >= 7812425:
        new_start = 0
        new_end = 7812425
        zk.set_range(new_start, new_end)

def schedule_cron_job():
    # Create a new scheduler and add the cron job
    scheduler = AsyncIOScheduler()
    scheduler.add_job(delete_old_urls, 'interval', days=365)

    # Start the scheduler
    scheduler.start()