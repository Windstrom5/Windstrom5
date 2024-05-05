import re
import subprocess
from typing import Tuple
from datetime import date

def generate_card() -> Tuple[str, str]:
    COMMAND_ARGS = ["node", "generate.js"]
    p = subprocess.Popen(args=COMMAND_ARGS, stdout=subprocess.PIPE)
    print(p.communicate()[0].decode())
    p.stdout.close()

if __name__ == '__main__':
    generate_card()
