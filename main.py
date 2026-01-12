import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

if token is None:
    print("Erro: O token do Discord não foi encontrado nas variáveis de ambiente.")
    exit(1)

print("Bot iniciado...")

intents = discord.Intents.all()

# Create bot instance with specified command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)


# Bot inicializado
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.event
async def on_message(msg: discord.message):
    hora = discord.utils.utcnow().strftime("%H:%M:%S")  
    canalEnviar = bot.get_channel("ID DO CHAT AQ")
    loritta = bot.get_user("ID USUARIO LORITTA")
    mudae = bot.get_user("ID MUDAE")
    if msg.author == bot.user or msg.author == loritta or msg.author == mudae:
        return
    else:
        if msg.content.startswith("$wa") or msg.content.startswith("tu") or msg.content.startswith("$w") or msg.content.startswith("$h") or msg.content.startswith("$ha") or msg.content.startswith("$ma") or msg.content.startswith("$wx") or msg.content.startswith("$m") or msg.content.startswith("$mx") or msg.author == mudae:
            return
        else:
            if msg.attachments:
                for attachment in msg.attachments:
                    if attachment.content_type:
                        await canalEnviar.send(
                            f"{msg.author.name} enviou uma imagem:\n{attachment.url}"
                        )
                    else:
                        await canalEnviar.send(f"|{hora} | {msg.author.name} | \n| {msg.channel}: {msg.content}")
            else:
                await canalEnviar.send(f"|{hora} | {msg.author.name} | \n| {msg.channel}: {msg.content}")

#run the bot with the specified token
bot.run(token)