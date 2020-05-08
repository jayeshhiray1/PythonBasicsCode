import redis
from redis.sentinel import Sentinel
sentinel = Sentinel([('192.168.10.1', 26379), ('192.168.10.2',26379), ('192.168.10.3',26379)], socket_timeout=0.1)

master = sentinel.master_for('master-name', socket_timeout=0.1)