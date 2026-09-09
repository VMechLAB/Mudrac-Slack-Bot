import random
import json
import os
import time
import requests
from slack_bolt import Ack

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

def send_response(response_url, text):
    """Send a response using the response_url"""
    try:
        requests.post(response_url, json={"text": text})
    except Exception as e:
        print(f"Error sending response: {e}")

def handle_mudrac(ack: Ack, command: dict):
    start_time = time.time()
    ack()
    text = command.get("text", "").strip().lower()
    response_url = command.get("response_url")

    if not response_url:
        print("No response_url found in command")
        return

    if text in ["help", "commands", "?"]:
        response = get_help_text()
        elapsed = (time.time() - start_time) * 1000
        send_response(response_url, f"{response}\n\n_(responded in {elapsed:.0f}ms)_")
        return

    if not text:
        response = random.choice(RESPONSES["mudrac_general"])
        elapsed = (time.time() - start_time) * 1000
        send_response(response_url, f"{response}\n\n_(responded in {elapsed:.0f}ms)_")
        return

    advice_keys = sorted(RESPONSES["mudrac_advice"].keys(), key=len, reverse=True)
    for keyword in advice_keys:
        if keyword in text:
            response = RESPONSES["mudrac_advice"][keyword]
            elapsed = (time.time() - start_time) * 1000
            send_response(response_url, f"{response}\n\n_(responded in {elapsed:.0f}ms)_")
            return

    fallback = random.choice(RESPONSES["mudrac_unknown"])
    if len(text.split()) > 3:
        fallback += " Try using a single keyword like 'wifi' or 'servo'."
    elapsed = (time.time() - start_time) * 1000
    send_response(response_url, f"{fallback}\n\n_(responded in {elapsed:.0f}ms)_")

def handle_coffee(ack: Ack, command: dict):
    start_time = time.time()
    ack()
    response_url = command.get("response_url")
    if not response_url:
        return
    response = random.choice(RESPONSES["coffee"])
    elapsed = (time.time() - start_time) * 1000
    send_response(response_url, f"{response}\n\n_(responded in {elapsed:.0f}ms)_")

def handle_motivate_me(ack: Ack, command: dict):
    start_time = time.time()
    ack()
    response_url = command.get("response_url")
    if not response_url:
        return
    response = random.choice(RESPONSES["motivate"])
    elapsed = (time.time() - start_time) * 1000
    send_response(response_url, f"{response}\n\n_(responded in {elapsed:.0f}ms)_")

def handle_fun_fun(ack: Ack, command: dict):
    start_time = time.time()
    ack()
    response_url = command.get("response_url")
    if not response_url:
        return
    response = random.choice(RESPONSES["fun"])
    elapsed = (time.time() - start_time) * 1000
    send_response(response_url, f"{response}\n\n_(responded in {elapsed:.0f}ms)_")

def handle_find_part(ack: Ack, command: dict):
    start_time = time.time()
    ack()
    category = command.get("text", "").strip().lower()
    response_url = command.get("response_url")
    if not response_url:
        return

    if not category:
        elapsed = (time.time() - start_time) * 1000
        send_response(response_url, f"You need to give me a category, e.g. `/find-part wifi` or `/find-part sensor`\n\n_(responded in {elapsed:.0f}ms)_")
        return

    matches = [item for item in COMPONENTS if category in item["category"].lower()]

    if not matches:
        all_cats = sorted(set(item["category"] for item in COMPONENTS))
        cat_list = ", ".join(all_cats)
        elapsed = (time.time() - start_time) * 1000
        send_response(response_url, f"Hmm, I don't know any components in the *{category}* category. Try one of these: {cat_list}\n\n_(responded in {elapsed:.0f}ms)_")
        return

    names = ", ".join([item["name"] for item in matches])
    elapsed = (time.time() - start_time) * 1000
    send_response(response_url, f"*{category.upper()}* components I know: {names}\n\n_(responded in {elapsed:.0f}ms)_")
