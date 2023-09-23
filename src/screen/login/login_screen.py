from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import (ObjectProperty,
                             BooleanProperty,
                             StringProperty,
                             ColorProperty)

from src.data.collect.data_collector import DataCollector

from src.screen.login.dialogs.update_dialog import UpdateDialog
from src.screen.login.dialogs.off_num_dialog import OffNumDialog


from src.data.retrieve.get_warning_message_info import (
    getWarningMessageInfo
    )
from src.screen.login.dialogs.utils.update_dialog_util import showDialog
from src.data.manager.config_manager import getConfig
from src.data.manager.design_manager import updateFontSize
from src.share.trace import TRACE

class LoginScreen(Screen):
    offNumTextFieldObj = ObjectProperty(None) # object in kv
    loginButtonObj = ObjectProperty(None) # object in kv
    updateButtonObj = ObjectProperty(None) # object in kv
    warningMessage = StringProperty() # binding
    warningMessageColor = ColorProperty() # binding
    offNum = StringProperty() # binding
    updateDone = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()
        
        config = getConfig()
        self.offNum = config['OFFICIAL_NUMBER_STARTUP']
        self.setWarningMessage()

    def setWarningMessage(self):
        warningMessageInfo = getWarningMessageInfo()
        self.warningMessage = warningMessageInfo['message']
        self.warningMessageColor = warningMessageInfo['color']

    def changeDefaultOffNum(self):
        currentOffNum = self.offNumTextFieldObj.text
        offNumDialog = OffNumDialog(currentOffNum, self)
        offNumDialog.open()

    def changeCurrentOffNum(self, newOffNum):
        self.offNumTextFieldObj.text = newOffNum

    def loginButton(self):
        offNum = self.offNumTextFieldObj.text
        try:
            self.manager.switchToMainScreen(offNum)
        except Exception as e:
            errorMessage = str(e)
            TRACE(errorMessage)
            self.updateDialog = UpdateDialog()
            self.updateDialog.text = errorMessage
            self.updateDialog.open()

    def updateButton(self):
        self.updateDialog = UpdateDialog()
        self.update()

    def increaseFontSize(self):
        oldValue = int(self.app.loginScreenFontSize[:-2])
        newValue = oldValue + 1
        updateFontSize('LOGIN_SCREEN_FONT_SIZE', newValue)
        self.app.loginScreenFontSize = str(newValue) + 'dp'

    def decreaseFontSize(self):
        oldValue = int(self.app.loginScreenFontSize[:-2])
        newValue = oldValue - 1
        updateFontSize('LOGIN_SCREEN_FONT_SIZE', newValue)
        self.app.loginScreenFontSize = str(newValue) + 'dp'

    @showDialog
    def update(self):
        dataCollector = DataCollector()
            
        finished = False
        updateResult = dict()
        self.updateDialog.text = 'Dropbox sinkronizacija'
        while not finished:
            updateResult = dataCollector.keepCollectingData()
            finished = updateResult['finished']
            self.updateDialog.text = updateResult['message']
   
        self.updateDialog.dotsTimer.cancel()
        success = updateResult['success']
        error = updateResult['error']
        errorMessage = updateResult['errorMessage']
        
        if success:
            self.setWarningMessage()
            self.updateDialog.text = 'Sluzbe azurirane!'
            
        elif error:
            self.updateDialog.text = 'GRESKA! Dokumenti popravljeni.\n' \
                                    + errorMessage
        else:
            self.updateDialog.text = 'Sluzbe jos nisu izasle!'

        self.updateDialog.auto_dismiss = True













            

