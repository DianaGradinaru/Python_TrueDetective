def is_twodigit_odd(number):
    return len(str(number)) == 2 and number % 2 != 0


def has_access(
    user,
    users_groups,
    file_owner,
    writable_by_owner,
    file_group,
    writable_by_group,
    writable_by_others,
    sudo_mode,
):
    pass


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_sunday(day, weekday_of_first):
    weekdays = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
    first = weekdays.index(weekday_of_first)
    weekdays = weekdays[first:] + weekdays[:first]
    weekdays = weekdays * 5
    return 1 <= day <= 31 and weekdays[day - 1] == "Su"


def should_bring_umbrella(
    rains,
    wind_scale,
    cloudy,
    red_sky,
    strong_flower_smell,
    spiders_down,
    lying_cattle,
    strong_sunshine,
):

    if wind_scale < 7:
        if rains:
            return True
        if cloudy and (red_sky or strong_flower_smell or spiders_down or lying_cattle):
            return True
        if strong_sunshine:
            return True
        return False
    return False


def should_take_a_nap(
    want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m
):
    pass