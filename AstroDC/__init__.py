
import random
import pkgutil
import numpy as np
import pandas as pd
import csv

class AstroDC:
    
    def __init__(self):
        pass
    
    def XML_CSV_to_CSV(file_address, file_name):

      #reading file
      file_ = open(file_address, "r")
      file_ = file_.read()
      list_array = file_.split("<DATA>")[1].split("</DATA>")[0].split("\n")[1:-1]
      for i in range(len(list_array)):
        list_array[i] = list_array[i].split(';')

      for i in range(len(list_array[0])):
        list_array[0][i] = list_array[0][i]+'('+list_array[1][i]+')'

      del list_array[1:3]

      #filling empty ...
      for i in list_array[1:]:
        for j in range(len(i)):
          if i[j] == "        ":
            i[j] = np.nan
          i[j] = float(i[j])

      # making DataFrame
      myFile = open(file_name + '.csv', 'w')
      writer = csv.writer(myFile)
      for data_list in list_array:
          writer.writerow(data_list)
      myFile.close()
      print(" .csv file of this data saved in local directory.")
    
    def isochrom_csv(file_addres,file_name):

      #reading file
      file_ = open(file_addres, "r")
      file_ = file_.read()

      #processing steps
      print(file_.split("isochrone tables")[0] + "isochrone dataframe" )
      list_of_Isochrom_for_all_years = file_.split("isochrone tables")[1].split('#')[1:-1]
      Number_Of_years = len(list_of_Isochrom_for_all_years )

      for i in range(Number_Of_years):
        list_of_Isochrom_for_all_years[i] = list_of_Isochrom_for_all_years[i].split('\n')
      for i in range(Number_Of_years):
        for j in range(len(list_of_Isochrom_for_all_years[i])):
          list_of_Isochrom_for_all_years[i][j] = list_of_Isochrom_for_all_years[i][j].split()

      # making csv file
      myFile = open(file_name + '.csv', 'w')
      writer = csv.writer(myFile)
      writer.writerow(list_of_Isochrom_for_all_years[0][0])

      for i in range(Number_Of_years):
        for data_list in list_of_Isochrom_for_all_years[i][1:]:
          writer.writerow(data_list)
      myFile.close()
