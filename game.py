from libs import command
import re
import discord

class Command(command.DirectOnlyCommand, command.AdminCommand):
    '''Set the game status of Idea.
You must be a bot admin for this to work; you probably don't have permission to use this command.

**Usage**
```@Idea set game to <title>```
Where
**`<title>`** is the title of the game to play
'''
    def matches(self, message):
        return self.collect_args(message) is not None and message.server is not None

    def action(self, message, bot):
        if message.author.id not in bot.ADMINS:
            yield from self.send_message(message.channel, 'You don\'t have permission to use this command')
            return
        args = self.collect_args(message)
        type = 0
        if args.group(1):
            type = int(args.group(1))
        name = args.group(2)
        game = discord.Game(name=name, type=type)
        yield from bot.change_presence(game=game)
        self.public_namespace.game_file.content['name'] = name
        self.public_namespace.game_file.content['type'] = type
        yield from self.send_message(message.channel, 'Success! Game is now `%s`' % str(game))

    def collect_args(self, message):
        return re.search(r'\bset\s*game(?:\s*to)?\s+(?:(\d)\s+)(.+)', message.content, re.I)
