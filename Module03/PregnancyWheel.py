import datetime

def print_header():
    print('--------------------')
    print('    Due Date APP')
    print('--------------------')
    print()


def get_lmp_from_patient():
    print("When was the patient's last normal menstrual cycle? ")

    date_str = input('Format: [dd/mm/yyyy]? ')
    # Desired format '05/26/2018'

    parts = date_str.split('/')
    # argument check
    if len(parts) !=3:
        print('Bad date found', date_str)
        return get_lmp_from_patient()

    year = int(parts[2])
    month = int(parts[1])
    day = int(parts[0])

    lmp = datetime.date(year, month, day)
    #print (lmp)
    return lmp

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(original_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    weeks = dt/7
    #this line converts days to weeks
    gest_age = weeks

    return gest_age.days
    #gest_age rounds the weeks up i.e. 10 weeks 3 days to 11 weeks (unsure how to make as a decimal/fraction)
def print_gestational_age(gest_age):
    print("Your current gestational age is {} weeks.".format(-gest_age))


def print_date_date_information(min_due_date, max_due_date, expected_due_date):

    print('Your expected due date is', expected_due_date.strftime('%a %b %d %Y'))
    print('But it may be as early as', min_due_date.strftime('%m/%d/%Y'))
    print('Or as late as', max_due_date.strftime('%m/%d/%Y'))


def main():
    print_header()
    lmp_day = get_lmp_from_patient()
    today = datetime.date.today()
    gest_length = datetime.timedelta(days = 281)
    gest_std = datetime.timedelta(days = 13)

    expected_due_date = lmp_day + gest_length
    min_due_date = expected_due_date - gest_std
    max_due_date = expected_due_date + gest_std

    print_date_date_information(min_due_date, max_due_date, expected_due_date)

    age = compute_days_between_dates(lmp_day, today)
    print_gestational_age(age)



main()