# Mudrac – The Engineer's Slack Bot
Mudrac is a Slack bot for engineers, makers, and hardware hobbyists.
It provides component lookups, troubleshooting advice, and TERRIBLE jokes.
 
Built for Hack Club's Stardance program.
 
---
 
## Commands
 
| Command | Description | Example |
|---------|-------------|---------|
| `/mudrac` | Random greeting or dad joke | `/mudrac` |
| `/mudrac <question>` | Engineering advice (servo, motor, wifi, sensor, etc.) | `/mudrac my servo keeps jittering` |
| `/mudrac help` | Show all available commands | `/mudrac help` |
| `/coffee` | Coffee wisdom | `/coffee` |
| `/motivate-me` | Engineering pep talk | `/motivate-me` |
| `/fun-fun` | Electronics dad joke | `/fun-fun` |
| `/find-part <category>` | Find components by category | `/find-part imu` |
 
---
 
## Component Categories
 
Try `/find-part` with any of these:
 
| Category | Example Components |
|----------|-------------------|
| wifi | ESP32, ESP8266, Raspberry Pi Pico W |
| imu | MPU6050, ICM-20948, BNO055 |
| sensor | DHT22, BME280, DS18B20 |
| motor | L298N, TB6612FNG, PCA9685 |
| led | WS2812B, APA102, SK6812 |
| display | SSD1306, ILI9341, ST7789 |
| bluetooth | HC-05, HC-06, HM-10 |
| gps | NEO-6M, NEO-M8N |
| regulator | LM2596, AMS1117, LM317 |
| stepper | A4988, DRV8825, TMC2208 |
| audio | PAM8302, MAX98357 |
| rtc | DS1307, DS3231 |
| rfid | MFRC522, PN532 |
| lora | SX1276, RFM95 |
 
This is a partial list — see [`components.json`](./components.json) for the full database of 50+ components across 20+ categories.
 
---
 
## Setup
 
### Requirements
 
- Python 3.8 or higher
- Slack workspace with admin access
- Slack app with Socket Mode enabled
### Installation
 
```bash
git clone https://github.com/VMechLAB/Mudrac-Slack-Bot.git
cd Mudrac-Slack-Bot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
 
Key dependencies (see `requirements.txt` for the full pinned list):
 
- `slack-bolt` – Slack app framework
- `python-dotenv` – environment variable loading
### Slack App Configuration
 
Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps) (or use the manifest below), then enable:
 
- **Socket Mode**
- **Slash Commands**: `/mudrac`, `/coffee`, `/motivate-me`, `/fun-fun`, `/find-part`
- **OAuth Scopes**: `commands`, `chat:write`
<details>
<summary>Example app manifest (click to expand)</summary>
```yaml
display_information:
  name: Mudrac
features:
  bot_user:
    display_name: Mudrac
    always_online: true
  slash_commands:
    - command: /mudrac
      description: Engineering advice, greetings, and jokes
      should_escape: false
    - command: /coffee
      description: Coffee wisdom
      should_escape: false
    - command: /motivate-me
      description: Engineering pep talk
      should_escape: false
    - command: /fun-fun
      description: Electronics dad joke
      should_escape: false
    - command: /find-part
      description: Find components by category
      usage_hint: "[category]"
      should_escape: false
oauth_config:
  scopes:
    bot:
      - commands
      - chat:write
settings:
  org_deploy_enabled: false
  socket_mode_enabled: true
  token_rotation_enabled: false
```
 
</details>
### Configuration
 
Create a `.env` file in the project root:
 
```env
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
SLACK_SIGNING_SECRET=your-signing-secret
```
 
### Running Locally
 
```bash
python app.py
```
 
### Deployment
 
Deploy to Render.com for 24/7 uptime:
 
1. Push code to GitHub
2. Create a Web Service on Render
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Add environment variables
6. Deploy
---
 
## Files
 
| File | Purpose |
|------|---------|
| `app.py` | Main Slack Bolt application |
| `commands.py` | Command handlers and logic |
| `responses.json` | All response text (jokes, advice, etc.) |
| `components.json` | Component database |
| `requirements.txt` | Python dependencies |
 
---
 
## Contributing
 
Contributions are welcome! To add a new component, joke, or piece of advice:
 
1. Fork the repo
2. Add your entry to `components.json` (components) or `responses.json` (jokes/advice)
3. Open a pull request with a short description of what you added
For bugs or feature requests, open an issue.

---

## License
 
MIT License
