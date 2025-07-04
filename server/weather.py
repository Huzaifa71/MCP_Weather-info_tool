from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

# Initialize MCP server
mcp = FastMCP("weather")

# OpenWeatherMap API setup
API_KEY = "your api key"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
USER_AGENT = "pakistan-weather-tool/1.0"

# Generic request function for weather API
async def weather_request(city: str) -> dict[str, Any] | None:
    params = {
        "q": f"{city},PK",
        "appid": API_KEY,
        "units": "metric"
    }
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(BASE_URL, params=params, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except (httpx.RequestError, httpx.TimeoutException, httpx.HTTPStatusError, httpx.HTTPError):
            return None

# Customized Tool creation to get weather info for a Pakistani city
@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for a Pakistani city, e.g. 'Lahore', 'Islamabad', etc.
    """
    data = await weather_request(city)
    if not data:
        return " Weather data could not be retrieved. Please check the city name or try again later."

    try:
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        city_name = data["name"]

        return (
            f"  Weather in {city_name}, Pakistan:\n"
            f"- Condition: {weather}\n"
            f"- Temperature: {temp} °C\n"
            f"- Humidity: {humidity}%\n"
            f"- Wind Speed: {wind} m/s"
        )
    except (KeyError, IndexError):
        return " Unexpected response format from weather API."


# MCP Resource for weather tool configuration
@mcp.resource("config://weather")
def weather_config() -> str:
    """Weather tool configuration"""
    return (
        " Pakistan Weather Tool Configuration:\n"
        "- API: OpenWeatherMap\n"
        "- Units: Metric (°C)\n"
        "- Region: Pakistan\n"
        "- Source: https://openweathermap.org/api"
    )

# MCP Prompt for weather tool explanation
@mcp.prompt()
async def explain_weather(city: str) -> list[base.Message]:
    """
    Provide a natural-language explanation of the weather in the given city.
    """
    data = await weather_request(city)
    if not data:
        return [base.UserMessage(f" Weather data for {city} could not be retrieved.")]

    try:
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        city_name = data["name"]

        explanation = (
            f"The weather in {city_name} is currently {weather.lower()} with a temperature of {temp} °C. "
            f"Humidity is at {humidity}% and wind is blowing at {wind} meters per second."
        )

        return [
            base.UserMessage(f"What's the weather like in {city_name}?"),
            base.AssistantMessage(explanation)
        ]
    except (KeyError, IndexError):
        return [base.UserMessage(" Unexpected data format from the API.")]


