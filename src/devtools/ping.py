import discord
from discord.ext import commands

from bot import tfumb

class PingCog(commands.Cog):
    def __init__(self, bot : tfumb):
        self.bot = bot

    @discord.app_commands.command(name="ping", description="Responds with pong.")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong")
        self.bot.logger.info("Ping Pong!")

async def setup(bot):
    await bot.add_cog(PingCog(bot))