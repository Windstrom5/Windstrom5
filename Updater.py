import re
import subprocess
from typing import Tuple
from datetime import date

def discord() -> Tuple[str, str]:
    COMMAND_ARGS = ["node", "DiscordUpdater.js"]
    p = subprocess.Popen(args=COMMAND_ARGS, stdout=subprocess.PIPE)
    print(p.communicate()[0].decode())
    p.stdout.close()
def steam() -> Tuple[str, str]:
    COMMAND_ARGS = ["node", "SteamUpdater.js"]
    p = subprocess.Popen(args=COMMAND_ARGS, stdout=subprocess.PIPE)
    print(p.communicate()[0].decode())
    p.stdout.close()
if __name__ == '__main__':
    discord()
    steam()
