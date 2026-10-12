# King Manager — loads king_p1.py + king_p2.py then runs
import pathlib, runpy

_base = pathlib.Path(__file__).resolve().parent
_p1 = _base / "king_p1.py"
_p2 = _base / "king_p2.py"
if not _p1.exists() or not _p2.exists():
    raise SystemExit("Missing king_p1.py / king_p2.py")

_code = _p1.read_text(encoding="utf-8") + _p2.read_text(encoding="utf-8")
_tmp = _base / "_king_runtime.py"
_tmp.write_text(_code, encoding="utf-8")
try:
    runpy.run_path(str(_tmp), run_name="__main__")
finally:
    try:
        _tmp.unlink()
    except Exception:
        pass
