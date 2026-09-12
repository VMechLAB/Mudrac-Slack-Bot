# Mudrac

He is THE dad like engeneer with stupid joks, some advice and ✨a tiniy silicon brain✨. 
Will waste you more time than save you but hey he doesnt have to be all that useful

## Commands

| Command | Description |
|---|---|
| `/mudrac` | Greeting or joke |
| `/mudrac <question>` | Engineering advice |
| `/mudrac help` | Show commands |
| `/coffee` | Coffee wisdom |
| `/motivate-me` | Engineering pep talk |
| `/fun-fun` | Electronics joke |
| `/find-part <category>` | Find components |

Example:

```text
/mudrac my servo keeps jittering
/find-part imu
/coffee
```
# Setup
## 1. Clone and install
Requirements:
Python 3.8+
A Slack workspace
A Slack app with Socket Mode enabled
git clone https://github.com/VMechLAB/Mudrac-Slack-Bot.git
cd Mudrac-Slack-Bot

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

## 2. Configure Slack
Create a Slack app and enable:
Socket Mode
Slash Commands
OAuth scopes: commands, chat:write
Add these slash commands:
/mudrac
/coffee
/motivate-me
/fun-fun
/find-part

## 3. Add environment variables
Create a .env file in the project root:

SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
SLACK_SIGNING_SECRET=your-signing-secret

Those are your dirty secrets

## 4. Run
python app.py
components.json contains 50 components across 20+ categories.
Examples: wifi, imu, sensor, motor, led, display, gps, bluetooth, lora.

## 5. Go trough the process 
Or just use him in a public channel he is awake 24/7. Here is the link to the channel where you can join:
https://hackclub.enterprise.slack.com/archives/C0C1D0S5J6N
It is called: mudrac-the-bot you can just search for it.

## Licence
MIT - free to use it to your liking.