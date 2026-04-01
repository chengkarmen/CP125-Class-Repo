import csv
def bmi_average_height(input_file):
    bmi = open(input_file, 'r', newline = "")
    reader_bmi = csv.reader(bmi)
    print(reader_bmi)
    next(reader_bmi)
    height = 0
    for row in reader_bmi:
        height += float(row[1])
    
    if height != 0:
        print(f"Average height: {height / len(reader_bmi)}")

    bmi.close()

def add_bmi_data(input_file):
    bmi = open(input_file, 'a+', newline = "")
    writer_bmi = csv.writer(bmi)
    new_gender = input("Enter gender: ")
    new_height = float(input("Enter height: "))
    new_weight = float(input("Enter weight; "))
    new_bmi = float(input("Enter BMI: "))
    writer_bmi.writerow(f"{[new_gender, new_height, new_weight, new_bmi]}\n")
    
    reader_bmi = csv.reader(bmi)
    print(reader_bmi)

    bmi.close()


bmi_average_height("labs/bmi.csv")
add_bmi_data("labs/bmi.csv")
