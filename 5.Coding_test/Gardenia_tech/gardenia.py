import datetime
import random

import numpy


# Todo add comments

class InvoiceStats:

    def __init__(self):
        self.client_full_name = str
        self.product_description = str
        self.total = 0
        self.invoices = []
        self.amount = None
        self.client_first_name = str
        self.client_last_name = str
        self.product_description = str
        self.invoice_number = int
        self.date = datetime.datetime.now()

    def add_invoice(self, client_first_name, client_last_name, product_description, amount):

        if amount < 0 or amount > 200000000:
            raise Exception("\nOops value much be greater and $0 or less than $200,000,000.00R")
        else:
            self.amount = amount

        self.invoice_number = (random.randint(10000, 100000))
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.client_full_name = client_first_name + ',' + client_last_name
        self.product_description = product_description
        self.amount = amount

        return self.invoice_number, self.client_first_name, self.client_last_name, self.client_full_name, self.product_description, self.amount

    """
    add a single invoice, in dollars and cents. 
    Maximum number of invoices is 20,000,000
    """

    def add_invoices(self, invoice):
        invoice_counter = len(self.invoices)
        if invoice not in self.invoices:
            self.invoices.append(invoice)
        if invoice_counter > 2000000:
            print(ValueError, "\nOops You have too many invoices")
            return ValueError

    """
    print invoice(s)
    """

    def print_invoice(self):
        counter = 0
        print('\nInvoice: ', counter)
        print('Invoice Number :', self.invoice_number)
        print("Client full name :", self.client_full_name)
        print("Product Name :", self.product_description)
        print("Total Amount :", '', '${:,.2f}'.format(self.amount))

    """
    remove and invoice 
    """

    def remove_invoice(self, invoice):
        if invoice in self.invoices:
            invoice_id = invoice.invoice_number
            print("Invoice", invoice_id, "has been removed")
            return self.invoices.remove(invoice)

    """ 
    remove all stored invoice data. 
    """

    def clear(self):
        self.invoices = []
        print('No more invoices', len(self.invoices))

    # --------------------Static Methods------------------------
    """
       print all invoice(s)
       """

    @staticmethod
    def print_all_invoice(invoices):
        counter = 0

        for invoice in invoices:
            counter += 1
            print('\nInvoice: ', counter)
            print('Invoice Number :', invoice.invoice_number)
            print("Client full name :", invoice.client_full_name)
            print("Product Name :", invoice.product_description)
            print("Total Amount :", '', '${:,.2f}'.format(invoice.amount))

    """
    find the median value (https://en.wikipedia.org/wiki/Median) of the added
    invoices, to the nearest cent. Half a cent should round down. 
    """

    @staticmethod
    def get_median(invoices):
        amounts_list = []
        for invoice in invoices:
            amounts_list.append(invoice.amount)
        calculated_median = numpy.median(amounts_list)
        return '${:,.2f}'.format(calculated_median)

    """ 
    find the mean value of the invoices, to the nearest cent. Half a cent should
    round down.
    """

    @staticmethod
    def get_mean(invoices):
        amounts_list = []
        for invoice in invoices:
            amounts_list.append(invoice.amount)
        calculated_mean = numpy.mean(amounts_list)
        return '${:,.2f}'.format(calculated_mean)


# -------------------------------------------------------------------------------------
invoice_1 = InvoiceStats()
invoice_1.add_invoice('Thomas', 'Acton', 'Banana', 99.7)
invoice_1.print_invoice()

invoice_2 = InvoiceStats()
invoice_2.add_invoice('Jacob', 'Acton', 'Banana', 80.3)
invoice_2.print_invoice()

invoice_3 = InvoiceStats()
invoice_3.add_invoice('Maire', 'Acton', 'Banana', 4)
invoice_3.print_invoice()

invoice_storage = InvoiceStats()

invoice_storage.add_invoices([invoice_1, invoice_2, invoice_3])
print()
print(invoice_storage.get_mean([invoice_1, invoice_2, invoice_3]))
print(invoice_storage.get_median([invoice_1, invoice_2, invoice_3]))

print()
invoice_storage.print_all_invoice([invoice_1, invoice_2, invoice_3])

print()
print(invoice_storage)
print()
invoice_storage.clear()
print()
print(invoice_storage)
