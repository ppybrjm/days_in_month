from setup_leap_array import year_cycle, gregorian_cycle_def
from utils import evaluating_possible_consecutive_sum_in_array

class YEAR_IS_LEAP:
    DEFINATE_NOT_LEAP_YEAR = -1
    UNKNOWN_IF_LEAP_YEAR = 0
    DEFINATE_LEAP_YEAR = 1

def months_to_days(number_of_months: int, get_details: bool = False):
    month_calculater = get_month_calc_object(number_of_months, get_details)
    print(month_calculater)

def get_month_calc_object(number_of_months: int, get_details: bool = False):
    if number_of_months >= gregorian_cycle_def.MONTHS_IN_CYCLE:
        return long_cycle_months_calc(number_of_months)

    elif number_of_months >=  year_cycle.MONTHS_IN_YEAR:
        return years_months_calc(number_of_months)

    else:
        return months_calc(number_of_months, YEAR_IS_LEAP.UNKNOWN_IF_LEAP_YEAR, get_details)


class months_calc():
    def __init__(self, number_of_months: int, year_is_leap: int, get_details: bool = False):
        self.setup_month_initial(number_of_months, year_is_leap, get_details)

    def setup_month_initial(self, number_of_months: int, year_is_leap: int, get_details: bool = False):
        self.get_details = get_details
        self.total_of_months = number_of_months
        self.evaluate_months = number_of_months % year_cycle.MONTHS_IN_YEAR
        self.year_is_leap = year_is_leap
        self.process_months()

    def process_months(self):
        evaluate_leap_year = True if (self.year_is_leap == YEAR_IS_LEAP.UNKNOWN_IF_LEAP_YEAR) else False
        months_cycle_days = year_cycle.MONTH_CYCLE_DAYS_LEAP if (self.year_is_leap == YEAR_IS_LEAP.DEFINATE_LEAP_YEAR) else year_cycle.MONTH_CYCLE_DAYS

        ordered_totals, examples = evaluating_possible_consecutive_sum_in_array(
            months_cycle_days,
            self.evaluate_months,
            evaluate_leap_year
        )
        self.generate_min_max_month_str(ordered_totals, evaluate_leap_year)

        if self.get_details:
            self.get_details_list(ordered_totals, examples)

    def generate_min_max_month_str(self, ordered_totals, evaluate_leap_year):
        first_item = next(iter(ordered_totals.items()))[0]
        last_last = next(reversed(ordered_totals.items()))[0]

        day_minumum = first_item.split("_")[0] if evaluate_leap_year else first_item
        day_maximum = last_last.split("_")[0] if evaluate_leap_year else last_last

        if day_minumum == day_maximum:
            self.min_max_str = "Answer is {} days".format(day_minumum)
        else:
            self.min_max_str = "Answer between {}-{} days".format(
                day_minumum, day_maximum
            )
    
    def get_details_list(self, ordered_totals, examples):
        if not self.get_details: return

        self.possible_outcomes_details = []
        for key in ordered_totals:
            self.append_detail(key, ordered_totals, examples, add_leap_day=False)
            
            #Do we need to add an attitional options for Leap Days
            info = key.split("_")
            if info[1] == "1":
                self.append_detail(key, ordered_totals, examples, add_leap_day=True)


    def append_detail(self, key, ordered_totals, examples, add_leap_day: bool):
        info = key.split("_")
        leap_star = "*" if add_leap_day else ""
        with_leap_str = " with Leap" if add_leap_day else ""
        number_of_days = int(info[0]) + 1 if add_leap_day else int(info[0])

        outcome_str = "{} days ({}{}/{} - ex:Starting in {}{})".format(
            number_of_days, #Number of Days
            ordered_totals[key], #Total Probablity
            leap_star, #* for leap years
            year_cycle.MONTHS_IN_YEAR,  #12
            year_cycle.MONTH_CYCLE_NAMES[examples[key]], #JAN
            with_leap_str # "with Leap" for leap years
        )
        self.possible_outcomes_details.append(outcome_str)


    def __str__(self):
        self.processing_str = self.generate_processing_str()        
        out_str = "{} - {}".format(self.processing_str, self.min_max_str)
        
        if self.get_details:
            for outcome in self.possible_outcomes_details:
                out_str += ("\n    {}").format(outcome)

        return out_str

    def generate_processing_str(self):
        plural_months = "" if self.total_of_months == 1 else "s"
        return("processing {} month{}".format(self.total_of_months, plural_months))


class years_months_calc(months_calc):
    def __init__(self, number_of_months):
        super().__init__(number_of_months, YEAR_IS_LEAP.UNKNOWN_IF_LEAP_YEAR)
        self.setup_year_initial()

    def setup_year_initial(self):
        self.year_total_number = self.total_of_months // year_cycle.MONTHS_IN_YEAR

    def process(self):
        pass

    def __str__(self):
        self.processing_str = self.generate_processing_str()
        return "{}".format(self.processing_str)
        
    def generate_processing_str(self):
        parent_str = super().generate_processing_str()

        purual_years = "" if self.year_total_number == 1 else "s"
        plural_months = "" if self.evaluate_months == 1 else "s"

        return("{} = {} year{} {} month{}".format(
            parent_str,
            self.year_total_number, purual_years, 
            self.evaluate_months, plural_months
            ))


class long_cycle_months_calc(years_months_calc):
    def __init__(self, number_of_months):
        super().__init__(number_of_months)
        self.setup_long_cycle_initial()
        self.process()

    def setup_long_cycle_initial(self):
        self.long_cycle_number = self.year_total_number // gregorian_cycle_def.YEARS_IN_CYCLE
        self.year_remainder_number = self.year_total_number % gregorian_cycle_def.YEARS_IN_CYCLE

    def process(self):
        gregorian_cycle = gregorian_cycle_def()
        self.long_cycle_years = self.long_cycle_number*gregorian_cycle_def.YEARS_IN_CYCLE
        self.long_cycle_days = self.long_cycle_number*gregorian_cycle.DAYS_IN_CYCLE
        self.long_cycle_included_leap_days = self.long_cycle_number*gregorian_cycle.LEAP_DAYS_IN_CYCLE

        self.long_cycle_str = "   In the first {} years, there were {} days, including {} leap years". format(
                self.long_cycle_years, self.long_cycle_days, self.long_cycle_included_leap_days
        )

    def __str__(self):
        self.processing_str = self.generate_processing_str()
        return "{}\n{}".format(self.processing_str, self.long_cycle_str)

    def generate_processing_str(self):
        parent_str = super().generate_processing_str()
        plural_cycles = "" if self.long_cycle_number == 1 else "s"
        year_remainder_str = "" if self.year_remainder_number == 0 else " + {}".format(self.year_remainder_number)

        return("{} --> ({} long cycle{} of 400{})".format(
            parent_str, self.long_cycle_number, plural_cycles, year_remainder_str
        ))

months_to_days(1, True)
months_to_days(2, True)
months_to_days(7, True)
months_to_days(11, True)
months_to_days(12)
months_to_days(123)
months_to_days(12300)