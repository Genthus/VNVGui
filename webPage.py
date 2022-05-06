import eel

eel.init("web")

@eel.expose
def holi():
    print("holi")
    return "holi"

eel.start("index.html")