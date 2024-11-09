import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith("Naber?"):
        await message.channel.send("İyi sen?")
    else:
        await message.channel.send(message.content)

client.run("BMTMwMDAzNDE3NTc0Mjc3NTM1OA.GzkK2z.NGTD_gC2NWIIQk7_fJ-_Kf9BsXKP4oxQBVRF9s")
