#Soal 2
from abc import ABC, abstractmethod 
import random

class kingdom(ABC): 
  def __init__(self, nama, filum, kelas, ordo, famili, genus, spesies): 
    self.nama = nama 
    self.filum = filum 
    self.kelas = kelas
    self.ordo = ordo
    self.famili = famili
    self.genus = genus
    self.spesies = spesies 
  @abstractmethod 
  def klasifikasi(self): 
    pass    

class animalia(kingdom): 
  def klasifikasi(self): 
    print(f"{self.nama} (Kingdom Animalia)") 
    print(f"Phylum  : {self.filum}") 
    print(f"Class   : {self.kelas}")
    print(f"Order   : {self.ordo}")
    print(f"Family  : {self.famili}") 
    print(f"Genus   : {self.genus}")
    print(f"Species : {self.spesies}")  

pausbiru = animalia("Paus Biru", "Chordata", "Mammalia", \
                    "Cetacea","Balaenidae","Balaenoptera","musculus")
pausbiru.klasifikasi() 
