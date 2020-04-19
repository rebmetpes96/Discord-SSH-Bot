import discord
import paramiko
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def ssh(xtc,*args):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect("[YOUR-DEVICE-IP]", port=22, username="pi", password="raspberry")

    output = ''
    for word in args:
        output+= word
        output+= ' '


    print(output)
    stdin, stdout, stderr = client.exec_command(output)
    output = stdout.readlines()
    (type(output))
    print('\n'.join(output))
    await xtc.send('\n'.join(output))



#Token
client.run('[YOUR-TOKEN]')
