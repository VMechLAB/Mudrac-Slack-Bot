import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

# Import our command handlers
from commands import (
    handle_mudrac,
    handle_coffee,
    handle_motivate_me,
    handle_fun_fun,
    handle_find_part
)

# Load environment variables from .env file (if it exists)
load_dotenv()

# DEBUG: Check if variables are being read
print("Checking environment variables...")
bot_token = os.environ.get("SLACK_BOT_TOKEN")
app_token = os.environ.get("SLACK_APP_TOKEN")
signing_secret = os.environ.get("SLACK_SIGNING_SECRET")

if not bot_token:
    print("ERROR: SLACK_BOT_TOKEN is missing!")
if not app_token:
    print("ERROR: SLACK_APP_TOKEN is missing!")
if not signing_secret:
    print("ERROR: SLACK_SIGNING_SECRET is missing!")

print(f"SLACK_BOT_TOKEN: {bot_token[:10]}... (length: {len(bot_token) if bot_token else 0})")
print(f"SLACK_APP_TOKEN: {app_token[:10]}... (length: {len(app_token) if app_token else 0})")
print(f"SLACK_SIGNING_SECRET: {signing_secret[:10] if signing_secret else 'MISSING'}... (length: {len(signing_secret) if signing_secret else 0})")

# Initialize the Slack app
app = App(
    token=bot_token,
    signing_secret=signing_secret
)

# Register all slash commands
app.command("/mudrac")(handle_mudrac)
app.command("/coffee")(handle_coffee)
app.command("/motivate-me")(handle_motivate_me)
app.command("/fun-fun")(handle_fun_fun)
app.command("/find-part")(handle_find_part)

if __name__ == "__main__":
    if not app_token:
        print("ERROR: SLACK_APP_TOKEN not found!")
        print("   Please add it. It starts with 'xapp-'")
    elif not bot_token:
        print("ERROR: SLACK_BOT_TOKEN not found!")
        print("   Please add it. It starts with 'xoxb-'")
    elif not signing_secret:
        print("ERROR: SLACK_SIGNING_SECRET not found!")
        print("   Please add it from Basic Information > App Credentials")
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
