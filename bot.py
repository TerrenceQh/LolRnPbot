import discord
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix='=', intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.tree.sync()
    print(f'{client.user} is connected to the server.')


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
    await interaction.response.send_message(f"<:Position_DiamondTop:1202765203557584906>")


@client.tree.command(name="selfroles", description="give yourself a role")
async def self_role(interaction: discord.Interaction):
    await interaction.response.send_message(content="choose your position", view=SelfPosition())


@client.tree.command(name="createrole", description="create all the roles")
async def createrole(interaction: discord.Interaction):
    all_positions = ["Top", "Jng", "Mid", "Bot", "Sup"]
    all_ranks = ["Iron", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grandmaster", "Challenger"]
    all_icons = ['<:IronTop:1204243791750627328>', ' <:BronzeTop:1204243626553774151>', ' <:Position_SilverTop:1202765001644056606>',
                 '<:GoldTop:1204243717653794857>',' <:Position_PlatTop:1202764964465483847>',' <:DiamondTop:1204243685445865543>',' <:Position_MasterTop:1202764932895215626>',
                 '<:GrandmasterTop:1204243753292931122>',' <:ChallengerTop:1204243653900501063>',

                 '<:IronJungle:1204243787245813882>', '<:BronzeJungle:1204243620287488112>',' <:Position_SilverJungle:1202764996308762624>',
                 '<:GoldJungle:1204243713480589312>', ' <:Position_PlatJungle:1202764961080672298>' ,'<:DiamondJungle:1204243680790183966>', '<:Position_MasterJungle:1202764928272826458>',
                 ' <:GrandmasterJungle:1204243748784177232>', '<:ChallengerJungle:1204243648250777601>',

                 '<:IronMid:1204243788185468929>', '<:BronzeMid:1204243622732759111>', ' <:Position_SilverMid:1202764998162784306>',
                 ' <:GoldMid:1204243714638356600>','<:Position_PlatMid:1202764962003558471>', ' <:DiamondMid:1204243682698723348>', '<:Position_MasterMid:1202764930013728779>',
                 ' <:GrandmasterMid:1204243749836820571>', ' <:ChallengerMid:1204243650582806598>',

                 '<:IronBot:1204243785534414888>', '<:BronzeBot:1204243618580267088>', ' <:Position_SilverBot:1202764995306332160>',
                 '<:GoldBot:1204243711186182234>', ' <:Position_PlatBot:1202764959499554906>' ,'<:DiamondBot:1204243679502409798>', ' <:Position_MasterBot:1202764927081775134>',
                 '<:GrandmasterBot:1204243747215384576>', '<:ChallengerBot:1204243646937825290>',

                 '<:IronSupport:1204243789967921163>', ' <:BronzeSupport:1204243625169649685>', ' <:Position_SilverSupport:1202764999446106223>',
                 ' <:GoldSupport:1204243715787460668>', ' <:Position_PlatSupport:1202764962901004299>' ,' <:DiamondSupport:1204243683705225246>', ' <:Position_MasterSupport:1202764931443986433>,'
                 ' <:GrandmasterSupport:1204243751015551046>', ' <:ChallengerSupport:1204243651811876885>'
                 ]
    count = 0
    for all_position in all_positions:
        for all_rank in all_ranks:
            count += 1
            posrank = all_rank + all_position
            await interaction.guild.create_role(name=posrank, display_icon=all_icons[count - 1])
            await interaction.response.send_message(content="role created")


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


async def main():
    async with client:
        await load()
        await client.start("YOUR_TOKEN")


asyncio.run(main())
