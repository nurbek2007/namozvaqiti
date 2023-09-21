from bs4 import BeautifulSoup
from PrayRequest import PrayRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup


class :
    def __init__(self, con:str) -> None:
        self.html = con
        self.__data = {
            "Tong":None,
            "Quyosh":None,
            "Peshin":None,
            "Asr":None,
            "Shom":None,
            "Xufton":None
        }
    
    def scrapping(self):
        b = BeautifulSoup(self.__html, "html.parser")
        all_pr_times = b.find_all("div", class_="prayer-times")

if __name__ == "__main__":
    pr = PrayRequest("Farg'ona")
    pr.request()
    pt = praytime(pr.Content)
    pt.scrapping()