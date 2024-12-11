def serialize_offer(offer):
    if offer:
        offer["_id"] = str(offer["_id"]) # Convert the mondoDB ObjectID into a string id
    return offer 