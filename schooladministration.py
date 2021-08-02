import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerrow(info_list)
        
condition = True

while(condition):
    student_info = input("Enter student information in the following format (Name Age Contact_Number E-mail_ID): ")
    print("Entered information:" + student_info)

        


    
    
        
      
         
      

       

       