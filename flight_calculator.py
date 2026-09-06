# Calculate active flight time in minutes based on payload weight in grams.
def calculate_flight_time(payload_weight_grams):

    """Calculate active flight time based on payload weight.

    Parameters:
        payload_weight_grams: Payload weight in grams.

    Returns:
        Active flight time in minutes.
    """

    if payload_weight_grams < 0:
        raise ValueError("Payload weight cannot be negative.") # Copilot suggested a long error message; edited it to clearly explain the problemn more shortly and concisely.

    # Calculate the flight time using the payload weight.
    flight_time = 180 - .1 * payload_weight_grams
    return max(0, flight_time) # Rejected Copilot suggestion because it introduced unnecessary code.

def flight_time_table(max_weight_grams, step_grams): # Rejected copilot suggestion because it igored parameters and used unnecessary code.
    """Create a table of payload weights and corresponding flight times.

    Parameters:
        max_weight_grams: Maximum payload weight in grams.
        step_grams: Increment between payload weights.

    Returns:
        A list of (weight, flight_time) pairs.
    """

    table = []

    for weight in range(0, max_weight_grams + 1, step_grams):
        table.append((weight, calculate_flight_time(weight)))

    return table