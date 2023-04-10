# Aproach
Create a service that creates a unique character base on a counter that iterates adding one in every call the idea is to codify that character between a range keep that range in a key-value service as Zookeeper and use Redis to get the redirection faster.

the service has an estimation of 50.000 requests per second if a day has 86.400 seconds, then we would have 4.320.000.000 requests per day, if we multiply by 365 days we will get 1.576.800.000.000 per year. in five years we would have 7.884.000.000.000

To catch that we plan to use a combination of 78 possible characters with a long of 7 characters 
that would be 17.565.568.854.912 more than the double that we could get in 5 years with our estimated requests

The service has cron to delete the date expired urls, and reset the counter. Regarding the Cache, every url is cached for 1 hour.

the next is a quick diagram of the service https://sketchboard.me/xDKbxDlfzIy#/ is important to say that every one of the services could be scaled to get more performance

# Install

As the service is dockerized you only need to have docker and docker-compose installed as a prerequisite

```docker-compose up --build```

