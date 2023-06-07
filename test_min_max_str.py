from months_to_days import get_month_calc_object

test_cases = [
    {"months": 0, "min_max_str": "Answer is 0 days"},
    {"months": 1, "min_max_str": "Answer between 28-31 days"},
    {"months": 2, "min_max_str": "Answer between 59-62 days"},
    {"months": 3, "min_max_str": "Answer between 89-92 days"},
    {"months": 4, "min_max_str": "Answer between 120-123 days"},
    {"months": 5, "min_max_str": "Answer between 150-153 days"},
    {"months": 7, "min_max_str": "Answer between 212-215 days"},
    {"months": 11, "min_max_str": "Answer between 334-337 days"},
    # {"months": 12, "min_max_str": ""},
    # {"months": 13, "min_max_str": ""},
    # {"months": 20, "min_max_str": ""},
    # {"months": 24, "min_max_str": ""},
    # {"months": 25, "min_max_str": ""},
    # {"months": 30, "min_max_str": ""},
    # {"months": 200, "min_max_str": ""},
    # {"months": 204, "min_max_str": ""},
    # {"months": 1199, "min_max_str": ""},
    # {"months": 1200, "min_max_str": ""},
    # {"months": 1201, "min_max_str": ""},
    # {"months": 1202, "min_max_str": ""},
    # {"months": 1212, "min_max_str": ""},
    # {"months": 1213, "min_max_str": ""},
    # {"months": 1214, "min_max_str": ""},
    # {"months": 2000, "min_max_str": ""},
    # {"months": 2004, "min_max_str": ""},
    # {"months": 3000, "min_max_str": ""},
    # {"months": 3001, "min_max_str": ""},
    # {"months": 3002, "min_max_str": ""},
    # {"months": 4799, "min_max_str": ""},
    # {"months": 4800, "min_max_str": ""},
    # {"months": 4801, "min_max_str": ""},
    # {"months": 4802, "min_max_str": ""},
    # {"months": 4812, "min_max_str": ""},
    # {"months": 4813, "min_max_str": ""},
    # {"months": 4826, "min_max_str": ""},
    # {"months": 6000, "min_max_str": ""},
    # {"months": 19200, "min_max_str": ""},
    # {"months": 20000, "min_max_str": ""},
    # {"months": 21000, "min_max_str": ""},
    # {"months": 21001, "min_max_str": ""},
    # {"months": 30000000, "min_max_str": ""},
    # {"months": 30001003, "min_max_str": ""},
    # {"months": 30001008, "min_max_str": ""}
]

for test in test_cases:
    calc_object = get_month_calc_object(test["months"])
    assert(calc_object.min_max_str == test["min_max_str"])

    for detail in [True, False]:
        calc_object = get_month_calc_object(test["months"], detail)
        assert(calc_object.min_max_str == test["min_max_str"])