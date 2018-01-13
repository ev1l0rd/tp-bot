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
from discord.ext import commands


class Support:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guide(self, ctx):
        '''Link to Ryumaru's theme guides'''
        embed = discord.Embed(title='Ryumaru\'s Theming Guides',
            type='rich',
            description='If you want to know how to make good quality themes, follow Ryumaru\'s Theming Guides over on GBATemp.',
            url='https://gbatemp.net/threads/tutorials-to-create-custom-themes-with-the-same-quality-of-official-nintendo-themes.460823/')
        embed.set_author(name='Ryumaru#4575',
            icon_url='https://secure.gravatar.com/avatar/317532823ab2aa3c54cfd6d711050597')
        await ctx.send(embed=embed)

    @commands.command()
    async def install(self, ctx):
        '''Link to Anemone3DS.'''
        embed = discord.Embed(title='Anemone3DS',
            type='rich',
            description='Anemone is the recommended theme manager for themes and Luma3DS splashes on the 3DS. Install the latest CIA from the releases page or scan the QR code in FBI.',
            url='https://github.com/astronautlevel2/Anemone3DS/releases/latest')
        embed.set_author(name='astronautlevel',
            icon_url='https://avatars1.githubusercontent.com/u/7305572')
        await ctx.send(embed=embed)

    @commands.command()
    async def howling(self, ctx):
        '''Link to Howling Theme Tools GBATemp post.'''
        embed = discord.Embed(title='Howling Theme Tool',
            type='rich',
            description='If you want to manage themes using the build-in theme selector, use Howling Theme Tool. Howling Theme Tool is a desktop application that can generate theme CIAs that show up in the build-in theme selector.',
            url='https://gbatemp.net/threads/release-howling-theme-tool-create-your-own-cia-theme-packages-with-custom-and-official-themes.401081/')
        embed.set_author(name='Chelsea_Fantasy',
            icon_url='https://gbatemp.net/data/avatars/m/347/347208.jpg')
        await ctx.send(embed=embed)

    @commands.command()
    async def gytb(self, ctx):
        '''Link to GTYB.'''
        embed = discord.Embed(title='GTYB',
            type='rich',
            description='In order to install badges, the recommended installer is GTYB. Download the CIA from the url. Note that officially, GTYB is discontinued, but as there are no simple alternatives available (yet), it is the recommended tool.',
            url='https://www.dropbox.com/s/qwd143416psttp2/GYTB_cia.zip?dl=0')
        embed.set_author(name='MrCheeze',
            icon_url='https://avatars3.githubusercontent.com/u/6541413')
        embed.add_field(name='How to use GTYB',
            value='Put the downloaded badge images on the SD card in a folder called \'badges\'. Then open GTYB from the home menu. It will first dump any official badges you have from the Badge Arcade, then it will import all the badges. If GTYB crashes, make sure that your total amount of badges (official and those in the badges folder) does not exceed 1000 and that you have run the Badge Arcade at least once.')
        await ctx.send(embed=embed)

    @commands.command(aliases=['tos'])
    async def faq(self, ctx):
        '''Link to official ThemePlaza FAQ'''
        embed = discord.Embed(title='ThemePlaza FAQ',
            type='rich',
            description='If you have any questions about ThemePlaza the website, please read the FAQ.',
            url='https://gist.github.com/wrathsoffire76/8e4359929e1cb980d1c574c9484b6863')
        embed.set_author(name='wrathsoffire76#3927',
            icon_url='https://avatars1.githubusercontent.com/u/25714359')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Support(bot))
