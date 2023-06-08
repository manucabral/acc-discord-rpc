from pypresence import Presence, exceptions as pexceptions
from colorama import (
    Fore as color,
    init as colorama_init,
)  # TODO: use ansicolors instead!
from requests import get  # TODO: use httpx instead

from .maps import Statics, Graphics, Physics, Structure
from ctypes import sizeof
from mmap import mmap

from subprocess import check_output, PIPE
from datetime import datetime
from time import sleep, time
from os import system
from sys import exit

from .constants import *


class Core:
    running = False
    acc_running = False
    acc_process = "AC2-Win64-Shipping.exe"
    start_time = None
    presence = None
    attemps = 0
    start_time = None

    def __init__(self, client_id: int, lang: str):
        self.client_id = client_id
        self.lang = LANGUAGE[lang]

    def message(
        self, msg: str, type: str = "info", log: bool = False, e: str = None
    ) -> None:
        keys = {
            "success": (color.GREEN, "V"),
            "error": (color.RED, "X"),
            "warning": (color.LIGHTYELLOW_EX, "!"),
            "info": (color.LIGHTCYAN_EX, ">"),
            "loading": (color.LIGHTBLUE_EX, "~"),
        }
        type = keys[type]
        print(f"{color.WHITE}[{type[0]}{type[1]}{color.WHITE}] {msg}{color.RESET}")
        if log:
            self.write_log(f"{msg} {e if e else None}")

    def write_log(self, msg: str) -> None:
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            file = open("log.txt", "a+", encoding="utf-8")
            file.write(f"[{time}] {msg}\n")
            file.close()
        except Exception:
            self.message(ERROR[7][self.lang], type="error")

    def check_system_lang(self) -> None:
        self.message(MSG[2][self.lang], type="loading")
        lang = (
            check_output(
                "powershell get-uiculture", universal_newlines=True, stderr=PIPE
            )
            .split("\n")[3][17:]
            .split("           ")
        )
        system_lang = (lang[0], lang[1][1:])
        self.lang = LANGUAGE[system_lang[0][:2]]
        if not lang[0]:
            self.write_log(ERROR[1][self.lang], type="error", log=True)
            raise Exception(ERROR[1][self.lang])
        self.message(f"{MSG[3][self.lang]} {system_lang[1]}", type="success")

    def check_updates(self):
        self.message(MSG[15][self.lang], type="loading")
        res = get(REPO_URL)
        try:
            res.raise_for_status()
        except rexceptions.HTTPError as err:
            self.message(str(err), type="error")
            return
        versions = []
        for key in res.json():
            versions.append(key["tag_name"])
        if versions[0] != VERSION:
            self.message(f"{MSG[16][self.lang]}: {versions[0]}", type="warning")
        else:
            self.message(MSG[17][self.lang], type="success")

    def init_settings(self) -> None:
        colorama_init()
        system("cls")
        system("title " + TITLE)

    def header(self) -> None:
        print()
        self.message(TITLE)
        self.message(f"{MSG[0][self.lang]}: {AUTHOR}")
        self.message("Github: " + GITHUB)
        self.message("Version: " + VERSION)
        self.message(MSG[1][self.lang])
        print()

    def connect_rpc(self) -> None:
        if self.attemps >= 3:
            self.message(ERROR[2][self.lang], type="error", log=True)
            sleep(5)
            self.close()
        try:
            self.presence = Presence(self.client_id)
            self.presence.connect()
            self.message(MSG[7][self.lang], type="success")
        except Exception as e:
            self.message(ERROR[3][self.lang], type="error", log=True, e=e)
            self.message(ERROR[4][self.lang], type="loading")
            sleep(5)
            self.attemps += 1
            self.connect_rpc()

    def get_statics(self) -> Structure:
        source = mmap(-1, sizeof(Statics), TAGNAME["statics"])
        return Statics.from_buffer(source)

    def get_graphics(self) -> Structure:
        source = mmap(-1, sizeof(Graphics), TAGNAME["graphics"])
        return Graphics.from_buffer(source)

    def presence_handler(self) -> dict:
        graphics = self.get_graphics()
        statics = self.get_statics()
        small_image = small_text = state = None
        details = STATUS[graphics.AC_STATUS][self.lang]
        large_text = MSG[8][self.lang] if not statics.isOnline else MSG[9][self.lang]
        if graphics.AC_STATUS == 0:
            self.start_time = time()
        if graphics.AC_STATUS == 2:
            details = f'{SESSION[graphics.AC_SESSION_TYPE][self.lang]} {"in" if self.lang == 1 else "en"} {statics.track.capitalize()} ({RAIN[graphics.rainTypes][self.lang]})'
            state = f"{MSG[10][self.lang]} {graphics.currentTime}, {MSG[11][self.lang]} {graphics.position}/{graphics.activeCars}"
            small_image = CAR_MODEL[statics.carModel][1]
            small_text = CAR_MODEL[statics.carModel][0]
            if graphics.isInPit:
                state += MSG[12][self.lang]
        elif graphics.AC_STATUS == 3:
            details += f", {graphics.completedLaps} {MSG[13][self.lang]}"
        if graphics.isSetupMenuVisible:
            state = {MSG[14][self.lang]}
        data = {
            "details": details,
            "state": state,
            "start": self.start_time,
            "large_image": "logo",
            "large_text": large_text,
            "small_image": small_image,
            "small_text": small_text,
        }
        return data

    def check_acc(self) -> None:
        self.message(MSG[4][self.lang], type="loading")
        while not self.acc_running:
            self.acc_running = self.acc_is_running()
        self.message(MSG[5][self.lang], type="success")
        self.message(MSG[6][self.lang], type="loading")
        self.connect_rpc()

    def update_presence(self) -> None:
        data = self.presence_handler()
        if not data:
            data = {
                "details": "Offline",
            }
        self.presence.update(**data)

    def acc_is_running(self) -> bool:
        return (
            True
            if check_output(
                f"wmic process where \"name='{self.acc_process}'\" get ExecutablePath",
                universal_newlines=True,
                stderr=PIPE,
            ).strip()
            else False
        )

    def main(self) -> None:
        self.start_time = time()
        while self.acc_running:
            self.acc_running = self.acc_is_running()
            self.update_presence()
            sleep(15)
        self.message(ERROR[5][self.lang], type="error")
        self.presence.clear()
        self.run()

    def run(self) -> None:
        try:
            if not self.running:
                self.init_settings()
                self.header()
                self.check_system_lang()
                self.check_updates()
                self.running = True
            self.check_acc()
            self.main()
        except KeyboardInterrupt:
            self.message(ERROR[0][self.lang])
            sleep(3)
            self.close()

    def close(self) -> None:
        self.running = False
        exit()
