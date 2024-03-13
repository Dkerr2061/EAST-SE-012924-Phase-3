import ipdb

class Car:
  def __init__(self, make, model, year, horn_volume= 1):
      self.make= make
      self.model= model
      self.year= year
      self.horn_volume= horn_volume

  @property
  def year(self):
     return self._year
  
  @year.setter
  def year(self, year_param):
     if(isinstance(year_param, int)) and (1900 <= year_param <= 2023):
        self._year = year_param
     else:
        raise ValueError ("Year must be an integer and must be between 1900 and 2023!")
     
  @property
  def horn_volume(self):
     return self._horn_volume
  
  @horn_volume.setter
  def horn_volume(self, horn_volume_param):
    if(isinstance(horn_volume_param, int)):
        self._horn_volume = horn_volume_param
    else:
      raise ValueError ("Horn volume must be an integer!")
    
  @property
  def make(self):
     return self._make
  
  @make.setter
  def make(self, make_param):
    if(isinstance(make_param, str)) and (len(make_param) >= 3):
        self._make = make_param
    else:
       raise ValueError ("Make must be a string and must be at least 3 characters long!")
    
  def honk_horn(self):
     print(f"BEEP BEEP {'!' * self.horn_volume}")

car1 = Car('Honda', 'Civic', 2023, 8)

ipdb.set_trace()