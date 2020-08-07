import signal
import sys
import time
import queue

from spotmicroai.lcd_screen_controller import LCD_16x2_I2C_driver
from spotmicroai.utilities.config import Config


i2c_address = int(Config().get(Config.LCD_SCREEN_CONTROLLER_I2C_ADDRESS), 0)

screen = LCD_16x2_I2C_driver.lcd(address=i2c_address)

screen.lcd_clear()

# Test BackLight
screen.backlight(0)
time.sleep(0.2)
screen.backlight(1)
# Test Text
