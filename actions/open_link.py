import webbrowser


def run(url=None, **kwargs):
    if url:
        webbrowser.open(url)
        print("[Action] Abrindo link:", url)
