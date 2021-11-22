import itertools


def is_attend_graduation(attendance, condition_limit):
    """
     here will calculate student's consecutive missed class based on the probability of combinations.
     That calculation count and condition limit will based to allow or not will decided

     @param attendance: probability of attended class sequence
     @param condition_limit: condition days limit of allowing the graduation ceremony

     @return : boolean value based calculate student's consecutive missed class and days limit
    """
    consecutive_absent_count = 0
    for i in attendance:
        if i == "A":
            consecutive_absent_count += 1
            if consecutive_absent_count >= condition_limit:
                return False
        else:
            consecutive_absent_count = 0
    return True


def probability_combinations(days, abs_limit):
    """
         The probability that you will miss your graduation ceremony was calculation based on
             i. student should don't miss the class four or more consecutive days
             ii. The student must Present on the Nth day. because of Nth is Student Graduation ceremony
    """
    probability_options = ["A", "P"]

    attendance_combinations = [combination for combination in itertools.product(probability_options, repeat=days)]

    allowed_attendance_combinations = [attendance for attendance in attendance_combinations if
                                       is_attend_graduation(attendance, abs_limit)]

    missed_graduation = [attendance for attendance in allowed_attendance_combinations if attendance[-1] == "A"]

    return f'{len(missed_graduation)}/{len(allowed_attendance_combinations)}'


if __name__ == '__main__':
    """
    In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
    You are not allowed to miss classes for four or more consecutive days. 
    Your graduation ceremony is on the last day of the academic year, which is the Nth day.

    Your task is to determine the following:
    1. The number of ways to attend classes over N days.
    2. The probability that you will miss your graduation ceremony.
    """
    no_of_days = 5
    absent_days_limit = 4
    print(probability_combinations(no_of_days, absent_days_limit))
