import csv
def write():
    with open("countries.csv","w",newline='') as fw :
        cwriter=csv.writer(fw)
        cwriter.writerow(['COUNTRY','CAPITAL','CODE'])
        cwriter.writerow(['India','New Delhi','II'])
        cwriter.writerow(['US','Washington D.C.','UU'])
        cwriter.writerow(['Malaysia','Kuala Lumpur','MM'])
        cwriter.writerow(['France','Paris','FF'])
        print("Data written to csv file ...")

def search():
    print("Contents of countries.csv file where capital name is more than 6 characters in length : ")
    with open("countries.csv",'r') as fr:
        creader=csv.reader(fr)
        next(creader)  # Moves to the first data row after header row
        for i in creader:
            if len(i[1])>6:
                print(i[0])

def showall():
    print("Contents of countries.csv file : ")
    with open("countries.csv",'r') as fr:
        creader=csv.reader(fr)
        for i in creader:
            print(i)

write()
showall()
search()
