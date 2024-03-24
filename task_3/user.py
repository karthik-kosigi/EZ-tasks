import sqlite3

def display_bill():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('shopping.db')
        cursor = conn.cursor()

        # Select all rows from the 'cart' table
        cursor.execute("SELECT * FROM cart")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the bill header
        print("Bill")
        print("================================================================")
        print(f"{'Product ID':<12}{'Product Name':<20}{'Quantity':<10}{'Total Price':<15}")

        # Initialize total variables
        total = 0.0

        # Print each item in the bill
        for row in rows:
            product_id, product_name, quantity, total_price = row
            total += total_price
            print(f"{product_id:<12}{product_name:<20}{quantity:<10}${total_price:.2f}")

        # Calculate CGST (assuming 5% CGST)
        cgst_percentage = 5
        cgst = (total * cgst_percentage) / 100

        # Print the totals
        print("================================================================")
        print(f"{'Total:':<42}${total:.2f}")
        print(f"{'CGST (' + str(cgst_percentage) + '%):':<42}${cgst:.2f}")

        # Calculate grand total
        grand_total = total + cgst
        print(f"{'Grand Total:':<42}${grand_total:.2f}")

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print("Error:", e)

# Example usage:
display_bill()
