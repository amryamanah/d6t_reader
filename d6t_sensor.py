### REMEMBER TO MAKESURE PIGPIOD run
### TO check "sudo ps aux | grep pigpiod"
### if only one line output
### start pigpiod with "sudo pigpiod"

import smbus
import sys
import getopt
import time
import pigpio

from result_writer import *

from IPython import embed


i2c_bus = smbus.SMBus(1)
OMRON_1 = 0x0a
OMRON_BUFFER_LENGTH = 35
temperature_data=[0]*OMRON_BUFFER_LENGTH

class D6T(object):
  def __init__(self):
    self.pi = pigpio.pi()
    self.handle = None

  def open(self):
    self.handle = self.pi.i2c_open(1, OMRON_1)
  
  def calculate_temp(self, byte_low, byte_high):
    return 256 * byte_high + byte_low
  
  def get_d6t_result(self):
    result = [x for x in range(18)]
    byte_result = bytearray(OMRON_BUFFER_LENGTH)
    
    i2c_bus.write_byte(OMRON_1, 0x4c)
    (bytes_read, byte_result) = self.pi.i2c_read_device(self.handle, len(byte_result))

    assert bytes_read == 35, "Bytes read not equal to 35"

    for x in range(len(result)-1):
      low_index = x * 2
      high_index = low_index + 1
      result[x] = self.calculate_temp(byte_result[low_index], byte_result[high_index])
    
    result[17] = byte_result[34]
	
    return result

if __name__ == "__main__":


  lst_result = []
  create_csv_result()

  a = D6T()
  a.open()

  count = 0
  while count < 5:
    start = time.time()
    d6t_result = a.get_d6t_result()
    end = time.time()
    print("{}> Time taken : {}".format(count + 1,(end - start)))
    print("{} > {}".format(count + 1, d6t_result))
    lst_result.append(form_dct_result(d6t_result))
    count += 1
    time.sleep(0.2)
  
  write_csv_result(lst_result)

  print("done")
