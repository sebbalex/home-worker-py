import time
import Adafruit_MCP230xx as MCP
# Use busnum = 0 for older Raspberry Pi's (256MB)
# mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)
# Use busnum = 1 for new Raspberry Pi's (512MB with mounting holes)
mcp = MCP.Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)

pin = 5
# Set pins 0, 1 and 2 to output (you can set pins 0..15 this way)
mcp.config(pin, mcp.OUTPUT)
mcp.config(1, mcp.OUTPUT)
mcp.config(2, mcp.OUTPUT)
 
# Set pin 3 to input with the pullup resistor enabled
mcp.pullup(3, 1)
# Read pin 3 and display the results
print "%d: %x" % (3, mcp.input(3) >> 3)
 
# Python speed test on output 0 toggling at max speed
while (True):
  print "accendo lo %d" % pin
  mcp.output(pin, 0)  # Pin 0 High
  time.sleep(1);
  print "spengo lo %d" % pin
  mcp.output(pin, 1)  # Pin 1 Low
  time.sleep(1);

