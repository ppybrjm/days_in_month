from months_to_days import get_month_calc_object

test_cases = [
    {"months": 0, "long_cycle": None},
    {"months": 1, "long_cycle": None},
    {"months": 11, "long_cycle": None},
    {"months": 12, "long_cycle": None},
    {"months": 204,"long_cycle": None},
    {"months": 1199, "long_cycle": None},
    {"months": 4799, "long_cycle": None},
    {"months": 4800, "long_cycle": "   In the first 400 years, there were 146097 days, including 97 leap years"},
    {"months": 4826, "long_cycle": "   In the first 400 years, there were 146097 days, including 97 leap years"},
    {"months": 6000, "long_cycle": "   In the first 400 years, there were 146097 days, including 97 leap years"},
    {"months": 21000, "long_cycle": "   In the first 1600 years, there were 584388 days, including 388 leap years"},
    {"months": 30001003, "long_cycle": "   In the first 2500000 years, there were 913106250 days, including 606250 leap years"}
]

for test in test_cases:
    calc_object = get_month_calc_object(test["months"])
    if test["long_cycle"] is None:
        assert(not hasattr(calc_object,"long_cycle_str"))
    else:
        assert(calc_object.long_cycle_str == test["long_cycle"])