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

app = App(
    token=bot_token,
    signing_secret=signing_secret
)

# Register commands - now we only pass ack and command
app.command("/mudrac")(handle_mudrac)
app.command("/coffee")(handle_coffee)
app.command("/motivate-me")(handle_motivate_me)
app.command("/fun-fun")(handle_fun_fun)
app.command("/find-part")(handle_find_part)

if __name__ == "__main__":
    if not app_token:
        print("ERROR: SLACK_APP_TOKEN not found!")
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
