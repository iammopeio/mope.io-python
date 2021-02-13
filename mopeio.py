from cefpython3 import cefpython as cef
import platform
import sys

URL = "https://mope.io" 

def create_browser(cef, settings):
    browser = cef.CreateBrowserSync(settings=settings,
                                    url=URL)
    browser.SendFocusEvent(True)
    browser.WasResized()

def main():

    settings = {
        "background_color": 0x00,
    }
    switches = {}
    browser_settings = {}
    sys.excepthook = cef.ExceptHook  
    cef.Initialize(settings=settings, switches=switches)
    create_browser(cef, browser_settings)
    cef.MessageLoop()
    cef.Shutdown()

if __name__ == '__main__':
    main()
