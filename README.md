# Discord roles bot

## Packages

python version 3.10.5
to start, go to this directory in cmd, "py main.py"


discord.py, pip install discord.py
dotenv, pip install dotenv

## Configuration

You're gonna need a bot token, which you can generate your own and paste it into the configuration file. (config.env)
You will have full control over the customization of the bot that way.

You alse need to configure the name of the bot role, like this:

BOT_ROLE=Whatever

Another thing that needs to be configured is the prefix that the bot responds to:

PREFIX=ab!

Roles also need to be configured, this by the following format:
First the emoji, which can be any discord supported emoji, and server emojis, followed by a space, a dash, and another space. 
After that, the name of the role, this is case sensitive, end with a comma, if it's not the last item.

ROLES=✅ - testRole1, ❌ - testRole2, :owenPog: - testRole3

Last is the message that the bot says in the role message.

MESSAGE=This is the message that's before the roles

## Commands

Let's assume the prefix you chose is "ab!", since that's the default.

### roles

This command is called by "ab!roles" and returns a message that lists the possible emoji choices with the corresponding role.
Users can respond to the message with one of the emoji's and they will be rewarded with the corresponding role.

### reloadenv

This command is called by "ab!reloadenv", which will update the bot with the current configuration in the config.env file.
This means you can update the roles or the message while the bot is still running, this prevents the bot from having to shut down to make changes.

## Note this
The roles message stops working after the bot has been restarted, whenever you restart the bot you should delete the old bot message and call the roles command again.

