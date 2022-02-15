import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="Sample bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Cybrancee Bot Hosting", url="https://cybrancee.com"))
    print('Bot online')

bot.run('token')
