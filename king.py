"""Restore original King Manager bot body from last known-good commit."""
import pathlib
import runpy
import urllib.request

_BASE = pathlib.Path(__file__).resolve().parent
_BODY = _BASE / "_king_body.py"
_ORIG_URL = (
    "https://raw.githubusercontent.com/Kartiknishad36/Chutiya/"
    "fb7c1d51e81611aadab1da42f30b67c39f82589c/king.py"
)


def main():
    if not _BODY.exists() or _BODY.stat().st_size < 10000:
        print("[king] restoring original body…")
        with urllib.request.urlopen(_ORIG_URL, timeout=60) as r:
            data = r.read()
        _BODY.write_bytes(data)
        print(f"[king] restored {len(data)} bytes")
    runpy.run_path(str(_BODY), run_name="__main__")


if __name__ == "__main__":
    main()
