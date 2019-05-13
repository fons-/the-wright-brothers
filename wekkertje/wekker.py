import subprocess
import time
from checker import check
from morse import play_text, lampuit


def refresh_git(also_do_hard_reset=True):
    if also_do_hard_reset:
        subprocess.call("git reset --hard", shell=True, stdout=subprocess.PIPE, cwd="..")
    subprocess.call("git pull", shell=True, stdout=subprocess.PIPE, cwd="..")


if __name__ == "__main__":
    while True:
        refresh_git()
        if check():
            lampuit()
            # 1 minuutje wachten tot de volgende pull
            # te vaak pullen wordt misschien geblokkeerd
            time.sleep(60)
        else:
            with open("geheimwoordje.txt") as f:
                geheimwoordje_text = f.readline()
            play_text(geheimwoordje_text)
            lampuit()
