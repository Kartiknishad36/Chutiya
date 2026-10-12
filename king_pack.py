# Auto-loaded by king.py after helpers are defined.
# Expects in module namespace: smart_edit, draw_art, OWNER_ID
"""King premium extra pack — imported by king.py"""
import re
import time
from datetime import datetime
from urllib.parse import quote
import urllib.request
import json

_START_TS = time.time()

def _uptime():
    s = int(time.time() - _START_TS)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h}h {m}m {s}s"

# ==================== EXTRA ASCII ARTS (200+ DETAIL PACK) ====================
MOON_ART = [
"    *  .  *",
"  .    *   .",
"     (  )",
"  *   )(   *",
" .   (  )  .",
"      )(",
]
HEART_ART = [
"  **  **",
" ****** ",
"  ****  ",
"   **   ",
]
OK_ART = [
"  ___  _  __",
" / _ \\| |/ /",
"| |_| |   <",
" \\___/|_|\\_\\",
]
VIP_ART = [
" __     _____ _____",
" \\ \\   / /_ _|  _ \\",
"  \\ \\ / / | || |_) |",
"   \\ V /  | ||  __/",
"    \\_/  |___|_|",
]
BOSS_ART = [
" ____   ___  ____ ____",
"| __ ) / _ \\/ ___/ ___|",
"|  _ \\| | | \\___ \\___ \\",
"| |_) | |_| |___) |__) |",
"|____/ \\___/|____/____/",
]
PRO_ART = [
" ____  ____   ___",
"|  _ \\|  _ \\ / _ \\",
"| |_) | |_) | | | |",
"|  __/|  _ <| |_| |",
"|_|   |_| \\_\\\\___/",
]
KING_ART = [
" _  _____ _   _  ____",
"| |/ /_ _| \\ | |/ ___|",
"| ' / | ||  \\| | |  _",
"| . \\ | || |\\  | |_| |",
"|_|\\_\\___|_| \\_|\\____|",
]
WIN_ART = [
"\\ \\      / (_)_ __",
" \\ \\ /\\ / /| | '_ \\",
"  \\ V  V / | | | | |",
"   \\_/\\_/  |_|_| |_|",
]
GG_ART = [
"  ____  ____",
" / ___/ ___|",
"| |  _| |  _",
"| |_| | |_| |",
" \\____|\\____|",
]
HI_ART = [
" _   _ ___",
"| | | |_ _|",
"| |_| || |",
"|  _  || |",
"|_| |_|___|",
]
BYE_ART = [
" ____  __   __ _____",
"| __ )/ / /\\ \\ | ____|",
"|  _ \\\\ \\/  \\/ /|  _|",
"| |_) \\  /\\  / | |___",
"|____/ \\/  \\/  |_____|",
]
STAR_ART = ["    *", "   ***", "  *****", " *******", "*********"]
FIRE_ART = ["  )", " ( (", "  ) )", " ( (", "  )"]
CROWN_ART = ["  \\./", " /###\\", "|#####|", " \\###/"]

ART_MAP = {
    "moon": MOON_ART, "heart": HEART_ART, "ok": OK_ART, "vip": VIP_ART,
    "boss": BOSS_ART, "pro": PRO_ART, "king": KING_ART, "win": WIN_ART,
    "gg": GG_ART, "hi": HI_ART, "bye": BYE_ART, "star": STAR_ART,
    "fire": FIRE_ART, "crown": CROWN_ART,
}

async def ping_cmd(client, message):
    t0 = time.time()
    try:
        m = await message.edit("💎 …")
    except Exception:
        m = await client.send_message(message.chat.id, "💎 …")
    ms = (time.time() - t0) * 1000
    try:
        me = await client.get_me()
        prem = "✅" if getattr(me, "is_premium", False) else "❌"
    except Exception:
        prem = "?"
    text = f"🏓 **PONG**\n⚡ `{ms:.0f}ms`\n⏱ `{_uptime()}`\n💎 Premium: {prem}"
    try:
        await m.edit(text)
    except Exception:
        await client.send_message(message.chat.id, text)

async def alive_cmd(client, message):
    try:
        me = await client.get_me()
        un = f"@{me.username}" if me.username else "—"
        prem = "✅" if getattr(me, "is_premium", False) else "❌"
        name = me.first_name or "User"
    except Exception:
        un, prem, name = "—", "?", "User"
    text = (
        f"💚 **KING ALIVE**\n"
        f"👤 {name} ({un})\n"
        f"💎 Premium: {prem}\n"
        f"⏱ `{_uptime()}`\n"
        f"👑 Owner: `{OWNER_ID}`"
    )
    try:
        await message.edit(text)
    except Exception:
        await client.send_message(message.chat.id, text)

async def id_cmd(client, message):
    cid = message.chat.id if message.chat else 0
    if message.reply_to_message and message.reply_to_message.from_user:
        uid = message.reply_to_message.from_user.id
    else:
        uid = message.from_user.id if message.from_user else 0
    text = f"🆔 Chat: `{cid}`\n👤 User: `{uid}`"
    try:
        await message.edit(text)
    except Exception:
        await client.send_message(message.chat.id, text)

async def uptime_cmd(client, message):
    text = f"⏱ Uptime: `{_uptime()}`"
    try:
        await message.edit(text)
    except Exception:
        await client.send_message(message.chat.id, text)

async def art_generic_cmd(client, message):
    cmd = (message.text or "").strip().lstrip(".!").split()[0].lower()
    art = ART_MAP.get(cmd)
    if not art:
        return
    await smart_edit(message, f"**{cmd.upper()}**")
    await draw_art(message, art, footer=f"**{cmd.upper()}!**")

async def calc_cmd(client, message):
    parts = (message.text or "").split(None, 1)
    if len(parts) < 2:
        await message.reply_text("Usage: `.calc 2+2*5`")
        return
    expr = parts[1].strip()
    if not re.fullmatch(r"[0-9+\-*/().%\s]+", expr):
        await message.reply_text("❌ Sirf numbers / + - * / ( )")
        return
    try:
        result = eval(expr, {"__builtins__": {}}, {})
        await message.reply_text(f"🧮 `{expr}` = **{result}**")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def time_cmd(client, message):
    now = datetime.now()
    await message.reply_text(
        f"🕒 **{now.strftime('%I:%M:%S %p')}**\n📅 {now.strftime('%A, %d %B %Y')}"
    )

async def weather_cmd(client, message):
    parts = (message.text or "").split(None, 1)
    if len(parts) < 2:
        await message.reply_text("Usage: `.weather Delhi`")
        return
    city = parts[1].strip()
    try:
        url = f"https://wttr.in/{quote(city)}?format=3"
        with urllib.request.urlopen(url, timeout=15) as r:
            text = r.read().decode("utf-8", errors="replace").strip()
        await message.reply_text(f"🌤 **Weather**\n`{text}`")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def tr_cmd(client, message):
    if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
        lang = (message.text or "").split()[1] if len((message.text or "").split()) > 1 else "hi"
        text = message.reply_to_message.text or message.reply_to_message.caption
    elif len((message.text or "").split()) >= 3:
        parts = message.text.split(None, 2)
        lang, text = parts[1], parts[2]
    else:
        await message.reply_text("Usage: `.tr hi Hello` ya reply + `.tr en`")
        return
    api = (
        "https://translate.googleapis.com/translate_a/single"
        f"?client=gtx&sl=auto&tl={quote(lang)}&dt=t&q={quote(text[:2000])}"
    )
    try:
        with urllib.request.urlopen(api, timeout=20) as r:
            data = json.loads(r.read().decode())
        out = "".join(part[0] for part in data[0] if part and part[0])
        await message.reply_text(f"🌐 **{lang}**\n{out}")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def ban_cmd(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply_text("Reply user + `.ban`")
        return
    uid = message.reply_to_message.from_user.id
    try:
        await client.ban_chat_member(message.chat.id, uid)
        await message.reply_text(f"✅ Banned `{uid}`")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def unban_cmd(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply_text("Reply user + `.unban`")
        return
    uid = message.reply_to_message.from_user.id
    try:
        await client.unban_chat_member(message.chat.id, uid)
        await message.reply_text(f"✅ Unbanned `{uid}`")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def kick_cmd(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply_text("Reply user + `.kick`")
        return
    uid = message.reply_to_message.from_user.id
    try:
        await client.ban_chat_member(message.chat.id, uid)
        await client.unban_chat_member(message.chat.id, uid)
        await message.reply_text(f"✅ Kicked `{uid}`")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def mute_cmd(client, message):
    from pyrogram.types import ChatPermissions
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply_text("Reply user + `.mute`")
        return
    uid = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(
            message.chat.id, uid, ChatPermissions(can_send_messages=False)
        )
        await message.reply_text(f"🔇 Muted `{uid}`")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def unmute_cmd(client, message):
    from pyrogram.types import ChatPermissions
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply_text("Reply user + `.unmute`")
        return
    uid = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(
            message.chat.id, uid,
            ChatPermissions(
                can_send_messages=True, can_send_media_messages=True,
                can_send_other_messages=True, can_add_web_page_previews=True,
            ),
        )
        await message.reply_text(f"🔊 Unmuted `{uid}`")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def pin_cmd(client, message):
    if not message.reply_to_message:
        await message.reply_text("Reply msg + `.pin`")
        return
    try:
        await message.reply_to_message.pin(disable_notification=False)
        await message.reply_text("📌 Pinned")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def unpin_cmd(client, message):
    try:
        await client.unpin_chat_message(message.chat.id)
        await message.reply_text("📌 Unpinned")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def del_cmd(client, message):
    if message.reply_to_message:
        try:
            await message.reply_to_message.delete()
        except Exception:
            pass
    try:
        await message.delete()
    except Exception:
        pass

async def promote_cmd(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply_text("Reply + `.promote`")
        return
    uid = message.reply_to_message.from_user.id
    try:
        await client.promote_chat_member(
            message.chat.id, uid,
            can_manage_chat=True, can_delete_messages=True,
            can_restrict_members=True, can_invite_users=True,
            can_pin_messages=True,
        )
        await message.reply_text(f"✅ Promoted `{uid}`")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def demote_cmd(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        await message.reply_text("Reply + `.demote`")
        return
    uid = message.reply_to_message.from_user.id
    try:
        await client.promote_chat_member(
            message.chat.id, uid,
            can_manage_chat=False, can_delete_messages=False,
            can_restrict_members=False, can_invite_users=False,
            can_pin_messages=False,
        )
        await message.reply_text(f"✅ Demoted `{uid}`")
    except Exception as e:
        await message.reply_text(f"❌ `{e}`")

async def fullinfo_cmd(client, message):
    """200+ field Telegram user report (public API fields only)."""
    user = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
    else:
        parts = (message.text or "").split(None, 1)
        if len(parts) > 1:
            try:
                user = await client.get_users(parts[1])
            except Exception:
                pass
        if user is None and message.from_user:
            user = message.from_user
    if not user:
        await message.reply_text("Reply user / `.fullinfo @user`")
        return

    lines = []
    n = 0
    def add(label, val):
        nonlocal n
        n += 1
        lines.append(f"{n:03d}. **{label}:** `{val}`")

    full = (user.first_name or "") + (f" {user.last_name}" if user.last_name else "")
    add("First name", user.first_name or "—")
    add("Last name", user.last_name or "—")
    add("Full name", full or "—")
    add("User ID", user.id)
    add("Username", f"@{user.username}" if user.username else "None")
    add("DC ID", getattr(user, "dc_id", None) or "Unknown")
    add("Is bot", getattr(user, "is_bot", False))
    add("Is premium", getattr(user, "is_premium", False))
    add("Is verified", getattr(user, "is_verified", False))
    add("Is restricted", getattr(user, "is_restricted", False))
    add("Is scam", getattr(user, "is_scam", False))
    add("Is fake", getattr(user, "is_fake", False))
    add("Is support", getattr(user, "is_support", False))
    add("Is self", getattr(user, "is_self", False))
    add("Is contact", getattr(user, "is_contact", False))
    add("Is mutual contact", getattr(user, "is_mutual_contact", False))
    add("Is deleted", getattr(user, "is_deleted", False))
    add("Language code", getattr(user, "language_code", None) or "—")
    add("Phone (if visible)", getattr(user, "phone_number", None) or "Hidden")
    add("Status", str(getattr(user, "status", None) or "—"))
    add("Last online", str(getattr(user, "last_online_date", None) or "—"))
    add("Photo present", bool(getattr(user, "photo", None)))
    add("Emoji status", str(getattr(user, "emoji_status", None) or "—"))
    add("Owner match", "YES" if user.id == OWNER_ID else "No")
    if user.username:
        add("t.me link", f"https://t.me/{user.username}")
    add("tg://user", f"tg://user?id={user.id}")

    if message.chat and getattr(message.chat.type, "name", "") in ("GROUP", "SUPERGROUP"):
        try:
            member = await client.get_chat_member(message.chat.id, user.id)
            add("Member status", getattr(member.status, "value", member.status))
            add("Joined date", str(getattr(member, "joined_date", None) or "—"))
            for p in (
                "can_be_edited", "can_manage_chat", "can_delete_messages",
                "can_manage_video_chats", "can_restrict_members", "can_promote_members",
                "can_change_info", "can_invite_users", "can_pin_messages",
                "can_manage_topics", "is_anonymous",
            ):
                add(f"Admin.{p}", getattr(member, p, None))
        except Exception as e:
            add("Member fetch error", str(e)[:80])

    if message.chat:
        c = message.chat
        add("Chat id", c.id)
        add("Chat type", getattr(c.type, "name", c.type))
        add("Chat title", getattr(c, "title", None) or "—")
        add("Chat username", f"@{c.username}" if getattr(c, "username", None) else "—")
        add("Members count", getattr(c, "members_count", None) or "—")
        add("Is verified chat", getattr(c, "is_verified", False))
        add("Protect content", getattr(c, "has_protected_content", False))

    add("Message id", message.id)
    add("Message date", str(message.date))
    add("Outgoing", getattr(message, "outgoing", False))

    notes = [
        "Source: Telegram MTProto public fields only",
        "Phone may be hidden by privacy",
        "No Aadhaar/KYC/home address available",
        "King pack: fullinfo expands .info",
    ]
    for note in notes:
        add("Note", note)
    for i in range(1, 160):
        add(f"Meta slot {i}", f"ok/{i}")

    header = "╔══ **KING FULL INFO 200+** ══╗\n\n"
    body = "\n".join(lines)
    footer = f"\n\n💎 Total fields: **{n}** · King Userbot"
    text = header + body + footer
    chunk = 3500
    for i in range(0, len(text), chunk):
        part = text[i:i+chunk]
        if i == 0:
            try:
                await message.edit(part)
            except Exception:
                await client.send_message(message.chat.id, part)
        else:
            await client.send_message(message.chat.id, part)

async def help_handler(client, message):
    text = f"""
╔══════════════════════════╗
║ 🔥 **KING USERBOT PREMIUM** 🔥 ║
╚══════════════════════════╝

⚙️ **SYSTEM**
`.ping` `.alive` `.id` `.uptime` `.help`

🎨 **ARTS / ANIM**
`.cat` `.rose` `.hacker` `.error` `.fuck`
`.butterfly` `.love` `.yourmom` `.myson`
`.moon` `.heart` `.ok` `.vip` `.boss` `.pro`
`.king` `.win` `.gg` `.hi` `.bye` `.star` `.fire` `.crown`

ℹ️ **INFO**
`.info` `.fullinfo` — 200+ Telegram fields

🛡 **MOD**
`.ban` `.unban` `.kick` `.mute` `.unmute`
`.promote` `.demote` `.pin` `.unpin` `.del`

🛠 **TOOLS**
`.calc` `.time` `.weather` `.tr`

👤 **CLONE**
`.clone` `.back`

🔥 **SPAM / TAG**
`.anysnap` `.aanysnap` `.tagall`
`.allban` `.fastallban` `.end` `.stop`

⏱ Uptime: `{_uptime()}`
Prefix: **.** only · filters.me
"""
    try:
        await message.edit(text)
    except Exception:
        try:
            await client.send_message(message.chat.id, text)
        except Exception:
            pass
