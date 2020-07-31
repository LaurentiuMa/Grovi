import os
from datetime import datetime

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='/')


@client.command
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'[{datetime.now().time()}] {str(extension)} cog loaded')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'[{datetime.now().time()}] {str(extension)} cog unloaded')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found. '
                       'type ?help for the list of available commands')


@client.event
async def on_ready():
    print(f'[{datetime.now().time()}] Grovi started')


client.run('NzE4MTkwNDg4MzcyNjQxODIz.XtlRMQ.fv_Maj2clPFdjwIWhk8kNtrGunM')
