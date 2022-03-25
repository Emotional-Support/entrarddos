import dotenv
import requests
from bs4 import BeautifulSoup as BS
import os
import dotenv

dotenv.load_dotenv()
USER = os.getenv("USER")
PASS = os.getenv("PASS")

url = requests.get("https://entrar.in/login/login")
soup = BS(url.content, features="html.parser")
soup = soup.find("div", {"class": "col-lg-3 col-sm-3"})
captcha = soup.text.replace(" =", "")
captcha = eval(captcha)

payload = {"username": USER, "password": PASS, "captcha": str(captcha)}
token = {"sessionToken": "4zx6sbbsjh7xsz0y"}

with requests.Session() as r:
    login = r.post("https://entrar.in/login/auth", data=payload)
    cookie = login.cookies
    cookie = cookie["PHPSESSID"]
    print("Request Sent to ------->", login.url, "-", login.elapsed.total_seconds(), "ms")

    req = r.get("https://entrar.in/parent_portal/myprofile", cookies=cookie)
    print(req.url)
