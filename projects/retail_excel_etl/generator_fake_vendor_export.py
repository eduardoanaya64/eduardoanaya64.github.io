# generate_fake_vendor_export.py
import os
import random
from datetime import datetime, timedelta

import pandas as pd

def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    return start + timedelta(days=random.randint(0, max(delta.days, 1)))

def generate_fake_vendor_export(rows: int = 250, start_date="2025-06-01", end_date="2025-06-28") -> pd.DataFrame:
    """
    Creates a fake 'VendorNet Excel export' shaped like a raw dump:
    - Has 12 columns so "B, D, F, J" operations make sense
    - Some empty rows to demonstrate cleaning
    - Mixed data types (dates, currency strings, qty)
    """
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    unit_names = [
        "TUSTIN CA 1123", "PHILLY PA 0432", "LONG BEACH CA 0199", "SAN JOSE CA 0550",
        "IRVINE CA 0888", "SACRAMENTO CA 0310", "CHULA VISTA CA 0666"
    ]
    products = [
        "Simple Green All-Purpose Cleaner 32oz",
        "Simple Green Degreaser 1gal",
        "Simple Green Heavy-Duty Cleaner 128oz",
        "Simple Green Lemon Cleaner 32oz",
        "Simple Green Concentrate 1gal"
    ]
    categories = ["Cleaners", "Degreasers", "Household", "Industrial"]
    promo_flags = ["N", "Y"]

    data = []
    for i in range(rows):
        # sprinkle in some blank/empty rows
        if random.random() < 0.03:
            data.append([None] * 12)
            continue

        txn_date = random_date(start_dt, end_dt)
        qty = random.randint(0, 50)
        price = round(random.uniform(3.99, 19.99), 2)
        sales = round(qty * price, 2)

        # currency as string (like many exports)
        sales_str = f"${sales:,.2f}"

        row = [
            f"TXN-{random.randint(100000, 999999)}",                 # Col A (index 0)
            random.choice(unit_names),                                # Col B -> will become Unit Name
            random.choice(categories),                                # Col C
            random.choice(products),                                  # Col D -> will become Description
            random.choice(promo_flags),                               # Col E
            f"INTERNAL_NOTE_{random.randint(10, 99)}",                # Col F (to delete)
            txn_date.strftime("%m/%d/%Y"),                             # Col G (date-like)
            sales_str,                                                 # Col H (currency string)
            qty,                                                       # Col I (qty)
            f"DO_NOT_SHARE_{random.randint(1000, 9999)}",             # Col J (to delete)
            random.choice(["East", "West", "Central"]),                # Col K
            random.choice(["Online", "In-Store"]),                     # Col L
        ]
        data.append(row)

    # Intentionally generic column headers like a raw export
    columns = [
        "Transaction Ref", "B_Store", "Category", "D_Item",
        "Promo Flag", "F_Internal", "Report Date",
        "Sales: $", "Sales: Qty", "J_Sensitive",
        "Region", "Channel"
    ]
    return pd.DataFrame(data, columns=columns)

def main():
    print("Fake Meijer Vendor Export Generator")
    print("=" * 50)

    out_folder = input("Output folder for fake raw exports: ").strip().strip('"')
    os.makedirs(out_folder, exist_ok=True)

    num_files = input("How many fake exports to generate? (default 3): ").strip()
    num_files = int(num_files) if num_files else 3

    rows = input("Rows per file? (default 250): ").strip()
    rows = int(rows) if rows else 250

    # Create date ranges for filenames like MMDDYY-MMDDYY
    base_start = datetime(2025, 6, 1)
    for i in range(num_files):
        start = base_start + timedelta(days=i * 7)
        end = start + timedelta(days=6)

        df = generate_fake_vendor_export(rows=rows, start_date=start.strftime("%Y-%m-%d"), end_date=end.strftime("%Y-%m-%d"))

        fname = f"Meijer_{start.strftime('%m%d%y')}-{end.strftime('%m%d%y')}.xlsx"
        path = os.path.join(out_folder, fname)
        df.to_excel(path, index=False)

        print(f"✅ Created: {path} ({len(df)} rows)")

    print("\nDone. These files are safe for GitHub.")

if __name__ == "__main__":
    main()

