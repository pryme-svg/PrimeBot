import discord
import requests
import random
from discord.ext import commands


class Urban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(alises=["ud", "urbandict"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def define(self, ctx, *, arg):

        url = "https://api.urbandictionary.com/v0/define?term=" + arg
        json1 = requests.get(url)
        data = json1.json()
        if not data["list"]:
            await ctx.send("Word not Found!")
            return
        defintion = data["list"][0]["definition"]
        title = "Urban Dictionary: " + arg
        embed = discord.Embed(title=title, description=description)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Urban(bot))
