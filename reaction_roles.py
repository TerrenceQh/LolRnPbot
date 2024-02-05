import discord
# https://discord.com/channels/1190491933852848178/1190491934335180800/1204136664696360990
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1204136664696360990
    async def on_ready(self):
        print('ready')
    async def on_raw_reaction_add(self, payload):
        if payload.user_id != self.target_message_id:
            return

        # guild = client.get_guild(payload.guild_id)

        print(payload.emoji.name)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('MTIwMjY3NTQ3MTExNzE5NzQwMg.GqX-C0.e73pSInagFMW7DV2SKTeBr2VRPShq5XRfeEWAw')