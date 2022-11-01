import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext.commands import Cog


class alert_analysis(Cog):

    def __init__(self, bot):
        self.bot = bot
    
    check = False
    mess = False
    process = 0 

    ID = 1035593393381838888

    @slash_command(name='log_files', description='check log files', guild_ids=[ID])
    async def log_files(self, interaction: Interaction):
        message = 'Omg!!! after checking log files, we detected that there are two problems\nThe first is some FTP requests from an unusual ipaddress\nThe other one is a penatration containing malware towards to your organization server.'
        await interaction.response.send_message('Performing analysing process-----------', ephemeral = False)
        await interaction.followup.send('Done!!!', ephemeral = False)
        await interaction.followup.send(message, ephemeral = False)
        self.check = True
        self.process += 1
        if self.mess == False: 
            await interaction.followup.send('Now, let\'s check other messages or select \'incident response\' for more information', ephemeral = False)
            
    @slash_command(name='other_messages', description='check log files', guild_ids=[ID])
    async def other_messages(self, interaction: Interaction):
        message1 = 'Hmmm... an employee from other department need to connect to server because of his working-from-home period of time'
        message2 = 'Oh!! and your manager ask you to make a report of all events happened last week as well\nSo many things you need to do today ha!'
        await interaction.response.send_message(message1, ephemeral = False)
        await interaction.followup.send(message2, ephemeral = False)
        self.mess = True
        self.process += 1
        if self.check == False: 
            await interaction.followup.send('Now, let\'s check log files or select \'incident response\' for more information', ephemeral = False)

def setup(bot):
    bot.add_cog(alert_analysis(bot))