import requests 
def webcall(url, param):
    return requests.posts(url,data=param)

resp = webcall("https://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python","")
print resp
