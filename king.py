# Auto-expand embedded king body from kb64_*.txt then run
import base64, pathlib, runpy
_base = pathlib.Path(__file__).resolve().parent
parts = sorted(_base.glob("kb64_*.txt"), key=lambda p: p.name)
if not parts:
    raise SystemExit("kb64_*.txt missing — pull full repo")
b64 = "".join(p.read_text() for p in parts)
code = base64.b64decode(b64)
tmp = _base / "_king_runtime.py"
tmp.write_bytes(code)
try:
    runpy.run_path(str(tmp), run_name="__main__")
finally:
    try:
        tmp.unlink()
    except Exception:
        pass
