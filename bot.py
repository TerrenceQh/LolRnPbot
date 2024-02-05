import discord
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix='=', intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    print(f'{client.user} is connected to the server.')
class SelfPosition (discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label = "Top", style = discord.ButtonStyle.primary)
    async def Top_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Top"
        await interaction.response.send_message(content="click a button corresponding to the rank", view=SelfRanks(position))
    @discord.ui.button(label="Jng", style=discord.ButtonStyle.primary)
    async def Jng_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Jng"
        await interaction.response.send_message(content="click a button corresponding to the rank", view=SelfRanks(position))
    @discord.ui.button(label="Mid", style=discord.ButtonStyle.primary)
    async def Mid_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Mid"
        await interaction.response.send_message(content="click a button corresponding to the rank", view=SelfRanks(position))
    @discord.ui.button(label="Bot", style=discord.ButtonStyle.primary)
    async def Bot_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Bot"
        await interaction.response.send_message(content="click a button corresponding to the rank", view=SelfRanks(position))
    @discord.ui.button(label="Sup", style=discord.ButtonStyle.primary)
    async def Sup_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Sup"
        await interaction.response.send_message(content="click a button corresponding to the rank", view=SelfRanks(position))
class SelfRanks(discord.ui.View):
    def __init__(self,position):
        super().__init__(timeout=None)
        self.position = position
    @discord.ui.button(label="Iron", style=discord.ButtonStyle.primary)
    async def Iron_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Iron" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
    @discord.ui.button(label="Bronze", style=discord.ButtonStyle.primary)
    async def Bronze_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Bronze" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
    @discord.ui.button(label="Silver", style=discord.ButtonStyle.primary)
    async def Silver_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Silver" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
    @discord.ui.button(label="Gold", style=discord.ButtonStyle.primary)
    async def Gold_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Gold" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
    @discord.ui.button(label="Platinum", style=discord.ButtonStyle.primary)
    async def Platinum_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Platinum" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
    @discord.ui.button(label="Diamond", style=discord.ButtonStyle.primary)
    async def Diamond_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Diamond" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
    @discord.ui.button(label="Master", style=discord.ButtonStyle.primary)
    async def Master_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Master" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
    @discord.ui.button(label="Grandmaster", style=discord.ButtonStyle.primary)
    async def Grandmaster_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Grandmaster" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
    @discord.ui.button(label="Challenger", style=discord.ButtonStyle.primary)
    async def Challenger_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Challenger" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)

        await interaction.user.add_roles(get_role)
@client.tree.command(name= "selfrank", description="change your rank")
async def self_rank(interaction: discord.Interaction):
    await interaction.response.send_message (content="click a button corresponding to the rank", view=SelfRanks())
@client.tree.command(name = "ping", description="show latency of the bot")
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"{bot_latency} ms")
@client.tree.command(name= "selfroles",description="give yourself a role")
async def self_role(interaction:discord.Interaction):
    await interaction.response.send_message(content="click a button corresponding to the rolecolour", view=SelfPosition())


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with client:
        await load()
        await client.start("MTIwMjY3NTQ3MTExNzE5NzQwMg.GqX-C0.e73pSInagFMW7DV2SKTeBr2VRPShq5XRfeEWAw")

asyncio.run(main())