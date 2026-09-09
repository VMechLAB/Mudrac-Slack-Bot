import random
import json
import os
from slack_bolt import Ack, Say

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "components.json")) as f:
    COMPONENTS = json.load(f)

with open(os.path.join(BASE_DIR, "responses.json")) as f:
    RESPONSES = json.load(f)

# Smart Help Message 
def get_help_text():
    return (
        "*Mudrac Help Desk*\n"
        "• `/mudrac` – Just say hi\n"
        "• `/mudrac <issue>` – Ask about: servo, motor, wifi, sensor, i2c, spi, arduino, code, battery, soldering, esp32, etc.\n"
        "• `/coffee` – Get caffeinated wisdom\n"
        "• `/motivate-me` – Get an engineering pep talk\n"
        "• `/fun-fun` – Get an electronics dad joke\n"
        "• `/find-part <category>` – Find components (e.g. wifi, imu, sensor, led, motor)\n"
        "\n_Try typing `/mudrac my servo is shaking` to see me in action!_"
    )

# /mudrac
def handle_mudrac(ack: Ack, command: dict, say: Say):
    ack()
    text = command.get("text", "").strip().lower()
    channel = command.get("channel_id")

    if text in ["help", "commands", "?"]:
        say(text=get_help_text(), channel=channel)
        return

    if not text:
        say(text=random.choice(RESPONSES["mudrac_general"]), channel=channel)
        return

    advice_keys = sorted(RESPONSES["mudrac_advice"].keys(), key=len, reverse=True)
    for keyword in advice_keys:
        if keyword in text:
            say(text=RESPONSES["mudrac_advice"][keyword], channel=channel)
            return

    fallback = random.choice(RESPONSES["mudrac_unknown"])
    if len(text.split()) > 3:
        fallback += " Try using a single keyword like 'wifi' or 'servo'."
    say(text=fallback, channel=channel)


# /coffee
def handle_coffee(ack: Ack, command: dict, say: Say):
    ack()
    channel = command.get("channel_id")
    say(text=random.choice(RESPONSES["coffee"]), channel=channel)


# /motivate-me
def handle_motivate_me(ack: Ack, command: dict, say: Say):
    ack()
    channel = command.get("channel_id")
    say(text=random.choice(RESPONSES["motivate"]), channel=channel)


# /fun-fun
def handle_fun_fun(ack: Ack, command: dict, say: Say):
    ack()
    channel = command.get("channel_id")
    say(text=random.choice(RESPONSES["fun"]), channel=channel)


# /find-part
def handle_find_part(ack: Ack, command: dict, say: Say):
    ack()
    category = command.get("text", "").strip().lower()
    channel = command.get("channel_id")

    if not category:
        say(text="You need to give me a category, e.g. `/find-part wifi` or `/find-part sensor`", channel=channel)
        return

    matches = [item for item in COMPONENTS if category in item["category"].lower()]

    if not matches:
        all_cats = sorted(set(item["category"] for item in COMPONENTS))
        cat_list = ", ".join(all_cats)
        say(text=f"Hmm, I don't know any components in the *{category}* category. Try one of these: {cat_list}", channel=channel)
        return

    names = ", ".join([item["name"] for item in matches])
    say(text=f"*{category.upper()}* components I know: {names}", channel=channel)
