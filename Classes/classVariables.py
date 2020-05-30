class Shopping:

#Class Variable declared
    GST = 0.18

    def __init__(self,amount,total_items):
        self.amount = amount
        self.total_items = total_items


    def apply_GST(self):
        # the class variable can be accessed using class_name or the class instance
        total_amount = self.amount + self.amount*Shopping.GST
        return "The total amount including GST = {}".format(total_amount)

#class instance created and passed amount to the init method
customer_1 = Shopping(1000,5)

print(customer_1.apply_GST())

#accessing class Variable using class instance and class name
print(customer_1.GST)
print(Shopping.GST)

