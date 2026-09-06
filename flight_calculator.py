# Calculate active flight time in minutes based on payload weight in grams.
def calculate_active_flight_time(payload_weight_grams):
    if payload_weight_grams < 0:
        raise ValueError("Weight cannot be negative.") # Copilot suggested a long error message; edited it to clearly explain the problemn more shortly and concisely.
    # Calculate the flight time using the payload weight.
    flight_time = 180 - .1 * payload_weight_grams
    return max(0, flight_time) # Rejected Copilot suggestion because it introduced unnecessary code.
