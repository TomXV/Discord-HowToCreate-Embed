import discord
from discord.ext import commands

TOKEN = 'TOKEN HERE!'

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("bot is ready.")


@client.command(pass_content=True)
async def clear(ctx):
    messages = []
    async for message in ctx.channel.history(limit=int(100)):
        message.append(message)
    await ctx.message.delete(messages)


@client.command()
async def displayembed(ctx):
    embed = discord.Embed(
        title='Title',
        description='This is a description.',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='This is a footer.')
    embed.set_image(url='https://media.discordapp.net/attachments/860875297419558912/860875514251051028/OIP.png')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/860875297419558912/860875514251051028/OIP.png')
    embed.set_author(name='Author Name',
                     icon_url='https://media.discordapp.net/attachments/860875297419558912/860875514251051028/OIP.png')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)
    embed.add_field(name='Field Name', value='Field Value', inline=True)

    await ctx.message.channel.send(embed=embed)


client.run(TOKEN)
