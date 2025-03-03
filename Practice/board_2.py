import csv
def write():
    with open("product.csv","w",newline='') as fw :
        cwriter=csv.writer(fw)
        cwriter.writerow(['PID','PNAME','COST','QUANTITY'])
        cwriter.writerow(['P1','Brush',50,200])
        cwriter.writerow(['P2','Toothpaste',120,150])
        cwriter.writerow(['P3','Comb',40,300])
        cwriter.writerow(['P4','Sheets',100,500])
        cwriter.writerow(['P5','Pen',10,250])
        print("Data written to csv file ...")

def search():
    print("Product with maximum cost : ")
    with open("product.csv",'r') as fr:
        creader=csv.reader(fr)
        next(creader)  
        Max = -1
        
        for i in creader:
            if int(i[2])>Max:
                Max=int(i[2])
                rec=i
        print(rec)

def showall():
    print("Contents of product.csv file : ")
    with open("product.csv",'r') as fr:
        creader=csv.reader(fr)
        for i in creader:
            print(i)

write()
showall()
search()
