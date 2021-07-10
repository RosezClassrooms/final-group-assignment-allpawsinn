class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
   
   def getCar(self):
      car = Car()
      
      brand=self.__builder.getBrand()
      car.setBrand(brand)

      color = self.__builder.getColor()
      car.setColor(color)

      horsePower = self.__builder.getHorsePower()
      car.setHorsePower(horsePower)
 
      types=self.__builder.getType()
      car.setType(types)

      engine = self.__builder.getEngine()
      car.setEngine(engine)
      return car

      


# The whole product
class Car:
  def __init__(self):
    
    self.__horsePower = None
    self.__brand = None
    self.__color = None
    self.__type =None
    self.__engine = None

  options={'Brands':['Bmw','Jeep','Mercedes','Toyota'],
            'Colors':['Blue','Red','Night Blue','White','Grey'],
            'Horse Power':['500','700','900','1000'],
            'Types':['Hatchback','Coupe','Sedan'],
            'Engine':['Diesel','Gas','Oil']
          } 
  raceoptions={'Brands':['Bmw','Jeep','Mercedes','Toyota'],
            'Colors':['Blue','Red','Night Blue','White','Grey'],         
            'Types':['Hatchback','Coupe','Sedan']     
          } 
  mountainoptions={'Brands':['Bmw','Jeep','Mercedes','Toyota'],
            'Colors':['Blue','Red','Night Blue','White','Grey'],
            'Engine':['Diesel','Gas','Oil']
          } 

  cartypes = ['Casual','Racing','Mountain']
  def setHorsePower(self,horsePower):
    self.__horsePower = horsePower
  
  def setColor(self,color):
    self.__color = color

  def setBrand(self,brand):
    self.__brand = brand

  def setType (self,types):
    self.__type = types

  def setEngine (self,engine):
    self.__engine = engine


  def specification(self):

    print ("Brand: %s" % self.__brand.branding)
    print ("Color: %s" % self.__color.coloring)
    print ("Horse Power: %s" % self.__horsePower.horsePowering)
    print ("Type: %s" % self.__type.typing)
    print ("Engine: %s" % self.__engine.engining)
  

class Builder:
      def getHorsePower(self):pass
      def getColor(self):pass
      def getBrand(self):pass
      def getType(self):pass
      def getEngine(self):pass
    

class CasualBuilder(Builder):
  def __init__(self,brand,color,horsepower,types,engine):
    self.color = color
    self.horsepower =  horsepower
    self.brand =brand
    self.types = types
    self.engine = engine

  def getBrand(self):
    brand = Brand()
    brand.branding = self.brand
    return brand
  
  def getColor(self):
    color=Color()
    color.coloring = self.color
    return color

  def getHorsePower(self):
    horsePower = HorsePower()
    horsePower.horsePowering = self.horsepower
    return horsePower

  def getType(self):
    types = Types()
    types.typing = self.types
    return types

  def getEngine(self):
    engine = Engines()
    engine.engining = self.engine   
    return engine
class RaceBuilder(Builder):
  def __init__(self,brand,color,types):
    self.color = color
    self.horsepower =  2000
    self.brand =brand
    self.types = types
    self.engine = 'Oil'

  def getBrand(self):
    brand = Brand()
    brand.branding = self.brand
    return brand
  
  def getColor(self):
    color=Color()
    color.coloring = self.color
    return color

  def getHorsePower(self):
    horsePower = HorsePower()
    horsePower.horsePowering = self.horsepower
    return horsePower

  def getType(self):
    types = Types()
    types.typing = self.types
    return types

  def getEngine(self):
    engine = Engines()
    engine.engining = self.engine   
    return engine
class MountainBuilder(Builder):
  def __init__(self,brand,color,engine):
    self.color = color
    self.horsepower =  1000
    self.brand =brand
    self.types = 'Monster'
    self.engine = engine

  def getBrand(self):
    brand = Brand()
    brand.branding = self.brand
    return brand
  
  def getColor(self):
    color=Color()
    color.coloring = self.color
    return color

  def getHorsePower(self):
    horsePower = HorsePower()
    horsePower.horsePowering = self.horsepower
    return horsePower

  def getType(self):
    types = Types()
    types.typing = self.types
    return types

  def getEngine(self):
    engine = Engines()
    engine.engining = self.engine   
    return engine
# Car parts
class Brand:
  branding = None
class Color:
  coloring = None
class HorsePower:
  horsePowering = None
class Types:
  typing = None 
class Engines:
  engining = None


def main():
  director = Director()
  car=Car()
  powerlists=car.options['Horse Power']
  brandlist= car.options['Brands']
  colorlist = car.options['Colors']
  typelist =car.options['Types']
  enginelist = car.options['Engine']
  while True:
    print("--------------------------------------------------------------")
    for item in car.cartypes:
      print(item)
    cartype=input("Please select car type from the list:")
    while cartype not in car.cartypes:
      cartype=input("Please select car type from the list:")
      
    if cartype == 'Casual':
        for key in car.options.values():
          print(key)
    
        brand=input("Please select brand from the list:")
        while brand not in brandlist:
          print("This car is not available")
          brand=input("Please select brand from the list:")

        color=input("Please select color  from the list:")
        while color not in colorlist:
          print("This car is not available")
          color=input("Please select color from the list:")

        horsePower=input("Please select horse power  from the list:")
        while horsePower not in powerlists:
          print("This car is not available")
          horsePower=input("Please select horsePower from the list:")

        types=input("Please select types from the list:")
        while types not in typelist:
          print("This car is not available")
          types=input("Please select types from the list:")
          
        engine=input("Please select engine from list:")
        while engine not in enginelist:
          print("This car is not available")
          engine=input("Please select engine from the list:")
    elif cartype == 'Racing':
        for key in car.raceoptions.values():
          print(key)
      
        brand=input("Please select brand from the list:")
        while brand not in brandlist:
          print("This car is not available")
          brand=input("Please select brand from the list:")

        color=input("Please select color  from the list:")
        while color not in colorlist:
          print("This car is not available")
          color=input("Please select color from the list:")

        types=input("Please select types from the list:")
        while types not in typelist:
          print("This car is not available")
          types=input("Please select types from the list:")
            
    elif cartype == 'Mountain':
        for key in car.mountainoptions.values():
          print(key)
      
        brand=input("Please select brand from the list:")
        while brand not in brandlist:
          print("This car is not available")
          brand=input("Please select brand from the list:")

        color=input("Please select color  from the list:")
        while color not in colorlist:
          print("This car is not available")
          color=input("Please select color from the list:")
          
        engine=input("Please select engine from list:")
        while engine not in enginelist:
          print("This car is not available")
          engine=input("Please select engine from the list:")

    if (cartype==car.cartypes[0]):
      print("Building Casual Car")
      casualBuilder = CasualBuilder(brand,color,horsePower,types,engine)
      
      director.setBuilder(casualBuilder)
      casual = director.getCar()
      casual.specification()
      print ("")

    elif(cartype==car.cartypes[1]):
      print("Building Racing Car")
      raceBuilder = RaceBuilder(brand,color,types)
      
      director.setBuilder(raceBuilder)
      race = director.getCar()
      race.specification()

    elif(cartype==car.cartypes[2]):
      print("Building Mountain Car")
      mountainBuilder = MountainBuilder(brand,color,engine)
      
      director.setBuilder(mountainBuilder)
      mountain = director.getCar()
      mountain.specification()


    else:
      print("You entered invalid choice")

if __name__ == "__main__":
   main()