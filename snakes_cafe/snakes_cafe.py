##
order_in = ""
def in_n_out():
    order_in = input("> ")
    if order_in == "quit" :
        pass


def format_text():
    print(
        "**************************************\r\n",
        "**    Please see our menu below.    **\r\n",
        "**    Welcome to the Snakes Cafe!   **\r\n **\r\n",
        '** To quit at any time, type "quit" **\r\n',
        "**************************************\r\n"
    )
    print(" Appetizers\r\n",
    "----------\r\n",
    "Wings\r\n",
    "Cookies\r\n",
    "Spring Rolls\r\n\r\n",

    " Entrees\r\n",
    "-------\r\n",
    "Salmon\r\n",
    "Steak\r\n",
    "Meat Tornado\r\n",
    "A Literal Garden\r\n\r\n",

    " Desserts\r\n",
    "--------\r\n",
    "Ice Cream\r\n",
    "Cake\r\n",
    "Pie\r\n\r\n",

    " Drinks\r\n",
    "------\r\n",
    "Coffee\r\n",
    "Tea\r\n",
    "Unicorn Tears\r\n\r\n",

    "***********************************\r\n",
    "** What would you like to order? **\r\n",
    "***********************************\r\n",)
    in_n_out()
    
menu = [
    {
        "name": "Appetizers",
        "types": [
            "Wings",
            "Cookies",
            "Spring Rolls",
        ],
    },
    {
        "name": "Entrees",
        "types": [
            "Salmon",
            "Steak",
            "Meat Tornado",
            "A Literal Garden",
        ],
    },
        {
        "name": "Desserts",
        "types": [
            "Ice Cream",
            "Cake",
            "Pie",
        ],
    },
            {
        "name": "Drinks",
        "types": [
            "Coffee",
            "Tea",
            "Unicorn Tears",
        ],
    },
]

if __name__=="__main__":
    format_text()
