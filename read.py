import time
import Adafruit_MCP230xx as MCP
import threading

mcp = MCP.Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)
delay = 0.3
shiftBit= 3
pinOut=9
#rest call routine
def call_rest_put(pin, val):
  print "calling rest put for pin %s with val %d" % (pin, val)
  #test
  mcp.output(pinOut,0)
  time.sleep(1)
  mcp.output(pinOut,1)

#async polling
def read_from_input(pinIn):
  print "Thread starting monitor input on pin %d with a delay of %f" % (pinIn, delay)
  while (True):
    prevVal = (mcp.input(pinIn) >> pinIn)
    time.sleep(delay);

    #if change status detected throw the rest call
    if ((mcp.input(pinIn) >> pinIn)==0 and prevVal==1) or ((mcp.input(pinIn) >> pinIn)==1 and prevVal==0):
      call_rest_put(pinIn,(mcp.input(pinIn) >> pinIn))
#    print "%d: %x" % (pinIn, mcp.input(pinIn) >> pinIn) 


for pin in range(8, 16):
  mcp.config(pin, mcp.OUTPUT)
  mcp.output(pin, 1)

for pin in range(0, 8):
  mcp.config(pin, mcp.INPUT)
 
  # Set pin pinIn to input with the pullup resistor enabled
  mcp.pullup(pin, 1)
  #Thread settings
  thread = threading.Thread(target=read_from_input, args=(pin,))

  #this set thread to daemon
  thread.daemon = True
  thread.start()

#hack to prevent exit
while True:
    time.sleep(10)
