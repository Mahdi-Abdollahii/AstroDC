
import random
import pkgutil
import numpy as np
import pandas as pd
import csv
from astropy import units
from astropy.coordinates import SkyCoord

class AstroDC:
    
    def __init__(self):
        pass
    
    #----------------------------------------------------------------------
    def Vizier_XMLCSV_to_CSV(file_address, file_name):
        
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
          try :  
            i[j] = float(i[j])
          except:
            pass

      # making DataFrame
      myFile = open(file_name + '.csv', 'w')
      writer = csv.writer(myFile)
      for data_list in list_array:
          writer.writerow(data_list)
      myFile.close()
      print( file_name + ".csv file of this data saved in local directory.")
        
        
    #----------------------------------------------------------------------
    def Stev_Isochrone_CSV(file_addres,file_name,Description=True):
      #reading file
      file_ = open(file_addres, "r")
      file_ = file_.read()

      #processing steps
      if Description == False :
        print(file_.split("isochrone tables")[0] + "isochrone dataframe" )
      list_of_Isochrone_for_all_years = file_.split("isochrone tables")[1].split('#')[1:-1]
      Number_Of_years = len(list_of_Isochrone_for_all_years )

      for i in range(Number_Of_years):
        list_of_Isochrone_for_all_years[i] = list_of_Isochrone_for_all_years[i].split('\n')
      for i in range(Number_Of_years):
        for j in range(len(list_of_Isochrone_for_all_years[i])):
          list_of_Isochrone_for_all_years[i][j] = list_of_Isochrone_for_all_years[i][j].split()

      # making csv file
      myFile = open(file_name + '.csv', 'w')
      writer = csv.writer(myFile)
      writer.writerow(list_of_Isochrone_for_all_years[0][0])

      for i in range(Number_Of_years):
        for data_list in list_of_Isochrone_for_all_years[i][1:]:
          writer.writerow(data_list)
      myFile.close()
      print( file_name + ".csv file of this data saved in local directory.")
        
    #----------------------------------------------------------------------    
    def Reg_file(Dataframe , First_column , Second_column ,
             Units = (units.hourangle, units.deg) ,
             Color = ("white", "black", "red", "green", "blue", "cyan", "magenta", "yellow") ,
             Size = 5 ,
             File_name = 'reg_file'):
      '''
        This function provides a reg file that helps you to illustrate the targets in the AstroDs9 application.

        dataframe: CSV file which contains survey data
        First_column: The column related to the first element of coordinate
        Second_column: The column related to the second element of coordinate
        Units: The unit of the coordinate in data
        Color : The color of circles illustrated in AstroDs9
        Size : The size of circle illusratd in AstroDs9
        File_name: The name of the final reg file
      '''
      # Prepairing data for reg file
      Cord_Deg = SkyCoord(Dataframe[First_column], Dataframe[Second_column], unit=( Units , units.deg))
      list_cor_deg = list(Cord_Deg)

      # making raw file and fill it by region data 
      f = open( File_name + '.reg' , "a")
      f.write('global color=' + Color + ' font="helvetica 10 normal" select=1 highlite=1 edit=1 move=1 delete=1 include=1 fixed=0 source' + '\n')

      for i in list_cor_deg :
        Ra_deg  = str(i).split('deg\n')[1].split('(')[1].split(')')[0].split(',')[0]
        Dec_deg = str(i).split('deg\n')[1].split('(')[1].split(')')[0].split(',')[1].split()[0]
        f.write( 'fk5;'+ 'circle' +'('+ Ra_deg + ',' + Dec_deg + ',' + str(Size)+ '")  #   '+"text=''" + '\n')
      f.close()
      print( File_name + ".reg file of this data saved in local directory.")
