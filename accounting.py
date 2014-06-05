#import csv

#with open('customer_orders.csv', 'rb') as f:
#    reader = csv.reader(f)
#    '''
 #   for line in reader:
 #       line = line.strip("\n")
 #       value = line.split(',')
#        print value'''

def open_file():
    invoice = open("customer_orders.csv", "rb")
    #customer_list = invoice.split(",")
    #print customer_list
    '''
    array = []
    array = invoice.readline()
    new_array_line = array.split(',')

    print new_array_line '''

    for line in invoice:
        line = line.strip()
        data = line.split(',')
        
        cus_name = data[1]
        order_amount = data[2]
        paid_amount = float(data[3])

        #print "%s ordered %s melons for $%s." % (cus_name, order_amount, paid_amount)

        melon_cost = 1.00

        expected_balance = float(order_amount) * melon_cost #total $ each customer should pay

        if paid_amount == expected_balance:
            #print "\tPaid in full. :-)"
            pass
        else:
            missing_balance = expected_balance - paid_amount
            print "%s ordered %s melons for $%s." % (cus_name, order_amount, paid_amount)
            print "\t %s has underpaid. :-( !!!!!!!!!!ALERT!!!!!!!!!!!" % cus_name

            #cus_name, "paid %.2f, expected %.2f"%(customer1_paid, customer1_expected)


    #id_num = list_data[0]

'''
    math_input = raw_input("> ")
    array = []
    array = math_input.split(" ")
    #print array

    character = str(array[0])
    num1 = int(array[1])
    if len(array) == 3:
        num2 = int(array[2])
'''        

if __name__ == "__main__":
    open_file()

