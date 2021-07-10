from abc import ABC, abstractmethod
import time

class Command(ABC):
  @abstractmethod
  def execute(self):
    pass

class CustomerIn(Command):
  def __init__(self, store):
    self.store = store

  def execute(self):
    self.store.customer_in()

class CustomerOut(Command):
  def __init__(self, store):
    self.store = store

  def execute(self):
    self.store.customer_out()

class LightsOn(Command):
  def __init__(self, lights):
    self.lights = lights

  def execute(self):
    self.lights.lights_on()

class LightsOff(Command):
  def __init__(self, lights):
    self.lights = lights

  def execute(self):
    self.lights.lights_off()


class Store:
  def __init__(self):
    self.customer = 0
  
  def customer_in(self):
    self.customer += 1
    print("\nA customer entered the store! Customer Inside: " + str(self.customer) + "\n")

  def customer_out(self):
    if(self.customer > 0):
      self.customer -= 1
      print("\nA customer left the store! Customer Inside: " + str(self.customer) + "\n")
    else:
      print("\nThere is no customer in store.\n")

class Lights:
  def lights_on(self):
    print("\nLights On!\n")

  def lights_off(self):
    print("\nLights Off\n")


class Invoker:
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()

if __name__ == '__main__':
  store = Store()
  lights = Lights() 
  customer_in_cmd = CustomerIn(store)
  customer_out_cmd = CustomerOut(store)

  lights_on_cmd = LightsOn(lights)
  lights_off_cmd = LightsOff(lights)

  cmd = 'a'
  print("############# Store Crowd Check System #############\n\nType '+' to incoming customer\nType '-' for exiting customer\nType 'O' to Open Lights\nType 'C' to Close Lights\n\nType 'Q' to exit.\n")

  while(cmd.upper() != 'Q'):
    time.sleep(0.4)
    
    cmd = input("Command: ")

    if(cmd.upper() == '+'):
      cust_in_invoker = Invoker(customer_in_cmd)
      cust_in_invoker.invoke()
    elif(cmd.upper() == '-'):
      cust_out_invoker = Invoker(customer_out_cmd)
      cust_out_invoker.invoke()
    elif(cmd.upper() == 'O'):
      door_open_invoker = Invoker(lights_on_cmd)
      door_open_invoker.invoke()
    elif(cmd.upper() == 'C'):
      door_close_invoker = Invoker(lights_off_cmd)
      door_close_invoker.invoke()

  