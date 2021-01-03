from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    d1 = date.today()
    d2 = date(2020,12,26)
    result1 = diff_dates(d2, d1)
    print ('{} days between {} and {}'.format(result1, d1, d2))

main()
