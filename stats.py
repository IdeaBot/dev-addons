from libs import command
from libs import discordstats
import re

FILEPATH="msgdumptemp.csv"

class Command(command.DirectOnlyCommand, command.AdminCommand):
    '''Generates and uploads CSV files of sent messages.
This command is currently disabled. A proper replacement will be completed soon (hopefully).

**Usage**
```@Idea statistics``` '''
    def matches(self, message):
        return re.search(r'stats|statistics', message.content, re.I)!=None

    def action(self, message, client):
        if message.author.id not in client.ADMINS:
            yield from send_func(message.channel, "No can do boss")
            return
        discordstats.dumpMessages(client, filename=FILEPATH, info="timestamp.isoformat(timespec='seconds'),author.name,id,channel.name,server.name")
        yield from self.send_file(message.channel,FILEPATH)
