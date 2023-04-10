from datetime import datetime, timedelta
from service.app.infrastructure.repositories.urls_mongo import UrlsMongo
from service.app.infrastructure.repositories.zookeeper_repo import ZookeeperRepo

async def delete_old_urls():
    """
    Delete the old URLs from the MongoDB repository
    and reset the counter in the Zookeeper repository if possible
    """
    # Connect to the MongoDB and Zookeeper repositories
    mongo = UrlsMongo()
    zk = ZookeeperRepo()

    # Calculate the date one year ago
    one_year_ago = datetime.utcnow() - timedelta(seconds=10)

    # Delete the old URLs from the MongoDB repository
    mongo.collection.delete_many({'created': {'$lt': one_year_ago}})

    # Reset the counter in the Zookeeper repository if possible
    current_start, current_end = zk.get_range()
    if current_start >= current_end:
        new_start = 0
        new_end = current_end
        zk.set_range(new_start, new_end)
