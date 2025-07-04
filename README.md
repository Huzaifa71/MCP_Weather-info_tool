# 🇵🇰 Pakistan Weather Tool 🌦️

A lightweight, async-ready weather tool for Pakistani cities built with [FastMCP](https://github.com/huzaifa-memon/mcp) and [OpenWeatherMap API](https://openweathermap.org/api). Perfect for retrieving up-to-date weather information like temperature, humidity, wind, and condition using natural language prompts or API endpoints.

## 🔧 Features

- 🌍 City-specific weather in Pakistan
- ⚡ Asynchronous HTTP requests via `httpx`
- 🔄 OpenWeatherMap integration
- 📦 Tool-based architecture using FastMCP
- 💬 Includes natural language prompt support (e.g., "What's the weather like in Lahore?")

---

## 📦 Installation

```bash
git clone https://github.com/Huzaifa71/MCP_Weather-info_tool.git
cd pakistan-weather-tool
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the MCP Server
```bash
mcp dev server/weather.py
