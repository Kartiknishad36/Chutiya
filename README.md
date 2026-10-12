# 👑 King Userbot (Chutiya)

Single-file style Telegram **manager bot + userbot** (Pyrogram).

## Files

| File | Role |
|------|------|
| `king.py` | Bootstrap — loads original body + injects pack |
| `king_pack.py` | **200+** detail pack (fullinfo, system, mod, tools, arts) |
| `requirements.txt` | Dependencies |
| `.env` | Config (do not commit secrets publicly) |

## New commands (after `/add` session)

**System:** `.ping` `.alive` `.id` `.uptime` `.help`  
**Arts:** `.moon` `.heart` `.ok` `.vip` `.boss` `.pro` `.king` `.win` `.gg` `.hi` `.bye` `.star` `.fire` `.crown` (+ old anims)  
**Info:** `.info` `.fullinfo` (200+ Telegram fields)  
**Mod:** `.ban` `.unban` `.kick` `.mute` `.unmute` `.promote` `.demote` `.pin` `.unpin` `.del`  
**Tools:** `.calc` `.time` `.weather` `.tr`  
**Classic:** `.clone` `.back` `.tagall` `.anysnap` `.allban` `.end` `.stop` …

## Setup

```bash
pip install -r requirements.txt
# set API_ID API_HASH BOT_TOKEN OWNER_ID FORCE_* in .env
python king.py
```

Bot DM: `/start` → `/add` → paste **STRING_SESSION** → userbot commands on your account.

## Legal

`.fullinfo` uses **public Telegram fields only**. No Aadhaar / home address / KYC.
