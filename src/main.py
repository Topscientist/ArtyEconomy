from discord.ext import commands
from discord import Intents
from glob import glob


bot = commands.Bot(command_prefix="!", intents=Intents.all(), client_id=123)


@bot.event
async def on_ready():
    for file in glob("./cogs/[!_]*.py"):
        await bot.load_extension(file[:-3].replace("\\", "."))

    await bot.tree.sync()
    print("the bot is online")


if __name__ == "__main__":
    bot.run("")
