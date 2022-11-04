import nextcord

from async_timeout import timeout
from nextcord.ui import View, Button, button
from nextcord import Interaction, ButtonStyle

class roles(View):
    def __init__(self):
        super().__init__(timeout = 5)
        self.value = None
        
    @nextcord.ui.button(label = 'alert analysis', style = ButtonStyle.red)
    async def alert_analysis(self, button: Button, interaction: Interaction):
        message = '''Alert analysis: are the tier-1 tasks, usually mentioned as collecting, checking and analysing the whole system events, log, alert, ...
Today, you will just need to check the log files, taskes assigned from network manager and email from other department.'''
        await interaction.response.send_message(message, ephemeral=False)
        self.value = 'alert'
        self.stop()
    
    @nextcord.ui.button(label = 'incident response', style = ButtonStyle.green)
    async def incident_response(self, button: Button, interaction: Interaction):
        message = '''Incident response: are the tier-2 tasks, usually mentioned as deeply analysing the alert, responding and giving the solution to the incident
Today, we will give you some useful tools, shortly introduce you guy to these tools and what you can do with the alert at the tier_1 report'''
        await interaction.response.send_message(message, ephemeral=False)
        self.value = 'response'
        self.stop()
        
    @nextcord.ui.button(label = 'simulating vulnarable environment', style = ButtonStyle.gray)
    async def environment(self, button: Button, interaction: Interaction):
        message = '''Simulating the vulnarable environment'''
        await interaction.response.send_message(message, ephemeral=False)
        self.value = 'environment'
        self.stop()
    
    