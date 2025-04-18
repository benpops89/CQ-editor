import os, sys, asyncio
import faulthandler
import spyder.utils.icon_manager as icon_manager

if getattr(sys, "frozen", False):
    # You're running a PyInstaller binary
    bundled_fonts_path = os.path.join(sys._MEIPASS, "spyder", "fonts")
    icon_manager.ima._resource["directory"] = bundled_fonts_path

faulthandler.enable()

if "CASROOT" in os.environ:
    del os.environ["CASROOT"]

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from cq_editor.__main__ import main


if __name__ == "__main__":
    main()
