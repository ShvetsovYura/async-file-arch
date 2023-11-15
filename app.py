import subprocess
from pathlib import Path

from src import utils

if __name__ == "__main__":
    p = subprocess.Popen(
        ["zip", "-rq", "-", ".venv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, _ = p.communicate()
    utils.save_to_file(stdout, Path(__file__).parent.resolve().joinpath("archive.zip"))
