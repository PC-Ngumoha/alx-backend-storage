# Redis

## Useful Points

- _Redis_ is a lightning-fast _key-value_ store (form of storage) which can be used for practically anything at all.

- _redis-py_ is a client library which enables you to work with Redis within Python. There are other such libraries for working with Redis in Python.

- port _6379_ is the port used for routing all redis-related communications.

- _Redis_ stands for _REmote DIctionary Service_

- Redis keys are always of the string data type, but values may be a number of different data types (strings, lists, hashes, sets e.t.c.)

- _RESP_ stands for _REdis Serialization Protocol_

- _Redis Pipelining_ is a practice/process which enables us to reduce the number of round-trip transactions that we need in order write or read data from our redis server. Essentially, it enables us to buffer all the transactions on the client side and then send all at once to the server.

- _transaction blocks_

- _Optimistic locking_

- We can't obtain real-time results for commands that are inserted into a transactional pipeline.

- A Redis DB file (RDB) _Snapshot_ is full (rather than incremental) point-in-time capture of the database.

## Useful Links

- [Youtube: Redis crash course By Traversy Media](https://www.youtube.com/watch?v=Hbt56gFj998)

- [How to use Redis with Python](https://realpython.com/python-redis/)

- [Redis commands list on the Redis page](https://redis.io/commands/)

- [redis-py documentation](https://redis-py.readthedocs.io/en/stable/)