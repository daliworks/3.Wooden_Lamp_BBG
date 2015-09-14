import time
#from logo import print_seeedstudio
import grove_chainable_rgb_led
from adxl345 import ADXL345
import grove_i2c_adc
CLK_PIN = "P9_22"
DATA_PIN = "P9_21"
NUMBER_OF_LEDS = 1


if __name__ == "__main__":

    adxl345 = ADXL345()
    rgb_led = grove_chainable_rgb_led.ChainableLED(CLK_PIN, DATA_PIN, NUMBER_OF_LEDS)
    button = grove_i2c_adc.I2cAdc()
    Red = 255
    Green = 255
    Blue = 255
    while True:
        try:
            if button.read_adc() >= 2000:
            
                axes = adxl345.getAxes(True)
                Red = 128 + 128 * axes['x'] 
                Green = 128 + 128 * axes['y'] 
                Blue = 128 + 128 * axes['z'] 
            
                print "   x = %.3fG" % ( axes['x'] )
                print "   y = %.3fG" % ( axes['y'] )
                print "   z = %.3fG" % ( axes['z'] )
                print "Red = %d " % Red
                print "Green = %d " % Green
                print "Blue = %d " % Blue
            
                print "button = %d " % button.read_adc();
         
                rgb_led.setColorRGB(0, int(Red),int(Green),int(Blue))
                time.sleep(.01)
            rgb_led.setColorRGB(0, int(Red),int(Green),int(Blue))
        except KeyboardInterrupt:
            rgb_led.setColorRGB(0, 0, 0, 0)
            break

        except IOError:
            print "Error"