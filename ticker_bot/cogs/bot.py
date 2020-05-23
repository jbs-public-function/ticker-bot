from discord.ext import commands
import logging
logging.basicConfig(level=logging.INFO)

class Bot(commands.Cog):
    LABEL = 'Core Bot'
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('discord.cogs')

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f'{self.LABEL} is alive.')

    