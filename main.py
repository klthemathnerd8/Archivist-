import discord
from discord.ext import commands
import requests
import re, os
import requests
from bs4 import BeautifulSoup



# Global vars
token = os.getenv("bot_token")
bot_name = "Archivist++"
cmd_prefix = ","

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
client = commands.Bot(command_prefix=cmd_prefix, intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"{cmd_prefix}help"))
    print("Bot Online")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')



@client.command(name='profile')
async def profile(ctx, player_name):
    print(player_name)
    url = f"https://bandit.rip/player/@{player_name}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting player stats
        player_username = soup.find('div', class_='playerpage-profile-stats-2').get_text(strip=True)

        # Find all elements under the specified div class
        stats_elements = soup.find_all('div', class_='playerpage-profile-stats')

        # Accumulate information in a variable
        profile_info = f"{player_username}\n"

        # Append everything under the <div class="playerpage-profile-stats"> tags to the variable
        for stat_element in stats_elements:
            profile_info += stat_element.get_text(strip=True) + "\n"

        # Send the accumulated information in a code block
        await ctx.send(f"```\n{profile_info}\n```")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

@client.command(name='stats')
async def profile(ctx, player_name):
    print(player_name)
    url = f"https://bandit.rip/player/@{player_name}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting player stats
        player_username = soup.find('div', class_='playerpage-profile-stats-2').get_text(strip=True)

        # Find all elements under the specified div class
        stats_elements = soup.find_all('div', class_='playerpage-profile-stats')

        # Accumulate information in a variable
        profile_info = f"{player_username}\n"

        # Append everything under the <div class="playerpage-profile-stats"> tags to the variable
        for stat_element in stats_elements:
            profile_info += stat_element.get_text(strip=True) + "\n"

        # Send the accumulated information in a code block
        await ctx.send(f"```\n{profile_info}\n```")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")




# Run the bot with your token
client.run(token)
