#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

#

# global constants
PROV_TAX = .05
FED_TAX = .025
TOTAL_TAX = .075
TOTAL_SALE = 1.075

# functions


def calc_prov_tax(purchase):
    prov_total = purchase * PROV_TAX
    return prov_total


def calc_fed_tax(purchase):
    fed_total = purchase * FED_TAX
    return fed_total


def calc_total_tax(purchase):
    total_tax = calc_prov_tax(purchase) * calc_fed_tax(purchase)
    return total_tax


def bill_of_sale(purchase):
    total_tax = calc_total_tax(purchase)
    total_cost = purchase * total_tax

    output = ("Amount of purchase: {0:.2f}".format(purchase)) + "\n"
    output += ("Provincial tax: {0:.2f}".format(purchase * .05)) + "\n"
    output += ("Federal tax: {0:.2f}".format(purchase * .025)) + "\n"
    output += ("Total tax: {0:.2f}".format(purchase * .075)) + "\n"
    output += ("Total sale: {0:.2f}".format(purchase * 1.075)) + "\n"

    return output


def file_writing(content):
    with open("output.txt", "w") as file_writer:
        file_writer.write(content)

file_writing(bill_of_sale(45.5))