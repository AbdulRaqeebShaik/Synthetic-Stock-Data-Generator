import random

def gen_ticker():
    t_seq="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tt=''.join(random.choices(t_seq, k=4))
    return tt
10
def gen_time():
    random_hour=random.randint(9, 17) 
    random_minute=random.randint(00,59)
    random_second=random.randint(00,59)
    random_millisec=random.randint(00,99)
    return str("%02d" %random_hour) + ":" + str("%02d" %random_minute) + ":" + str("%02d" %random_second) + ":" + str("%02d" %random_millisec)

def gen_value():
    random_float = random.random() * random.randint(10, 1000)
    return random_float


if __name__=='__main__':
    num_rows=int(input("Enter number of required rows: "))
    req_date=input("Enter Date(DD/MM/YYYY): ")


    #fname="mock_data_"+req_date+".csv"
    #print(fname)
    file = open('mock_data.csv', 'w')

    file.write("Ticker, Time stamp, Value\n")

    for i in range(0,num_rows):
        vvv=gen_ticker()+", "+req_date+" "+gen_time()+", "+str(gen_value())

        res=file.write(str(vvv))
        file.write("\n")
    file.close()

    print("mock_data.csv created Successfully!!!")