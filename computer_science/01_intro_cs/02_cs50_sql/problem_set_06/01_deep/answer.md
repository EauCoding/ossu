# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

Here are the reasons to adopt this approach is that it allows the data to be evenly distributed meaning no single boat will be overwhelmed. The reason not to adopt this approach is because the reading time scale with the number of boat which increase the time to read from the data.

## Partitioning by Hour

Adopting this approach will reduce reading time for time specifying querying. However, this approach means that one boat will have more data than others which means that it could run out of space to store all the data.

## Partitioning by Hash Value

Adopting this approach will reduce the time for querying a specific observation and reduce the likelihood of a boat running out of space because the observations are evenly distributed. However, it will still create a problem of increase reading time when looking for a range of observation because the query has to be sent to all the boats.
