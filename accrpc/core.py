from colorama import Fore as color, init as colorama_init
from pypresence import Presence, exceptions as pexceptions
from subprocess import check_output, PIPE
from maps import Statics, Graphics, Physics
from ctypes import sizeof
from mmap import mmap
from constants import *
from datetime import datetime
from os import system
from time import sleep, time
from sys import exit

class Core:
    running = False
    acc_running = False
    acc_process = 'AC2-Win64-Shipping.exe'
    start_time = None
    presence = None
    attemps = 0

    def __init__(self, client_id: int):
        self.client_id = client_id
    
    def message(self, msg: str, type: str = 'info', log: bool = False, e:str = None) -> None:
        keys = {
            'success': (color.GREEN, 'V'),
            'error': (color.RED, 'X'),
            'info': (color.LIGHTCYAN_EX, '>'),
            'loading': (color.LIGHTBLUE_EX, '~')
        }
        type = keys[type]
        print(f'{color.WHITE}[{type[0]}{type[1]}{color.WHITE}] {msg}{color.RESET}')
        if log:
            self.write_log(f'{msg}: {e}')
    
    def write_log(self, msg: str) -> None:
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            file = open('log.txt', 'a', encoding='utf-8')
            file.write(f'[{time}] {msg}\n')
            file.close()
        except Exception:
            self.message('Error al manipular el archivo de registro', type='error')

    def acc_is_running(self):
        return True if check_output(f'wmic process where "name=\'{self.acc_process}\'" get ExecutablePath', universal_newlines=True, stderr=PIPE).strip() else False
    
    def init_settings(self):
        colorama_init()
        system('cls')
        system('title ' + TITLE)
    
    def header(self):
        print()
        self.message(TITLE)
        self.message('Autor: ' + AUTHOR)
        self.message('Github: ' + GITHUB)
        self.message('Version: ' + VERSION)
        print()

    def connect_rpc(self):
        if self.attemps >= 3:
            self.message('Se excedió el limite de re-conexión con Discord, cerrando programa', type='error', log=True)
            sleep(5)
            self.close()
        try:
            self.presence = Presence(self.client_id)
            self.presence.connect()
            self.message('Conectado a Discord correctamente', type='success')
        except Exception as e:
            self.message('Hubo un error al conectarse con Discord', type='error', log=True, e=e)
            self.message('Re-conectandose con Discord en 5s', type='loading')
            sleep(5)
            self.attemps += 1
            self.connect_rpc()

    def check_acc(self):
        self.message('Esperando ejecución de ' + GAME, type='loading')
        while not self.acc_running:
            self.acc_running = self.acc_is_running()
        self.message(GAME + ' encontrado', type='success')
        self.message('Conectandose con Discord', type='loading')
        self.connect_rpc()
    
    def get_physics(self):
        source = mmap(-1, sizeof(Physics), u"Local\\acpmf_physics")
        data = Physics.from_buffer(source)
        return data

    def get_statics(self):
        source = mmap(-1, sizeof(Statics), u"Local\\acpmf_static")
        data = Statics.from_buffer(source)
        return data
    
    def get_graphics(self):
        source = mmap(-1, sizeof(Graphics), u"Local\\acpmf_graphics")
        data = Graphics.from_buffer(source)
        return data

    def presence_handler(self):
        graphics = self.get_graphics()
        statics = self.get_statics()
        physics = self.get_physics()
        state = None
        details = STATUS[graphics.AC_STATUS]
        if graphics.AC_STATUS == 2:
            details = f'{SESSION[graphics.AC_SESSION_TYPE]} en {statics.track.capitalize()} ({RAIN[graphics.rainTypes]})'
            state = f'{CAR_MODEL[statics.carModel]}, {round(physics.speedKmh)} km/h'
            if graphics.isInPit:
                state += '(En los pits)'
        elif graphics.AC_STATUS == 3:
            details += f', {graphics.completedLaps} vueltas hechas'
        data = {
            'details': details,
            'state': state,
            'start': self.start_time
        }
        return data

    def update_presence(self):
        data = self.presence_handler()
        if not data:
            data = {
                'details': 'Offline',
                'start': self.start_time
            }
            
        self.presence.update(**data)
        
    def close(self):
        self.running = False
        exit()

    def main(self):
        self.start_time = time()
        while self.acc_running:
            self.acc_running =  self.acc_is_running()
            self.update_presence()
            sleep(15)
        self.message(f'{GAME} se ha cerrado, re-conectando', type='info')
        self.presence.clear()
        self.presence.close()
        self.check_acc()

    def run(self):
        try:
            self.init_settings()
            self.header()
            self.check_acc()
            self.main()
        except KeyboardInterrupt:
            self.message('Programa interrumpido por el usuario')
        
if __name__ == '__main__':
    accrpc = Core('')
    accrpc.run()
