from datetime import datetime
from random import randint

import discord
from discord.ext import commands
import re


class Rolling(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[{datetime.now().time()}] Rolling cog loaded')

    @commands.command()
    async def roll(self, ctx):
        user = f'<@{ctx.message.author.id}>'

        rolling_range = ctx.message.content[6:]
        print(rolling_range)

        if re.search('^[0-9:]', rolling_range) != -1:
            print('letter found')
            await ctx.send(f'{user}, the range cannot contain letters or symbols')
        elif rolling_range == '':
            print('no arguments')
            await ctx.send(f'{user} rolls {randint(0, 100)}')
        elif ':' in rolling_range:
            print(' ":" found')
            values = rolling_range.split(':')
            await ctx.send(f'{user} rolls {randint(int(values[0]), int(values[1]))}')
        else:
            print('integer passed')
            await ctx.send(f'{user} rolls {randint(0, int(rolling_range))}')


def setup(client):
    client.add_cog(Rolling(client))
