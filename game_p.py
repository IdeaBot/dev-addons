from libs import plugin
from libs import dataloader
import re
import discord

class Plugin(plugin.AdminPlugin, plugin.OnReadyPlugin):
    '''Set the game status of Idea after a restart.
See the `game` command for more information

(This plugin just makes the current game persist between restarts)'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.public_namespace.game_file = dataloader.loadfile_safe(self.config['game'])
        if not isinstance(self.public_namespace.game_file.content, dict):
            self.public_namespace.game_file.content = {'name':None, 'type':None, 'url':None}

    async def action(self):
        if self.public_namespace.game_file.content['name']:
            game = discord.Game(name=self.public_namespace.game_file.content['name'], type=self.public_namespace.game_file.content['type'], url=self.public_namespace.game_file.content['url'])
            await self.bot.change_presence(game=game)
        self.period = -1 # prevent repeating

    def shutdown(self):
        self.public_namespace.game_file.save()
