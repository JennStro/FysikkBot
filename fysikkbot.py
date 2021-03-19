import discord
import os
import random
import emoji
import sys

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    sys.stdout.flush()

motivations = ["Keep going!", "Just do it!", "You're not as dumb as you think.", "Life will get better.", "Today is your day", "Heiaheia", "I'm sending you lots of hugs!", "You have so many other good qualities.", "Go kick some ass!", "Always look on the bright side of life.", "Don't limit yourself!", "Be yourself, everyone else is already taken!", "You are smart, strong and beautiful!", "It's your time to shine!!"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content.startswith('hjelp') or message.content.startswith('Hjelp')):
        random_motivation = random.choice(motivations)
        await message.channel.send('Hello, @' + message.author.name + "! " + random_motivation + " \N{SLIGHTLY SMILING FACE}")

    if message.content.startswith('Ai'):
      await message.channel.send("Aiiaiiiaiii. Men det fikser seg @" + message.author.name + " " + emoji.emojize(':thumbs_up:'))
    
    if (message.content == "hei" or message.content == "Hei" or message.content == "hei!" or message.content == "Hei!"):
      await message.channel.send("Heiii " + message.author.name + "!!")

client.run(os.environ.get('TOKEN'))