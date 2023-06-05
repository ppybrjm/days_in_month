class year_cycle:
    MONTH_CYCLE_NAMES = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    MONTH_CYCLE_DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
    LEAP_DAY_INDEX = 1 #Leap Day in Feb

    MONTHS_IN_YEAR = len(MONTH_CYCLE_NAMES)
    SHORT_YEAR_DAYS = sum(MONTH_CYCLE_DAYS)
    LEAP_YEAR_DAYS = SHORT_YEAR_DAYS + 1

class gregorian_patern_def:
    SHORT_PATERN = [0,0,0,1]  # Leap year every 4 years
    MID_PATERN = [1]*25       # Every 100 years, miss a leap year
    MID_PATERN[24] = 0
    LONG_PATERN = [0,0,0,1]   # Every 400 years, add a bonus leap year.
    YEARS_IN_CYCLE = len(SHORT_PATERN) * len(MID_PATERN) * len(LONG_PATERN)