import platform
from accrpc import Core

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("This program only works on Windows")
        input("Press any key to exit...")
        exit()
    app = Core(0, "en")
    app.run()
