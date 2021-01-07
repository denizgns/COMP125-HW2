"""
Student Name:Deniz Güneş
File: stock_purchase.py
-----------------------
"""
def get_num_shares():
    return input("Enter number of shares: ")
def get_purchase_price():
    return input("Enter purchase price: ")
def get_sale_price():
    return input("Enter sale price:")

def purchase(n_shares, purch_price, sale_price):
    purchase_bill = float(n_shares) * float(purch_price)
    stockbroker_purch = (purchase_bill / 100) * 3
    sell_bill = float(n_shares) * float(sale_price)
    stockbroker_sale = (sell_bill / 100) * 3

    loss = purchase_bill + stockbroker_purch + stockbroker_sale
    gain = sell_bill

    if loss > gain:
        print("After the transaction, you lost ", format(loss - gain, '.2f'), "dollars")
    elif gain > loss:
        print("After the transaction, you gained ", format(gain - loss, '.2f'), "dollars")
    elif gain == loss:
        print("After the transaction, you stayed the same")

def main():
    """
    Replace this comment with a more descriptive one.
    Don't forget to delete the pass statement below.
    """
    n_shares = get_num_shares()
    purch_price = get_purchase_price()
    sale_price = get_sale_price()
    purchase(n_shares, purch_price,sale_price)



if __name__ == "__main__":
    main()
