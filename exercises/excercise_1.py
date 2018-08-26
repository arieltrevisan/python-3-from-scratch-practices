def calc_tax(state: str, income: float, federal_tax: float = 10.0):
    """
    Calculate net income after federal and state tax
    :param state: US state code
    :param income: Gross income
    :param federal_tax: Percentage of federal taxes
    """
    states_taxes = {
        "AL": ("Alabama", 5),
        "AK": ("Alaska", 3),
        "FL": ("Florida", 4),
        "IL": ("Illinois", 8),
    }

    state = state.upper()

    if state not in states_taxes:
        raise AssertionError("Taxes calculation of '{}' is not available. List: {}"
                             .format(state, states_taxes.keys()))

    net = income - (income * federal_tax / 100)
    print("Net after Federal Taxes:", net)

    tax_to_deduct = net * states_taxes[state][1] / 100.0
    net = net - tax_to_deduct
    print("Net after {} Taxes: {}".format(states_taxes[state][0], net))


calc_tax("al", 100)
calc_tax("il", 100)
# calc_tax("tr", 100)  # this one errors
