import json
from os.path import exists   # If file exists

class Json:
    CONFIG_FILE = "config.json"
    firstNames = []
    lastNames = []
    value = []
    pin = []
    bankStatement = []
    
    def SaveToJSON(self):
        data = {
            "config" : {
                "firstNames": self.firstNames,
                "lastNames": self.lastNames,
                "value": self.value, 
                "pin": self.pin
            }
        }
        with open(self.CONFIG_FILE, "w") as outfile:
            json.dump(data, outfile)

    def LoadFromJSON(self):
        if not exists(self.CONFIG_FILE):
            self.SaveToJSON()
            return
        try:
            with open(self.CONFIG_FILE) as json_file:
                data = json.load(json_file)
                self.firstNames = data["config"]["firstNames"]
                self.lastNames = data["config"]["lastNames"]
                self.value = data["config"]["value"]
                self.pin = data["config"]["pin"]
        except Exception as e:
            print("The config has a wrong format. Delete the file and a new one will be generated. Error: {}" .format(e))