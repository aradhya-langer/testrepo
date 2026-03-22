import pdfplumber
import pandas as pd
import re

def extract_transactions(pdf_path):

    records = []
    current_desc = ""
    current_is_debit = False

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = text.split("\n")

            for line in lines:

                # detect description line
                if "UPI/DR" in line:
                    current_desc = line
                    current_is_debit = True

                elif "UPI/CR" in line:
                    current_is_debit = False

                # detect amount line
                nums = re.findall(r"\d+\.\d{2}", line)

                if len(nums) == 2 and current_is_debit:
                    withdrawal = float(nums[0])

                    records.append({
                        "Description": current_desc,
                        "Expense": withdrawal
                    })

    df = pd.DataFrame(records)
    return df
