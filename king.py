"""
King Manager bootstrap
1) Load original single-file bot body (cached as _king_body.py)
2) Inject king_pack.py (200+ fullinfo + system/mod/tools/arts)
3) Register extra handlers on session connect
"""
import pathlib
import re
import runpy
import urllib.request

_BASE = pathlib.Path(__file__).resolve().parent
_BODY = _BASE / "_king_body.py"
_PACK = _BASE / "king_pack.py"

# Original known-good single-file bot (before accidental overwrite)
_ORIG_URL = (
    "https://raw.githubusercontent.com/Kartiknishad36/Chutiya/"
    "fb7c1d51e81611aadab1da42f30b67c39f82589c/king.py"
)


def _ensure_body():
    if _BODY.exists() and _BODY.stat().st_size > 10000:
        return
    print("[king] downloading original body…")
    with urllib.request.urlopen(_ORIG_URL, timeout=60) as r:
        data = r.read()
    _BODY.write_bytes(data)
    print(f"[king] body saved {_BODY} ({len(data)} bytes)")


def _inject_pack(src: str) -> str:
    """Inject pack loader + expanded handler registration into source."""
    loader = '''
# ==================== LOAD PREMIUM PACK (200+) ====================
import pathlib as _pathlib
_pack_path = _pathlib.Path(__file__).with_name("king_pack.py")
if not _pack_path.exists():
    _pack_path = _pathlib.Path("_king_body.py").resolve().parent / "king_pack.py"
if _pack_path.exists():
    try:
        exec(compile(_pack_path.read_text(encoding="utf-8"), str(_pack_path), "exec"), globals())
        print("[king] king_pack.py loaded — 200+ features ON")
    except Exception as _e:
        print(f"[king] pack load fail: {_e}")
else:
    print("[king] king_pack.py missing")

'''
    marker = "# ==================== MAIN BOT LOGIC ===================="
    if marker in src and "king_pack.py loaded" not in src:
        src = src.replace(marker, loader + marker, 1)

    old = '''        new_user.add_handler(MessageHandler(help_handler, filters.command("help", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(cat_handler, filters.command("cat", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(rose_handler, filters.command("rose", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(hacker_handler, filters.command("hacker", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(error_handler, filters.command("error", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(fuck_handler, filters.command("fuck", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(butterfly_handler, filters.command("butterfly", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(love_handler, filters.command("love", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(yourmom_handler, filters.command("yourmom", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(myson_handler, filters.command("myson", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(info_cmd, filters.command("info", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(clone_cmd, filters.command("clone", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(back_cmd, filters.command("back", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(anysnap_cmd, filters.command("anysnap", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(aanysnap_cmd, filters.command("aanysnap", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(tagall_cmd, filters.command("tagall", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(allban_cmd, filters.command("allban", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(fastallban_cmd, filters.command("fastallban", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(end_cmd, filters.command("end", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(stop_cmd, filters.command("stop", prefixes=".") & filters.me))

        new_user.add_handler(MessageHandler(auto_reply_listener, filters.incoming & ~filters.me))
'''

    new = '''        new_user.add_handler(MessageHandler(help_handler, filters.command(["help", "menu"], prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(ping_cmd, filters.command("ping", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(alive_cmd, filters.command("alive", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(id_cmd, filters.command("id", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(uptime_cmd, filters.command("uptime", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(cat_handler, filters.command("cat", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(rose_handler, filters.command("rose", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(hacker_handler, filters.command("hacker", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(error_handler, filters.command("error", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(fuck_handler, filters.command("fuck", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(butterfly_handler, filters.command("butterfly", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(love_handler, filters.command("love", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(yourmom_handler, filters.command("yourmom", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(myson_handler, filters.command("myson", prefixes=".") & filters.me))
        for _art in ("moon", "heart", "ok", "vip", "boss", "pro", "king", "win", "gg", "hi", "bye", "star", "fire", "crown"):
            new_user.add_handler(MessageHandler(art_generic_cmd, filters.command(_art, prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(info_cmd, filters.command(["info", "whois"], prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(fullinfo_cmd, filters.command(["fullinfo", "userinfo"], prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(clone_cmd, filters.command("clone", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(back_cmd, filters.command("back", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(anysnap_cmd, filters.command("anysnap", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(aanysnap_cmd, filters.command("aanysnap", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(tagall_cmd, filters.command("tagall", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(allban_cmd, filters.command("allban", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(fastallban_cmd, filters.command("fastallban", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(end_cmd, filters.command("end", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(stop_cmd, filters.command("stop", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(ban_cmd, filters.command("ban", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(unban_cmd, filters.command("unban", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(kick_cmd, filters.command("kick", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(mute_cmd, filters.command("mute", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(unmute_cmd, filters.command("unmute", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(pin_cmd, filters.command("pin", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(unpin_cmd, filters.command("unpin", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(del_cmd, filters.command(["del", "delete"], prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(promote_cmd, filters.command("promote", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(demote_cmd, filters.command("demote", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(calc_cmd, filters.command(["calc", "calculate"], prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(time_cmd, filters.command(["time", "date"], prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(weather_cmd, filters.command("weather", prefixes=".") & filters.me))
        new_user.add_handler(MessageHandler(tr_cmd, filters.command(["tr", "translate"], prefixes=".") & filters.me))

        new_user.add_handler(MessageHandler(auto_reply_listener, filters.incoming & ~filters.me))
'''
    if old in src:
        src = src.replace(old, new)
    return src


def main():
    _ensure_body()
    src = _BODY.read_text(encoding="utf-8", errors="replace")
    src = _inject_pack(src)
    # Write runtime next to pack so Path(__file__) for pack resolves
    runtime = _BASE / "_king_runtime.py"
    runtime.write_text(src, encoding="utf-8")
    print("[king] starting runtime…")
    try:
        runpy.run_path(str(runtime), run_name="__main__")
    finally:
        try:
            runtime.unlink()
        except Exception:
            pass


if __name__ == "__main__":
    main()
