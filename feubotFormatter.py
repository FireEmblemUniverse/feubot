from discord.ext.commands import HelpCommand

class FeubotFormatter(HelpCommand):
    def filter_command_list(self):
        return sorted(super().filter_command_list(), key=lambda e: str.lower(e[0]))

