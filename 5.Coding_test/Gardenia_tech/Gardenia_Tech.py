import datetime
import random
from collections import defaultdict

import numpy


# Todo add comments

class InvoiceStats:
    def __init__(self, client_first_name, client_last_name, product_description, amount):
        self.invoice_number = (random.randint(10000, 100000))
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.client_full_name = client_first_name + ',' + client_last_name
        self.date = datetime.datetime.now()
        self.product_description = product_description
        self.products = defaultdict(lambda: None)
        if amount < 0 or amount > 200000000:
            raise Exception("\nOops value much be greater and $0 or less than $200,000,000.00R")
        else:
            self.amount = amount


def add_invoice(self):
    return self.invoice_number, self.client_full_name, self.product_description, self.amount


class InvoicesStats(InvoiceStats):
    def __init__(self, invoices=None):
        if invoices is None:
            self.invoices = []
        else:
            self.invoices = invoices

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
    add a single invoice, in dollars and cents. 
    Maximum number of invoices is 20,000,000
    """

    def add_invoices(self, invoice):
        if invoice not in self.invoices:
            self.invoices.append(invoice)
        if len(self.invoices > 2000000):
            print(ValueError, "\nOops You have too many invoices")
            return ValueError

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

    # ---------------------------- Static Methods ----------------------------
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


invoice_1 = InvoiceStats('name_1', 'sn_1', 'banana', 99)
invoice_2 = InvoiceStats('name_2', 'sn_2', 'apple', 86)
invoice_3 = InvoiceStats('name_3', 'sn_3', 'orange', 87)
invoices = InvoicesStats([invoice_1, invoice_2, invoice_3])
print(invoices.get_median())
print(invoices.get_mean())

# invoices.clear()
# invoices.print_invoice()
amount_list = [99, 86, 87, 88, 111, 86, 103]
print(numpy.median(amount_list))
print(numpy.mean(amount_list))
