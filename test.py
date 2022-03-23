import requests
from bs4 import BeautifulSoup as BS
from proxies import proxy
import json

url = requests.get("https://entrar.in/login/login", proxies=proxy, timeout=5)
soup = BS(url.content, features="html.parser")
soup = soup.find("div", {"class": "col-lg-3 col-sm-3"})
captcha = soup.text.replace(" =", "")
captcha = eval(captcha)

with requests.Session() as r:
    payload = {"username": "B/14155", "password": "pratham03", "captcha": captcha}
    login = r.post("https://entrar.in/login/login", headers=payload, proxies=proxy, timeout=5)
    req = r.get(
        "https://entrar.in/classroom_creation_crm_new/s_display",
        headers=payload,
        proxies=proxy,
        timeout=5,
    )
    print(req.url)
