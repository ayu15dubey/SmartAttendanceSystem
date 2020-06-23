
# Writing to an excel  
# sheet using Python 
import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

sheet1.write(0, 0, 'NAME') 
  
sheet1.write(1, 0, 'Ayush') 
sheet1.write(2, 0, 'shubham')
sheet1.write(3, 0, 'Mazhar')
sheet1.write(4, 0, 'vishal')

 
sheet1.write(0, 2, 'PRESENT') 
 
  

sheet1.write(1, 2, 'yes') 
sheet1.write(2,2, 'no')
sheet1.write(3,2, 'no')
sheet1.write(4,2, 'no')
  
wb.save('xlwt example.xls')     
