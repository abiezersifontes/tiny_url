import os
import time
from kazoo.client import KazooClient
from kazoo.exceptions import NodeExistsError, NoNodeError


if __name__ == "__main__":
    if hosts := os.getenv("ZOOKEEPER_HOSTS", None):
        # Connect to ZooKeeper
        zk = KazooClient(hosts=hosts)
        while True:
            try:
                zk.start()
                break
            except:
                print("Waiting for ZooKeeper to start...")
                time.sleep(1)

        # Define the path and value
        path = '/tinyurls/chunk0'
        value = b'{"start": 0, "end": 1000000}'

        # Create the parent path if it doesn't exist
        try:
            zk.ensure_path('/tinyurls')
        except NodeExistsError:
            pass

        # Create the path if it doesn't exist and set the value
        try:
            zk.create(path, value)
        except NodeExistsError:
            # The path already exists, so just set the value
            zk.set(path, value)
        except NoNodeError:
            # The parent path does not exist, so create it and then create the path
            zk.ensure_path('/tinyurls')
            zk.create(path, value)

        # Close the connection to ZooKeeper
        zk.stop()
