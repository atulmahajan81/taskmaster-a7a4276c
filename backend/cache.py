import redis

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value, ttl=300):
        self.client.setex(key, ttl, value)

    def delete(self, key):
        self.client.delete(key)

    def invalidate(self, pattern):
        for key in self.client.scan_iter(pattern):
            self.delete(key)