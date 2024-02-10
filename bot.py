import discord
from discord import emoji
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix='=', intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.tree.sync()
    print(f"{client.user} is connected to the server.")


class SelfPosition(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)

    @discord.ui.button(label="Top", style=discord.ButtonStyle.primary)
    async def Top(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Top"
        await interaction.response.send_message(content="Selected Top, choose a rank",
                                                view=SelfRanks(position))

    @discord.ui.button(label="Jng", style=discord.ButtonStyle.primary)
    async def Jng(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Jng"
        await interaction.response.send_message(content="Selected Jng, choose a rank",
                                                view=SelfRanks(position))

    @discord.ui.button(label="Mid", style=discord.ButtonStyle.primary)
    async def Mid(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Mid"
        await interaction.response.send_message(content="Selected Mid, choose a rank",
                                                view=SelfRanks(position))

    @discord.ui.button(label="Bot", style=discord.ButtonStyle.primary)
    async def Bot(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Bot"
        await interaction.response.send_message(content="Selected Bot, choose a rank",
                                                view=SelfRanks(position))

    @discord.ui.button(label="Sup", style=discord.ButtonStyle.primary)
    async def Sup(self, interaction: discord.Interaction, Button: discord.ui.Button):
        position = "Sup"
        await interaction.response.send_message(content="Selected Sup, choose a rank",
                                                view=SelfRanks(position))


class SelfRanks(discord.ui.View):
    def __init__(self, position):
        super().__init__(timeout=30)
        self.position = position

    @discord.ui.button(label="Iron", style=discord.ButtonStyle.primary)
    async def Iron_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Iron" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)

    @discord.ui.button(label="Bronze", style=discord.ButtonStyle.primary)
    async def Bronze_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Bronze" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)

    @discord.ui.button(label="Silver", style=discord.ButtonStyle.primary)
    async def Silver_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Silver" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)

    @discord.ui.button(label="Gold", style=discord.ButtonStyle.primary)
    async def Gold_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Gold" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)

    @discord.ui.button(label="Platinum", style=discord.ButtonStyle.primary)
    async def Platinum_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Platinum" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)

    @discord.ui.button(label="Diamond", style=discord.ButtonStyle.primary)
    async def Diamond_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Diamond" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)

    @discord.ui.button(label="Master", style=discord.ButtonStyle.primary)
    async def Master_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Master" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)

    @discord.ui.button(label="Grandmaster", style=discord.ButtonStyle.primary)
    async def Grandmaster_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Grandmaster" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)

    @discord.ui.button(label="Challenger", style=discord.ButtonStyle.primary)
    async def Challenger_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = "Challenger" + self.position
        get_role = discord.utils.get(interaction.guild.roles, name=role)
        await interaction.user.add_roles(get_role)
        await interaction.response.send_message(content="recieved role: " + role)


@client.tree.command(name="ping", description="show latency of the bot")
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"<:DiamondTop:1204243685445865543>")


@client.tree.command(name="selfroles", description="give yourself a role")
async def self_role(interaction: discord.Interaction):
    await interaction.response.send_message(content="choose your position", view=SelfPosition())


@client.tree.command(name="createrole", description="create all the roles")
async def createrole(interaction: discord.Interaction):
    all_positions = ["Top", "Jungle", "Mid", "Bot", "Support"]
    all_ranks = ["Iron", "Bronze", "Silver", "Gold", "Plat", "Diamond", "Master", "Grandmaster", "Challenger"]
    all_icons = ["<:IronTop:1204243791750627328>", "<:BronzeTop:1204243626553774151>", "<:SilverTop:1205964421629874206>",
                 "<:GoldTop:1204243717653794857>","<:PlatTop:1205960294107582594>","<:DiamondTop:1204243685445865543>","<:MasterTop:1204475730352672869>",
                 "<:GrandmasterTop:1204243753292931122>"," <:ChallengerTop:1204243653900501063>",

                 "<:IronJungle:1204243787245813882>", "<:BronzeJungle:1204243620287488112>","<:SilverJungle:1205964417913589820>",
                 "<:GoldJungle:1204243713480589312>", "<:PlatJungle:1205960288084557875>" ,"<:DiamondJungle:1204243680790183966>", "<:MasterJungle:1204475720772882473>",
                 "<:GrandmasterJungle:1204243748784177232>", "<:ChallengerJungle:1204243648250777601>",

                 "<:IronMid:1204243788185468929>", "<:BronzeMid:1204243622732759111>", "<:SilverMid:1205964419251568712>",
                 "<:GoldMid:1204243714638356600>","<:PlatMid:1205960291318505562>", " <:DiamondMid:1204243682698723348>", "<:MasterMid:1204475724917116958>",
                 "<:GrandmasterMid:1204243749836820571>", " <:ChallengerMid:1204243650582806598>",

                 "<:IronBot:1204243785534414888>", "<:BronzeBot:1204243618580267088>", "<:SilverBot:1205964416336662578>",
                 "<:GoldBot:1204243711186182234>", "<:PlatBot:1205960287019208734>" ,"<:DiamondBot:1204243679502409798>", "<:MasterBot:1204475689550749767>",
                 "<:GrandmasterBot:1204243747215384576>", "<:ChallengerBot:1204243646937825290>",

                 "<:IronSupport:1204243789967921163>", " <:BronzeSupport:1204243625169649685>", "<:SilverSupport:1205964420594012220>",
                  "<:GoldSupport:1204243715787460668>", "<:PlatSupport:1205960292731981845>" ," <:DiamondSupport:1204243683705225246>", "<:MasterSupport:1204475719661395978>",
                  "<:GrandmasterSupport:1204243751015551046>", "<:ChallengerSupport:1204243651811876885>"
                 ]
    for all_position in all_positions:
        for all_rank in all_ranks:
            posrank = all_rank + all_position
            src = "ranked-positions/" + posrank + ".png"
            with open(src, 'rb') as emoji_file:
                emoji_data = emoji_file.read()
            await interaction.guild.create_role(name=posrank, display_icon=emoji_data)
            emoji_file.close()
            await interaction.response.send_message(content="role created: " + src)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start("MTIwMjY3NTQ3MTExNzE5NzQwMg.GHaamE.2Y4lX7k2_e1gIdLsnhGHoJ37jH9lJPJbNlDXpw")


asyncio.run(main())
