from datetime import date


def is_valid_entry(entry):
    today = date.today()

    if int(entry["expiryYear"]) < today.year or int(entry["expiryMonth"]) < today.month:
        return {"msg": "CARD_EXPIRED"}

    checksum = 0
    for idx, digit in enumerate(entry["number"]):
        if idx + 1 % 2 == 0:
            double = int(digit) * 2
            if double > 10:
                checksum += (double % 10) + 1
            else:
                checksum += double
        else:
            checksum += int(digit)

    if checksum % 10 != 0:
        return {"msg": "INVALID_CARD_NUMBER"}


def make_card(entry):
    return {
        "number": entry["number"],
        "cvv": entry["cvv"],
        "expiryMonth": entry["expiryMonth"],
        "expiryYear": entry["expiryYear"],
        "limit": int(entry["limit"]),
        "assignedTo": entry["assignedTo"],
        "balance": int(entry["limit"]),
        "type": entry["type"]
    }


def make_card_entry(entry):
    err_code = is_valid_entry(entry)
    if err_code:
        return err_code, True

    return {
               "number": entry["number"],
               "cvv": entry["cvv"],
               "expiryMonth": entry["expiryMonth"],
               "expiryYear": entry["expiryYear"],
               "limit": int(entry["limit"]),
               "assignedTo": entry["assignedTo"],
               "balance": int(entry["limit"]),
               "type": entry["type"]
           }, False
