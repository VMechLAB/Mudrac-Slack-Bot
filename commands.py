import random
import json
import os
import time
from slack_bolt import Ack, Say

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "components.json")) as f:
    COMPONENTS = json.load(f)

with open(os.path.join(BASE_DIR, "responses.json")) as f:
    RESPONSES = json.load(f)

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

def handle_mudrac(ack: Ack, command: dict, say: Say):
    start_time = time.time()
    ack()
    text = command.get("text", "").strip().lower()
    channel = command.get("channel_id")
    
    # If channel is None, try using user_id as fallback
    if not channel:
        channel = command.get("user_id")
    
    # If still None, use the response_url (Slack will handle it)
    if not channel:
        say(text="I couldn't determine where to send this message. Please try again in a channel.", response_type="ephemeral")
        return

    if text in ["help", "commands", "?"]:
        response = get_help_text()
        elapsed = (time.time() - start_time) * 1000
        say(text=f"{response}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)
        return

    if not text:
        response = random.choice(RESPONSES["mudrac_general"])
        elapsed = (time.time() - start_time) * 1000
        say(text=f"{response}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)
        return

    advice_keys = sorted(RESPONSES["mudrac_advice"].keys(), key=len, reverse=True)
    for keyword in advice_keys:
        if keyword in text:
            response = RESPONSES["mudrac_advice"][keyword]
            elapsed = (time.time() - start_time) * 1000
            say(text=f"{response}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)
            return

    fallback = random.choice(RESPONSES["mudrac_unknown"])
    if len(text.split()) > 3:
        fallback += " Try using a single keyword like 'wifi' or 'servo'."
    elapsed = (time.time() - start_time) * 1000
    say(text=f"{fallback}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)

def handle_coffee(ack: Ack, command: dict, say: Say):
    start_time = time.time()
    ack()
    channel = command.get("channel_id")
    if not channel:
        channel = command.get("user_id")
    if not channel:
        say(text="I couldn't determine where to send this message.", response_type="ephemeral")
        return
    response = random.choice(RESPONSES["coffee"])
    elapsed = (time.time() - start_time) * 1000
    say(text=f"{response}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)

def handle_motivate_me(ack: Ack, command: dict, say: Say):
    start_time = time.time()
    ack()
    channel = command.get("channel_id")
    if not channel:
        channel = command.get("user_id")
    if not channel:
        say(text="I couldn't determine where to send this message.", response_type="ephemeral")
        return
    response = random.choice(RESPONSES["motivate"])
    elapsed = (time.time() - start_time) * 1000
    say(text=f"{response}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)

def handle_fun_fun(ack: Ack, command: dict, say: Say):
    start_time = time.time()
    ack()
    channel = command.get("channel_id")
    if not channel:
        channel = command.get("user_id")
    if not channel:
        say(text="I couldn't determine where to send this message.", response_type="ephemeral")
        return
    response = random.choice(RESPONSES["fun"])
    elapsed = (time.time() - start_time) * 1000
    say(text=f"{response}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)

def handle_find_part(ack: Ack, command: dict, say: Say):
    start_time = time.time()
    ack()
    category = command.get("text", "").strip().lower()
    channel = command.get("channel_id")
    if not channel:
        channel = command.get("user_id")
    if not channel:
        say(text="I couldn't determine where to send this message.", response_type="ephemeral")
        return

    if not category:
        elapsed = (time.time() - start_time) * 1000
        say(text=f"You need to give me a category, e.g. `/find-part wifi` or `/find-part sensor`\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)
        return

    matches = [item for item in COMPONENTS if category in item["category"].lower()]

    if not matches:
        all_cats = sorted(set(item["category"] for item in COMPONENTS))
        cat_list = ", ".join(all_cats)
        elapsed = (time.time() - start_time) * 1000
        say(text=f"Hmm, I don't know any components in the *{category}* category. Try one of these: {cat_list}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)
        return

    names = ", ".join([item["name"] for item in matches])
    elapsed = (time.time() - start_time) * 1000
    say(text=f"*{category.upper()}* components I know: {names}\n\n_(responded in {elapsed:.0f}ms)_", channel=channel)
