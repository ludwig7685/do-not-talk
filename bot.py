import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Replace 'YOUR_USER_IDS' with a list of user IDs you want to target
target_user_ids = [69420, 123456, 93746, lol]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message author is one of the target users
    if message.author.id in target_user_ids:
        try:
            await message.delete()
            print(f'Deleted message from {message.author.name}: {message.content}')
        except discord.Forbidden:
            print(f'Error: Bot does not have permission to delete messages.')

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    print(f'Error executing command: {error}')
    if isinstance(error, commands.CommandNotFound):
        print(f'Error: Command not found.')

# Add more bot commands here if needed

# Start the bot
bot.run('bot_token')
