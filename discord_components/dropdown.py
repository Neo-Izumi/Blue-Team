import nextcord
from nextcord.ui import View, Select
from nextcord import Interaction

# from nextcord import slash_command, Interaction
# from nextcord.ext.commands import Cog

class select_tasks(Select):
    
    def __init__(self):
        tasks = [
            nextcord.SelectOption(lablel = 'FPT requests from strange IP addresses', description = 'Task No.1'),
            nextcord.SelectOption(lablel = 'Penatration containing malware', description = 'Task No.2'),
            nextcord.SelectOption(lablel = 'Report events', description = 'Task No.3'),
            nextcord.SelectOption(lablel = 'Working from home', description = 'Task No.4'),
        ]
        super().__init__(placeholder = 'All taskes', min_value = 1, max_value = 1, options = tasks)
        
    async def callback(self, interaction: Interaction):
        await interaction.response.send_message(f'You chose {self.value} from these tasks.')
        if self.values[0] == 'FPT requests from strange IP addresses':
            return await interaction.followup.send('Ok let\'s dive into the network configuration.')
        elif self.values[0] == 'Penatration containing malware':
            return await interaction.followup.send('Hmmm... let\'s see what can we deal with that.')
        elif self.values[0] == 'Report events':
            return await interaction.followup.send('Yes!! Making a professional report is one of our favorite task ha')
        elif self.values[0] == 'Working from home':
            return await interaction.followup.send('Ok ... building connection to the server is quite simple though')

class list_tasks_view(View):
    
    def __init__(self):
        super().__init__()
        self.add_item(select_tasks())
        
        
# class incident_response(Cog): 
    
#     def __init__(self, bot):
#         self.bot = bot
        
#     ID = 1035593393381838888
    
#     @slash_command(name='list_tasks', description='list all tasks you need to do', guild_ids=[ID])
#     async def list_tasks(self, interaction: Interaction):
#         tasks = list_tasks_view()
#         await interaction.response.send_message('Here are all your tasks', view = tasks)
        
# def setup(bot):
#     bot.add_cog(incident_response(bot))
                        