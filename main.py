import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("DISCORD_TOKEN non trovato. Impostalo nel file .env.")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True


class OrizonBot(commands.Bot):
    async def setup_hook(self) -> None:
        await self.tree.sync()


bot = OrizonBot(
    command_prefix="!",
    intents=intents,
)


@bot.tree.command(name="ping", description="Verifica che il bot sia online.")
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Pong! Bot Online")


@bot.tree.command(name="server", description="Mostra informazioni sul server.")
async def server(interaction: discord.Interaction) -> None:
    guild = interaction.guild
    if guild is None:
        await interaction.response.send_message("Questo comando può essere usato solo in un server.")
        return

    embed = discord.Embed(
        title=f"ᴏʀɪᴢᴏɴᴍᴄ ɴᴇᴛᴡᴏʀᴋ",
        description=f"OrizonMC Network è un server minecraft Italiano",
        color=discord.Color.blue(),
    )
    await interaction.response.send_message(embed=embed)


@bot.event
async def on_ready() -> None:
    print(f"Connesso come {bot.user}")


bot.run(token)
