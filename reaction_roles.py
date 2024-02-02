import discord

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1202765374383194162

    async def on_raw_reaction_add(self, payload):
        if payload.user_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        print(payload.emoji.name)


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
client.run('MTIwMjY3NTQ3MTExNzE5NzQwMg.GU7Eye.p6699o3tAH2dKnH1VuszacVJJYl9ANjFmYYGKI')