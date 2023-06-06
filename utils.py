from setup_leap_array import year_cycle

def get_index(counter:int, length_of_array:int):
    return (counter)%length_of_array

def evaluating_possible_consecutive_sum_in_array(
    given_array: list,
    check_consectutive_number: int
):
    outcome_totals = {}
    examples = {}
    # Three Counters
    #   i   =   Loop through every possible Starting Point
    #   j   =   Loop through consecutative numbers from Starting Point
    #   k   =   combination of the two

    # Looping through possible start_points
    for i in range(len(given_array)):
        sum_total = 0           # SUM(Number of Leaps) in Year Array 
                                #   OR SUM(Number of Days) in Month Array
        k = 0                   #K Loop
        
        # Looping through consecutive numbers
        for j in range(check_consectutive_number):
            k = get_index(i+j,len(given_array))
            sum_total += given_array[k]
        
        out_key = sum_total

        if out_key not in outcome_totals:
            outcome_totals[out_key] = 0
            examples[out_key] = i
        
        outcome_totals[out_key] += 1

    return outcome_totals, examples


for no_of_months in range(13):
    totals, examples = evaluating_possible_consecutive_sum_in_array(year_cycle.MONTH_CYCLE_DAYS, no_of_months)
    print("For {} months:".format(no_of_months))
    for key in totals:
        print("{} days ({}/{} - ex:Starting in {})".format(
            key,
            totals[key],
            year_cycle.MONTHS_IN_YEAR,
            year_cycle.MONTH_CYCLE_NAMES[examples[key]]
        ))
    print()
