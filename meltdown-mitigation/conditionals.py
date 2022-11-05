"""Functions to prevent a nuclear meltdown."""


def get_emissions(temperature, neutrons_emitted):
    return temperature * neutrons_emitted


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    product_max = 500000
    temperature_max = 800
    emitted_neutrons_min = 500
    emissions = get_emissions(temperature, neutrons_emitted)

    return (
        (temperature < temperature_max)
        and (neutrons_emitted > emitted_neutrons_min)
        and (emissions < product_max)
    )


def get_generated_power_value(voltage, current):
    return voltage * current


def get_efficiency_percentage_value(generated_power, theoretical_max_power):
    return (generated_power / theoretical_max_power) * 100


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    power_ranges = {80: "green", 60: "orange", 30: "red", 0: "black"}

    generated_power = get_generated_power_value(voltage, current)
    efficiency = get_efficiency_percentage_value(generated_power, theoretical_max_power)

    if efficiency >= 80:
        return power_ranges[80]
    if 60 <= efficiency < 80:
        return power_ranges[60]
    if 30 <= efficiency < 60:
        return power_ranges[30]

    return power_ranges[0]


def get_threshold_percentage_value(threshold, percentage):
    return (percentage / 100) * threshold


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    threshold_low_value = get_threshold_percentage_value(threshold, 90)
    threshold_normal_max_value = get_threshold_percentage_value(threshold, 110)
    emissions = get_emissions(temperature, neutrons_produced_per_second)

    if threshold_low_value <= emissions <= threshold_normal_max_value:
        return "NORMAL"
    if emissions < threshold_low_value:
        return "LOW"

    return "DANGER"
