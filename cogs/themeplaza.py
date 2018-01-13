# TP-Bot - A discord bot for the ThemePlaza Discord
# Copyright (C) 2018 Valentijn "Ev1l0rd"
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import discord
import requests
from discord.ext import commands
import datetime


class ThemePlaza:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def theme_id(self, ctx, *, tid):
        '''Query a theme by it's ID for ThemePlaza

        The ID is the number after /item/ in the URL for a theme.'''
        api_request = requests.get('https://themeplaza.eu/api/v0/theme_lookup?item_id=' + tid)
        if api_request.status_code is 200:
            api_request = api_request.json()
            embed = discord.Embed(title=api_request['title'],
                description=api_request['description'],
                url='https://themeplaza.eu/item/' + tid)
            if api_request['metadata']['enable_bgm'] is 1:
                embed.add_field(name="BGM",
                    value=api_request['metadata']['bgm_info'],
                    inline=False)
            if api_request['metadata']['custom_cursor'] is 1:
                embed.add_field(name="Custom Cursor",
                    value="Has custom cursor artwork")
            if api_request['metadata']['custom_folder'] is 1:
                embed.add_field(name="Custom Folder",
                    value="Has custom folder artwork")
            if api_request['metadata']['custom_cart'] is 1:
                embed.add_field(name="Custom Cart",
                    value="Has custom cart artwork")
            if api_request['metadata']['custom_sfx'] is 1:
                embed.add_field(name="Custom SFX",
                    value="Has custom SFX")
            embed.set_author(name=api_request['author'], url='https://themeplaza.eu/profile' + api_request['author'])
            embed.set_footer(text=api_request['upload_date'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("Invalid theme ID!")


def setup(bot):
    bot.add_cog(ThemePlaza(bot))
