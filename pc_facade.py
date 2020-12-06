class Boot(object):
   
   @staticmethod
   def boot_up():
      return True

class Cpu(object):

   def __init__(self):
      self.cpu_freq = 0
      self.cpu_power = 0

   def normal(self):
      self.cpu_freq = 4700
      self.cpu_power = 65

   def boost(self):
      self.cpu_freq = 5200
      self.cpu_power = 90
   
   def turnoff(self):
      self.cpu_freq = 0
      self.cpu_power = 0

class PowerSupply(object):
   
   def __init__(self):
      self.wattage = 500
   
   @property
   def watt(self):
      return self.wattage
   
   @watt.setter
   def watt(self, wtt):
      self.wattage = wtt

class GraphicsCard(object):

   def __init__(self):
      self.gpu_freq = 0
      self.gpu_power = 0

   def normal(self):
      self.gpu_freq = 5800
      self.gpu_power = 300

   def boost(self):
      self.gpu_freq = 6300
      self.gpu_power = 400

   def turnoff(self):
      self.gpu_freq = 0
      self.gpu_power = 0

class Ram(object):

   def __init__(self):
      self.ram_freq = 0
      self.ram_power = 0

   def normal(self):
      self.ram_freq = 3000
      self.ram_power = 50

   def boost(self):
      self.ram_freq = 4200
      self.ram_power = 100

   def turnoff(self):
      self.ram_freq = 0
      self.ram_power = 0




# Facade
class Computer(object):
   
  def __init__(self):
    self.booting = Boot()
    self.cpu = Cpu()
    self.gpu = GraphicsCard()
    self.psu = PowerSupply()
    self.ram = Ram()
  
  @property
  def sys_watt(self):
    return self.ram.ram_power + self.cpu.cpu_power + self.gpu.gpu_power
  
  def start(self):
    print("\n PC is started in normal mode.")
    if self.booting.boot_up():
        self.cpu.normal()
        self.gpu.normal()
        self.ram.normal()
    else:
        print("Error: PC didn't boot.")

  def boost_mode(self):
    print("\n Switching to boost mode.")
    self.cpu.boost()
    self.gpu.boost()
    self.ram.boost()

    if(self.psu_is_enough()):
      

      print("System boosted successfully.")
    
    else:
      print("System is failed to boost... \n System is revert to back!")
      self.normal_mode()


  def normal_mode(self):
    print("\n Switching to normal mode.")
    self.cpu.normal()
    self.gpu.normal()
    self.ram.normal()

  def stop(self):
    print("System is shutting down..")
    self.cpu.turnoff()
    self.gpu.turnoff()
    self.ram.turnoff()

  def new_psu(self, wtt):
    self.psu.watt = wtt

  def psu_is_enough(self):
  
    if int(self.psu.wattage) >= int(self.sys_watt):
        print("PSU is " + str(self.psu.wattage) + "W but system draws " + str(self.sys_watt) + "W ")
        return True
    else:
        print("PSU is " + str(self.psu.wattage) + "W but system draws " + str(self.sys_watt) + "W ")
        return False

  def info(self):
    if(self.cpu.cpu_freq == 4700):
      print("System is running in Normal Mode with \nCPU Frequency: " + str(round(self.cpu.cpu_freq/1000,3)) + " GHz \nGPU Frequency: " + str(self.gpu.gpu_freq) + " MHz \nRAM Frequency: " + str(self.ram.ram_freq) + " MHz \nTotal System Power Draw: " + str(self.sys_watt) + " W\n Power Supply Wattage: " + str(self.psu.wattage) + " W\n\n")
      return False
    else:
      print("System is running in Normal Mode with \nCPU Frequency: " + str(round(self.cpu.cpu_freq/1000,3)) + " GHz \nGPU Frequency: " + str(self.gpu.gpu_freq) + " MHz \nRAM Frequency: " + str(self.ram.ram_freq) + " MHz \nTotal System Power Draw: " + str(self.sys_watt) + " W\n Power Supply Wattage: " + str(self.psu.wattage) + " W\n\n")
      return True

				
# the main function is the Client
def main():
   pc = Computer()
   val = input("Type R to Start Computer: ")
   if(val.upper() == 'R'):
    pc.start()
    print("Welcome to the High OS! \n")
    pc.info()
   while(val.upper() != 'Q'):

    val = input("Type 'B' to Boost your PC, but your PC will consume more power.\nType 'N' to switch power mode to Normal.\nType 'I' to see your PC's current state.\nType 'P' to insert new Power Supply to your PC.\n\nType 'Q' to shut your pc down.")

    if(val.upper() == 'B'):
      pc.boost_mode()
    elif(val.upper() == 'N'):
      pc.normal_mode()
    elif(val.upper() == 'I'):
      pc.info()
    elif(val.upper() == 'P'):
      watt = input("\nEnter the new Power Supply Wattage: ")
      pc.new_psu(watt)

if __name__ == "__main__":
   main()