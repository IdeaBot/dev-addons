from libs import reaction #as reactioncommand

class Reaction(reaction.ReactionAddCommand, reaction.ErrorlessReaction):
    '''Gets the ID of an emoji

**Usage**
React to a message containing the word "id" with the emoji you want the ID of

**NOTE:** This is a debug command
**NOTE2:** This command will be removed with the next point release (v1.0)'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.emoji=None

    def matches(self, reaction, user):
        return " id " in reaction.message.content.lower() or " id" == reaction.message.content.lower()[-3:] or "id " == reaction.message.content.lower()[:3] or "id"==reaction.message.content.lower()

    def action(self, reaction, user):
        try:
            yield from self.send_message(reaction.message.channel, "Name: `" + reaction.emoji.name + "`\nID: `" + reaction.emoji.id + "`")
        except AttributeError:
            yield from self.send_message(reaction.message.channel, reaction.emoji + " doesn't have an ID")
