import re

def extract_merchant(desc):
    desc = desc.lower()

    # remove upi codes
    desc = re.sub(r"upi/.*?/", "", desc)

    words = desc.split()

    # pick readable words
    clean = []
    for w in words:
        if len(w) > 2 and not w.isdigit():
            clean.append(w)

    return " ".join(clean[:3])
