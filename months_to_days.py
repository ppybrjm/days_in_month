from setup_leap_array import year_cycle, gregorian_cycle_def


def months_to_days(number_of_months: int):
    month_calculater = get_month_calc_object(number_of_months)
    print(month_calculater)

def get_month_calc_object(number_of_months: int):
    if number_of_months >= gregorian_cycle_def.MONTHS_IN_CYCLE:
        return long_cycle_months_calc(number_of_months)
    elif number_of_months >=  year_cycle.MONTHS_IN_YEAR:
        return years_months_calc(number_of_months)
    else:
        return months_calc(number_of_months)


class months_calc():
    def __init__(self, number_of_months: int):
        self.number_of_months = number_of_months

    def __str__(self):
        self.processing_str = self.generate_processing_str()        
        return "{}".format(self.processing_str)

    def generate_processing_str(self):
        plural_months = "" if self.number_of_months == 1 else "s"
        return("processing {} month{}".format(self.number_of_months, plural_months))


class years_months_calc(months_calc):
    def __init__(self, number_of_months):
        super().__init__(number_of_months)
        self.year_total_number = self.number_of_months // year_cycle.MONTHS_IN_YEAR
        self.month_remainder_number = self.number_of_months % year_cycle.MONTHS_IN_YEAR

    def generate_processing_str(self):
        parent_str = super().generate_processing_str()

        purual_years = "" if self.year_total_number == 1 else "s"
        plural_months = "" if self.month_remainder_number == 1 else "s"

        return("{} = {} year{} {} month{}".format(
            parent_str,
            self.year_total_number, purual_years, 
            self.month_remainder_number, plural_months
            ))

class long_cycle_months_calc(years_months_calc):
    def __init__(self, number_of_months):
        super().__init__(number_of_months)
        self.long_cycle_number = self.year_total_number // gregorian_cycle_def.YEARS_IN_CYCLE
        self.year_remainder_number = self.year_total_number % gregorian_cycle_def.YEARS_IN_CYCLE

    def generate_processing_str(self):
        parent_str = super().generate_processing_str()
        plural_cycles = "" if self.long_cycle_number == 1 else "s"
        year_remainder_str = "" if self.year_remainder_number == 0 else " + {}".format(self.year_remainder_number)

        return("{} --> ({} long cycle{} of 400{})".format(
            parent_str, self.long_cycle_number, plural_cycles, year_remainder_str
        ))

months_to_days(1)
months_to_days(2)
months_to_days(123)
months_to_days(12300)    




