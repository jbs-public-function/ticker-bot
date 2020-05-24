from discord.ext import commands
import logging
logging.basicConfig(level=logging.INFO)

class BaseCog(commands.Cog):
    LABEL = 'BotBaseCog'
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(f'discord.cogs.{self.LABEL}')

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f'{self.LABEL} is alive.')

    def format_table(self, table):
        mx_length = 0
        for row in table:
            for col in row:
                mx_length = max(mx_length, len(str(col)))
        new_table = []
        for row in table:
            new_row = []
            for col in row:
                col = str(col)
                new_row.append(' ' + col +'\t' + ' '*((mx_length + 4) - len(col)))
            new_table.append(''.join(new_row))
        return new_table