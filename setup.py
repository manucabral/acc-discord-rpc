import sys
from accrpc import __title__, __version__, __author__
from cx_Freeze import setup, Executable


setup(
    name=__title__,
    version=__version__,
    description="A simple Asseto Corsa Competizione RPC",
    author=__author__,
    options={"build_exe": {"excludes": ["tkinter", "unittest"]}},
    executables=[
        Executable(
            "main.py",
            copyright="© 2021 - 2023 by " + __author__ + " - All rights reserved",
            icon="accrpc/assets/logo.ico",
            target_name="Assetto Corsa Competizione RPC.exe",
            shortcut_name="Assetto Corsa Competizione RPC",
        )
    ],
)
