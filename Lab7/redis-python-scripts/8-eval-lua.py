from redis import Redis

redis_connection = Redis(decode_responses=True)


script = """
return "test"
"""

print(redis_connection.eval(script, 0))