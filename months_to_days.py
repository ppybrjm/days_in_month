from setup_leap_array import year_cycle, gregorian_cycle_def

def months_to_days(number_of_months: int):
    months_calculater = months_calc(number_of_months)

    print(months_calculater)

class months_calc():
    def __init__(self, number_of_months: int):
        self.number_of_months = number_of_months

    def __str__(self):
        plural_months = "" if self.number_of_months == 1 else "s"
        return("processing {} month{}".format(self.number_of_months, plural_months))



months_to_days(1)
months_to_days(2)
months_to_days(123)
months_to_days(12300)    




