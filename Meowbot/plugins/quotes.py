import random

import requests

from . import *


@bot.on(mew_cmd(pattern="love$", outgoing=True))
@bot.on(sudo_cmd(pattern="love$", allow_sudo=True))
async def love(e):
    txt = random.choice(LOVESTR)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="dhoka$", outgoing=True))
@bot.on(sudo_cmd(pattern="dhoka$", allow_sudo=True))
async def katgya(e):
    txt = random.choice(DHOKA)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="metoo$", outgoing=True))
@bot.on(sudo_cmd(pattern="metoo$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(METOOSTR)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="gdnoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="gdnoon$", allow_sudo=True))
async def noon(e):
    txt = random.choice(GDNOON)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="chase$", outgoing=True))
@bot.on(sudo_cmd(pattern="chase$", allow_sudo=True))
async def police(e):
    txt = random.choice(CHASE_STR)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="congo$", outgoing=True))
@bot.on(sudo_cmd(pattern="congo$", allow_sudo=True))
async def Sahih(e):
    txt = random.choice(CONGRATULATION)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="qhi$", outgoing=True))
@bot.on(sudo_cmd(pattern="qhi$", allow_sudo=True))
async def hoi(e):
    txt = random.choice(HELLOSTR)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="gdbye$", outgoing=True))
@bot.on(sudo_cmd(pattern="gdbye$", allow_sudo=True))
async def bhago(e):
    txt = random.choice(BYESTR)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="gdnyt$", outgoing=True))
@bot.on(sudo_cmd(pattern="gdnyt$", allow_sudo=True))
async def night(e):
    txt = random.choice(GDNIGHT)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="gdmng$", outgoing=True))
@bot.on(sudo_cmd(pattern="gdmng$", allow_sudo=True))
async def morning(e):
    txt = random.choice(GDMORNING)
    await eor(e, txt)


@bot.on(mew_cmd(pattern="quote ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="quote ?(.*)", allow_sudo=True))
async def quote_search(event):
    if event.fwd_from:
        return
    Meow = await eor(event, "`Processing...`")
    if input_str := event.pattern_match.group(1):
        api_url = f"https://quotes.cwprojects.live/search/query={input_str}"
        try:
            response = random.choice(requests.get(api_url).json())
        except:
            response = None
    else:
        api_url = "https://quotes.cwprojects.live/random"
        try:
            response = requests.get(api_url).json()
        except:
            response = None
    if response is not None:
        await Meow.edit(f"`{response['text']}`")
    else:
        await eod(Meow, "`Sorry Zero results found`")


CmdHelp("quotes").add_command(
    "quote", None, "Sends a random mind-blowing quote"
).add_command("gdmng", None, "Sends a random Good Morning Quote").add_command(
    "gdnyt", None, "Sends a random Good Night Quote"
).add_command(
    "gdbye", None, "Sends a random Good Byee Quote"
).add_command(
    "qhi", None, "Sends a random Hello msg"
).add_command(
    "congo", None, "Sends a random congratulations quote"
).add_command(
    "chase", None, "Sends a random Chase quote"
).add_command(
    "gdnoon", None, "Sends a random Good Afternoon quote"
).add_command(
    "metoo", None, "Sends a text saying Mee too."
).add_command(
    "dhoka", None, "Sends a random Dhoka quote(katt gya bc)"
).add_command(
    "love", None, "Sends a random love quote🥰. (A stage before .dhoka)"
).add_info(
    "Random Quotes."
).add_warning(
    "✅ Harmless Module."
).add()
