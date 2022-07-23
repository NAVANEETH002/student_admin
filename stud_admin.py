import csv

def write_into_csv(info_list):
    with open('Student_info.csv','a',newline = '') as csv_file:
        writer  =csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact_number","Group"])

        writer.writerow(info_list)

if __name__ == "__main__":
    condition = True
    while(condition):
        student_info = input("Enter Student Information in format(Name Age Contact_number Group) : ")
        print("Entered Information : " + student_info)


        student_info_list = student_info.split(' ')
        print("Splited values are : " + str(student_info_list))

        print("Entered Information is : \n\t Name : {} \n\t Age : {} \n\t Contact_number : {} \n\t Group : {}"
            .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        check = input("Is info correct (yes/no) : ")
        if check == "yes":
            write_into_csv(student_info_list)
            condition_check = input("Enter (yes/no) to add another student : ")

            if condition_check == "yes":
                condition = True
            elif condition_check == "no":
                condition = False
        elif check == "no":
            print("Re-Enter values : ")
