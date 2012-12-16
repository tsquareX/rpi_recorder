import RPi.GPIO as gpio
import time


"""
Python button class.
"""
class Button:
	def __init__(self, gpio_id, callback = None, callback_info = None):
		self.gpio_id = gpio_id
		self.callback = callback
		self.callback_info = callback_info

		gpio.setmode(gpio.BOARD)
		gpio.setup(gpio_id, gpio.IN, pull_up_down=gpio.PUD_UP)

		gpio.set_rising_event(gpio_id, enable=False)
                gpio.set_falling_event(gpio_id)


	def clear(self):
		gpio.event_detected(self.gpio_id)

	
	def was_pressed(self):
                print("in: " + str(gpio.input(self.gpio_id)))
		return gpio.event_detected(self.gpio_id)

        def poll(self, hz, callback, callback_info):
            cur_state = gpio.input(self.gpio_id) 

            while(1):
                s = gpio.input(self.gpio_id)
                if(s != cur_state):
                    print("State change: "  + str(s))
                    callback(callback_info)
                    cur_state = s


                time.sleep(1.0 / hz)
                



	
		
def press_event(press_info):
    print("Pressed: " + press_info)
	
		


if __name__ == "__main__" :
        gpio.cleanup()

        """
        gpio.setmode(gpio.BOARD)
        #pins = [ 7, 11, 12, 13, 15, 16, 22 ]
        pins = [ 11 ]

        for id in pins:
            gpio.setup(id, gpio.OUT)

        s = gpio.HIGH

        while(1):
            for id in pins :
                if(s == gpio.HIGH):
                    s = gpio.LOW
                else: 
                    s = gpio.HIGH

                print ("GPIO set: " + str(s))
                gpio.output(id, s)

            time.sleep(1)                
        """



	b = Button(11, None, None)
	b.clear()
        b.poll(20, press_event, "Test")

	

