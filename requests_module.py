import requests

# r = requests.get("https://xkcd.com/353/")

# print(r.text)

# r= requests.get("https://imgs.xkcd.com/comics/python.png")



# with open("..\comic.png","wb") as f:
#     f.write(r.content)



# print(r.status_code)
#print(r.ok)

# print(r.headers)
# payload = {
#     "page":2,
#     "count":25

# }
# r= requests.get("https://httpbin.org/get",params=payload)

# print(r.text)
# print(r.url)

# payload = {
#     "username":"corey",
#     "password":"testing"

# }
# r= requests.post("https://httpbin.org/post",data=payload)

# # print(r.text)
# # print(r.url)

# r_dict = r.json()
# print(r_dict["form"])

# r= requests.get("https://httpbin.org/basic-auth/corey/testing", auth=("corey","testing"))

r = requests.get("https://httpbin.org/delay/6",timeout=3)

print(r)
