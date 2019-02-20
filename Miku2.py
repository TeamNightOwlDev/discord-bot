# Work with Python 3.6
import random
import asyncio
import discord
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound

BOT_PREFIX = ("+")
#https://discordapp.com/oauth2/authorize?client_id=547553744506716170&scope=bot&permissions=1022748758
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    print("Command:eightball")
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with friends"))
    print("Logged in as " + client.user.name, "Hooray!")
    print("----------------------------------------------")

@client.event
async def on_message(message):
# we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('+help'):
        print ("Command:Help")

        msg = ("""```H-hello, My name is Miku Nakano. My Prefix is +
Commands you can tell me are: 
+help-Shows this help screen
+hello-To say hi to me!
+howareyou-Ask me how I am!
+loveyou-You can figure that one out...
+pictureofyou-See a picture of me
+fact-learn a fact about ancient warlords.```
            """)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+hello'):
        print ("Command:Hello")
        responses = ['O-oh, hi there {0.author.mention}', '*blushes*, hello {0.author.mention}', 'Hello {0.author.mention} you look great today!']
        msg = random.choice(responses).format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+fact'):
        print ("Command:Fact")
        responses = ['The Shin dynasty is one of the greatest anime warlords of all time!', 'New factions and alliances constantly ensured that no one warlord ever became powerful enough to destroy all the rest', 'Yuan’s power had come from his position as head of the Beiyang Army, which was the only major modern military force in China at the time.', 'Duan Qirui, Wade-Giles romanization Tuan Ch’i-jui, (born March 6, 1865, Hefei, Anhui province, China—died Nov. 2, 1936, Shanghai), warlord who dominated China intermittently between 1916 and 1926.']
        msg = random.choice(responses).format(message)
        await client.send_message(message.channel, msg) 
    if message.content.startswith('+pictureofyou'):
        print ("Command:Picture")
        pictures = ['Miku.jpg', 'Miku2.jpg', 'Miku3.jpg','Miku4.jpg','Miku5.jpg', 'Miku6.jpg', 'cute.gif']
        msg = 'F-Fine {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        msg2 = random.choice(pictures)
        await client.send_file(message.channel, msg2)
    if message.content.startswith('+loveyou'):
        print ("Command:loveyou")
        responses = ['I l-love you too {0.author.mention}', '*blushes*', 'd-dont say that outloud {0.author.mention}!']
        msg = random.choice(responses).format(message)
        await client.send_message(message.channel, msg) 
    if message.content.startswith('+howareyou'):
        print ("Command:howareyou")
        responses = ['Could be better, but its great now.', 'Im doing good', 'Great!']
        msg = random.choice(responses).format(message)
        await client.send_message(message.channel, msg)         
    if message.content.startswith('Im doing good'):
        msg = ("Thats good to hear").format(message)
        await client.send_message(message.channel, msg)
    await client.process_commands(message)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
            print("--------------------------------")
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)