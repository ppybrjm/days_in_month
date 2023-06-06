class year_cycle:
    MONTH_CYCLE_NAMES = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    MONTH_CYCLE_DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
    LEAP_DAY_INDEX = 1 #Leap Day in Feb

    MONTHS_IN_YEAR = len(MONTH_CYCLE_NAMES)
    SHORT_YEAR_DAYS = sum(MONTH_CYCLE_DAYS)
    LEAP_YEAR_DAYS = SHORT_YEAR_DAYS + 1

class gregorian_cycle_def:
    #In Gregorian Calandar, leap years happen in a 400 year cycle. setup by three paterns:
    # 1) Quadrennial - Every 4 Years        (AKA "SHORT PATERN") - Leap year every 4 years
    CYCLE_SHORT_PATERN = [0,0,0,1]

    # 2) Centurial - Every 100 years        (AKA "MID PATERN")   - Every 100 years, miss a leap year
    CYCLE_MID_PATERN = [1]*25
    CYCLE_MID_PATERN[24] = 0

    # 3) Quatercentenary - Every 400 years  (AKA "LONG PARTERN") - Every 400 years, add a bonus leap year.
    CYCLE_LONG_PATERN = [0,0,0,1]

    #All of these combine to make the "LONG CYCLE"
    YEARS_IN_CYCLE = len(CYCLE_SHORT_PATERN) * len(CYCLE_MID_PATERN) * len(CYCLE_LONG_PATERN)
    MONTHS_IN_CYCLE = YEARS_IN_CYCLE * year_cycle.MONTHS_IN_YEAR

    def __init__(self):
        self.LONG_CYCLE = self.define_gregorian_long_cycle()
        self.DAYS_IN_CYCLE = self.count_days_in_long_cycle()
        self.LEAP_DAYS_IN_CYCLE = self.count_leap_days_in_long_cycle()

    def define_gregorian_long_cycle(self):
        years_in_long_cycle = []

        for century in gregorian_cycle_def.CYCLE_LONG_PATERN:
            for quadrennial in gregorian_cycle_def.CYCLE_MID_PATERN:
                for viewed_year in gregorian_cycle_def.CYCLE_SHORT_PATERN:
                    if viewed_year == 1 and (quadrennial == 1 or century == 1):
                        years_in_long_cycle.append(1)
                    else:
                        years_in_long_cycle.append(0)

        return years_in_long_cycle

    def count_days_in_long_cycle(self):
        years = len(self.LONG_CYCLE)
        non_leap_days = years * year_cycle.SHORT_YEAR_DAYS
        leap_days = sum(self.LONG_CYCLE)
        return non_leap_days + leap_days
    
    def count_leap_days_in_long_cycle(self):
        return sum(self.LONG_CYCLE)