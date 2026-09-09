import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

from commands import (
    handle_mudrac,
    handle_coffee,
    handle_motivate_me,
    handle_fun_fun,
    handle_find_part
)

load_dotenv()

bot_token = os.environ.get("SLACK_BOT_TOKEN")
app_token = os.environ.get("SLACK_APP_TOKEN")
signing_secret = os.environ.get("SLACK_SIGNING_SECRET")

print("Checking environment variables...")
if not bot_token:
    print("ERROR: SLACK_BOT_TOKEN is missing!")
if not app_token:
    print("ERROR: SLACK_APP_TOKEN is missing!")
if not signing_secret:
    print("ERROR: SLACK_SIGNING_SECRET is missing!")

app = App(
    token=bot_token,
    signing_secret=signing_secret
)

# Register commands with client passed in
app.command("/mudrac")(lambda ack, command, say, client: handle_mudrac(ack, command, say, client))
app.command("/coffee")(lambda ack, command, say, client: handle_coffee(ack, command, say, client))
app.command("/motivate-me")(lambda ack, command, say, client: handle_motivate_me(ack, command, say, client))
app.command("/fun-fun")(lambda ack, command, say, client: handle_fun_fun(ack, command, say, client))
app.command("/find-part")(lambda ack, command, say, client: handle_find_part(ack, command, say, client))

if __name__ == "__main__":
    if not app_token:
        print("ERROR: SLACK_APP_TOKEN not found!")
    elif not bot_token:
        print("ERROR: SLACK_BOT_TOKEN not found!")
    elif not signing_secret:
        print("ERROR: SLACK_SIGNING_SECRET not found!")
    else:
        print("Mudrac is running! Go test your commands in Slack.")
        print("")
        print("Available commands:")
        print("   /mudrac - Ask for advice or get a joke")
        print("   /coffee - Coffee wisdom")
        print("   /motivate-me - Engineering pep talk")
        print("   /fun-fun - Electronics dad joke")
        print("   /find-part <category> - Find components")
        SocketModeHandler(app, app_token).start()
