# king_commands.py — extra 200+ commands (loaded by king.py, nothing deleted from original)
# Requires: smart_edit, draw_art, OWNER_ID, time, re, datetime, urllib, json in globals
# ==================== EXTRA ARTS + 200+ COMMANDS PACK (ADDED — NOTHING REMOVED) ====================
_START_TS = time.time()

def _uptime():
    s = int(time.time() - _START_TS)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h}h {m}m {s}s"

MOON_ART = "    *  .  *\n  .    *   .\n     (  )\n  *   )(   *\n .   (  )  .\n      )("
HEART_ART = "  **  **\n ****** \n  ****  \n   **   "
OK_ART = "  ___  _  __\n / _ \\| |/ /\n| |_| |   <\n \\___/|_|\\_\\"
VIP_ART = " __     _____ _____\n \\ \\   / /_ _|  _ \\\n  \\ \\ / / | || |_) |\n   \\ V /  | ||  __/\n    \\_/  |___|_|