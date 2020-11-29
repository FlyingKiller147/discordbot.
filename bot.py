import discord
from discord.ext import commands




client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('Bot Is Ready ')



client.run('Nzc3NDQxMjAxMDk0Nzg3MTIy.X7Deig.ONpbv2OyD2jFHc_FDQLghG5YLWw')


