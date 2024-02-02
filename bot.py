import discord
import responses
import reaction_roles

async def give_roles(bot, message):
    try:
        reaction_roles.MyClient(discord.Client, message)
    except Exception as re:
        print(re)
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN =  'MTIwMjY3NTQ3MTExNzE5NzQwMg.GU7Eye.p6699o3tAH2dKnH1VuszacVJJYl9ANjFmYYGKI'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is connected to the server.')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_msg = str(message.content)
        channel = str(message.channel)

        print(f'{username}said: {user_msg} ({channel})')

        if (user_msg[0] == "?"):
            user_msg = user_msg[1:]
            await send_message(message,user_msg,is_private=True)
        elif (user_msg[0]=="!"):
            user_msg = user_msg[1:]
            await send_message(message, user_msg, is_private=False)
        if user_msg == 'cool':
            await message.add_reaction('\U0001F603')
    client.run(TOKEN)