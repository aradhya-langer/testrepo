def rule_category(desc):

    d = desc.lower()

    # FOOD
    if any(x in d for x in [
        "zomato","cante","sweets","veg","food","cake",
        "swiggy","jiomar","ekart","rudres","anna","junk"
    ]):
        return "Food"

    # TRANSPORT
    if any(x in d for x in ["bus","bmtc","metro","uber","ola"]):
        return "Transport"

    # EDUCATION
    if any(x in d for x in ["iit","college","exam","fee","sit","sri"]):
        return "Education"

    # FRIENDS
    if any(x in d for x in [
        "himanshu","langer","raghav","shreyas","aryan","chetan"
    ]):
        return "Friends/Transfer"

    # SAVINGS
    if "aradhy" in d:
        return "Savings/Investment"

    # SHOPPING
    if any(x in d for x in ["amazon","flipkart","jiomar"]):
        return "Shopping"

    # BILLS
    if any(x in d for x in ["recharge","electric","bill"]):
        return "Bills"

    return "Other"
