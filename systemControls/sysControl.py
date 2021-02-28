import os
#import screen_brightness as sbc
from subprocess import call
# import voiceResponse
# from importlib import import_module


class SystemOperations:
    def __init__(self):
        super().__init__()
        # self.vol = vol
        # self.importedModule = import_module('/home/kitretsu/Repository/HCI/File-Management/voiceResponse.py')

    def change_volume(self, vol) -> int:
        flag = False

        while not flag:
            volume = vol  # input('What volume? > ')

            try:
                volume = int(volume)

                if (volume <= 100) and (volume >= 0):
                    call(["amixer", "-D", "pulse", "sset",
                          "Master", str(volume)+"%"])
                    flag = True
                    # self.importedModule.voice_response("Volume is now set to " + str(volume) + " percent")
                    print("Volume set to" + str(volume) + "%")
                    return volume

            except ValueError:
                pass
                # self.importedModule.voice_response("Sir, volume can be between 0 to 100 percent, please tell the appropriate value")

    def change_brightness(self, screen_brightness):  # -> int:
        # try:
        #     brightness = screen_brightness
        #     sbc.set_brightness(brightness)
        # except sbc.ScreenBrightnessError as error:
        #     print(error)

        # return brightness
        pass

    def sys_shutdown(self):
        os.system("shutdown -P +1")
        print("Your system will shutdown in 60 seconds")

    def sys_reboot(self):
        os.system("reboot")
        print("Your system will restart in 10 seconds")

    def sys_lock(self):
        pass


# obj = SystemOperations()
# obj.change_volume(25)
