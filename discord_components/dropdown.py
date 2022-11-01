import nextcord
from nextcord.ui import View, Select
from nextcord import Interaction

# from nextcord import slash_command, Interaction
# from nextcord.ext.commands import Cog

class list_tasks(Select):
    
    def __init__(self):
        tasks = [
            nextcord.SelectOption(lablel = 'FPT requests from strange IP addresses'),
            nextcord.SelectOption(lablel = 'Penatration containing malware'),
            nextcord.SelectOption(lablel = 'Report events'),
            nextcord.SelectOption(lablel = 'Working from home')
        ]
        super().__init__(placeholder = 'All taskes', min_value = 1, max_value = 1, options = tasks)
        
        async def callback(self, interaction: Interaction):
            if self.values[0] == 'FPT requests from strange IP addresses':
                return await interaction.response.send_message('Ok le\'s dive into the network configuration.')
            elif self.values[0] == 'Penatration containing malware':
                return await interaction.response.send_message('Hmmm... let\'s see what happened.')
            elif self.values[0] == 'Report events':
                return await interaction.response.send_message('Yes!! Making a professional report is one of our favorite task ha')
            elif self.values[0] == 'Working from home':
                return await interaction.response.send_message('Ok ... building connection to the server is quite simple though')

class list_tasks_view(View):
    
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(list_tasks())
        
        
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
                        