# Aproach
Create a service that create a unique character base on a counter that iterate adding one in every call the idea is codify that character between a range keep that range in a key-value service as Zookeeper and use Redis to do get the redireccion faster.

the service has an stimation of 50.000 request per second if a day which has 86.400 seconds, then we would have 4.320.000.000 requests per day, if we multiply by 365 days we would get 1.576.800.000.000 per year. in five years we would have 7.884.000.000.000

In order to catch that we plan to use a combination of 78 posible characters with a long of 7 characters 
that would be 17.565.568.854.912 more than the double that we could get in 5 years with our stimated requests

The service has cron to delete the date expired urls, and reset the counter. Regarding the Cache every url is caches for 1 hour.

# Install
```docker-compose up --build```

# Follow ups
1. add stadistics
2. make the redireccion awnser faster
3. delete could be async