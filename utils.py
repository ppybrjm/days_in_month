from setup_leap_array import year_cycle, gregorian_cycle_def

def get_index(counter:int, length_of_array:int):
    return (counter)%length_of_array

def evaluating_possible_consecutive_sum_in_array(
    given_array: list,
    check_consectutive_number: int,
    check_leap_month: bool = False,     #Does contain Leap Month
):
    outcome_totals = {}
    examples = {}
    # Three Counters
    #   i   =   Loop through every possible Starting Point
    #   j   =   Loop through consecutative numbers from Starting Point
    #   k   =   combination of the two

    # Looping through possible start_points
    for i in range(len(given_array)):
        feb_flag = False        #Does list contain a FEB        
        sum_total = 0           # SUM(Number of Leaps) in Year Array 
                                #   OR SUM(Number of Days) in Month Array
        k = 0                   # k Loop counter
        
        # Looping through consecutive numbers
        for j in range(check_consectutive_number):
            k = get_index(i+j,len(given_array))
            sum_total += given_array[k]

            #Have we passed a FEB?
            if check_leap_month and k == year_cycle.LEAP_DAY_INDEX: feb_flag = True
        
        #Create output_key
        if check_leap_month:
            feb_int = 1 if feb_flag else 0
            out_key = "{}_{}".format(sum_total, feb_int)
        else:
            out_key = sum_total

        #Create output objects
        if out_key not in outcome_totals:
            outcome_totals[out_key] = 0
            examples[out_key] = i

        outcome_totals[out_key] += 1

    return outcome_totals, examples

# #No Leap Month Check Example
# for no_of_months in range(13):
#     totals, examples = evaluating_possible_consecutive_sum_in_array(year_cycle.MONTH_CYCLE_DAYS, no_of_months)
#     print("For {} months:".format(no_of_months))
#     for key in totals:
#         print("{} days ({}/{} - ex:Starting in {})".format(
#             key,
#             totals[key],
#             year_cycle.MONTHS_IN_YEAR,
#             year_cycle.MONTH_CYCLE_NAMES[examples[key]]
#         ))
#     print()

# #Leap Month Check Example
# for no_of_months in range(13):
#     totals, examples = evaluating_possible_consecutive_sum_in_array(year_cycle.MONTH_CYCLE_DAYS, no_of_months, True)
#     print("For {} months:".format(no_of_months))
#     for key in totals:
#         info = key.split("_")
#         leap_year_info_1 = "   " if info[1] == "0" else "+1?"
#         leap_year_info_2 = "" if info[1] == "0" else "[if Contained Feb is Leap Year] "

#         print("{}{} days ({}/{} - ex:Starting in {}){}".format(
#             info[0],
#             leap_year_info_1,
#             totals[key],
#             year_cycle.MONTHS_IN_YEAR,
#             year_cycle.MONTH_CYCLE_NAMES[examples[key]],
#             leap_year_info_2
#         ))
#     print()

#Year Example
gregorian_cycle = gregorian_cycle_def()
for no_of_years in range(gregorian_cycle.YEARS_IN_CYCLE + 1):
    totals, examples = evaluating_possible_consecutive_sum_in_array(gregorian_cycle.LONG_CYCLE, no_of_years)
    print("For {} years:".format(no_of_years))
    for key in totals:
        print("{} leap days ({}/{} - ex:Starting in {})".format(
            key,
            totals[key],
            gregorian_cycle.YEARS_IN_CYCLE,
            examples[key] + 2001
        ))
    print()
