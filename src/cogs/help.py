from discord import Interaction, app_commands, Embed
from discord.ext import commands


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog()


class HelpCog(commands.Cog):
    def __init__(self: "HelpCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.commands()
    async def info(self: "HelpCog", ctx: Interaction) -> None:
        await ctx.response.send_message(
            embed=Embed(
                title="info",
                description="This is a basic economy discord bot created by Arty Studios",
            )
        )
