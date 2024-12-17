import traceback
import datetime

def log(e):
    exc = traceback.format_exc()
    print(
        "\n***************************************\n", 
        "Error:", exc, "\nDate:", datetime.datetime.now(),
        "\n\nDetails:", "\n--------\n", exc,
        "\n***************************************\n"
    )