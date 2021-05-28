# (c) @Unknown
# Original written by @Unknown edit by @Unbornkiller

from telethon import events
import asyncio
from collections import deque
from userbot.events import register

@register(outgoing=True, pattern="^.jeelpatel$")
async def jeelpatel(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nA pro dev who makes custom Roms and a pro player in valorant known as jeel , the proest of em all`")
