from redis import Redis

r = Redis(host="redis-myweblab.7e14.starter-us-west-2.openshiftapps.com", password='', port=6379)

r.set("Test","Test")

print(r.get("Test"))