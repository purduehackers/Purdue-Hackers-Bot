import sqlite3
import discord
from discord.ext import commands
from discord import app_commands

db_path = 'channels.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()


class Bot(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #what gets run when the bot starts
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game(f"testing? testing? 123?"))
        print('This bot is online!')
            

    #help command
    @app_commands.command(name= 'help', description = 'Shows the help menu')
    async def help(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("test")


async def setup(bot: commands.Bot):
    await bot.add_cog(Bot(bot))