class year_cycle:
    MONTH_CYCLE = [31,28,31,30,31,30,31,31,30,31,30,31]
    MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    LEAP_DAY_INDEX = 1 #Leap Day in Feb
    MONTHS_IN_YEAR = 12

class gregorian_patern_def:
    SHORT_PATERN = [0,0,0,1]  # Leap year every 4 years
    MID_PATERN = [1]*25       # Every 100 years, miss a leap year
    MID_PATERN[24] = 0
    LONG_PATERN = [0,0,0,1]   # Every 400 years, add a bonus leap year.

class defining_constants:
    @staticmethod
    def define_short_year(MONTH_CYCLE):
        days = 0
        for month in MONTH_CYCLE:
            days += month if month != "A" else 28
        return days

    SHORT_YEAR = define_short_year(year_cycle.MONTH_CYCLE)
    LEAP_YEAR = SHORT_YEAR+1