# 🚀 𝘽𝙪𝙞𝙡𝙩 𝙖 𝘾𝙪𝙨𝙩𝙤𝙢 𝙒𝙚𝙖𝙩𝙝𝙚𝙧 𝙄𝙣𝙛𝙤 𝙏𝙤𝙤𝙡 𝙬𝙞𝙩𝙝 𝙈𝘾𝙋 (𝙈𝙤𝙙𝙚𝙡 𝘾𝙤𝙣𝙩𝙚𝙭𝙩 𝙋𝙧𝙤𝙩𝙤𝙘𝙤𝙡) 🌦️

Ever wanted to fetch real-time weather updates for any Pakistani city using your own **AI-integrated assistant**?  
This project is a modular, prompt-ready weather tool tailored for **Pakistan’s cities**, powered by the 🌐 **OpenWeatherMap API**, and built using the ⚙️ **FastMCP** framework.

---

## 🔧 𝙏𝙚𝙘𝙝 𝙎𝙩𝙖𝙘𝙠 & 𝙆𝙚𝙮 𝙁𝙚𝙖𝙩𝙪𝙧𝙚𝙨:

- 💻 **Framework**: `FastMCP (Modular Command Protocol)`
- 🌍 **API**: `OpenWeatherMap` for real-time weather data
- ⚙️ **Async HTTP**: Used `httpx` for efficient asynchronous API calls
- 🧠 **Custom Tools & Prompts**:
  - `@mcp.tool()` → Dynamic weather fetching
  - `@mcp.resource()` → Tool configuration overview
  - `@mcp.prompt()` → Natural language weather explanations

---

## 📦 𝙁𝙚𝙖𝙩𝙪𝙧𝙚𝙨 𝙄𝙢𝙥𝙡𝙚𝙢𝙚𝙣𝙩𝙚𝙙:

- 🌀 **`get_weather(city)`**  
  Get current weather with a structured natural-language response.

- 💬 **`explain_weather(city)`**  
  Prompt the assistant: _“What’s the weather like in Islamabad?”_

- ⚙️ **`weather_config()`**  
  Outputs tool configuration and API source metadata.

---

## 🛠️ 𝘿𝙚𝙨𝙞𝙜𝙣𝙚𝙙 𝙏𝙤 𝙍𝙪𝙣 𝙊𝙣 𝘽𝙤𝙩𝙝:

- 🧪 **MCP Inspector** — For local testing/debugging
- 💻 **Claude Desktop** — For clean user interactions with toolchain prompts

---

## 🚀 𝙌𝙪𝙞𝙘𝙠 𝙎𝙩𝙖𝙧𝙩

### 📁 Clone the Repo

```bash
git clone https://github.com/Huzaifa71/MCP_Weather-info_tool.git
cd MCP_Weather-info_tool
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the MCP Server
```bash
mcp dev server/weather.py
