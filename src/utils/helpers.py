from pathlib import Path
from functools import lru_cache

import tomli


@lru_cache()
def load_config():
    path = Path("src/config/config.toml")
    with path.open("rb") as fp:
        data = tomli.load(fp)

    return data
