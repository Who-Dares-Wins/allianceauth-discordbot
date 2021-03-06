import logging
import pendulum
import traceback
import re

import discord

from discord.ext import commands
from discord.embeds import Embed
from discord.colour import Color
from django.conf import settings

#log = logging.getLogger(__name__)

class Auth(commands.Cog):
    """
    Returns a link to the AllianceAuth Install
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def auth(self, ctx):
        """
        Returns a link to the AllianceAuth Install
        Used by many other Bots and is a common command that users will attempt to run.
        """
        await ctx.trigger_typing()

        embed = Embed(title="AllianceAuth")
        embed.set_thumbnail(
            url="https://assets.gitlab-static.net/uploads/-/system/project/avatar/6840712/Alliance_auth.png?width=128"
        )
        embed.colour = Color.blue()

        embed.description = "All Authentication functions for this Discord server are handled through our Alliance Auth install"
        
        regex = r"^(.+)\/d.+"

        matches = re.finditer(regex, settings.DISCORD_CALLBACK_URL, re.MULTILINE)

        for m in matches:
            url = m.groups()

        embed.add_field(
            name="Auth Link", value="[{}]({})".format(url[0], url[0]), inline=False
        )

        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Auth(bot))
