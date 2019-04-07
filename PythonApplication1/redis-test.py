from redis import Redis

r = Redis  (host="redis-test-2.7e14.starter-us-west-2.openshiftapps.com", password='BFH1Q3spMuVYG7Ag')

r.set("Test","Test")

print(r.get("Test"))