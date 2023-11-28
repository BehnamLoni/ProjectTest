from datetime import datetime
import inflect
import sys

p = inflect.engine()

def main():
    try:
        BirthDate = input("Date of Birth: ")
        age = calculate_diff(BirthDate)
        print(f"Age: {calculate_age(age)[0]} years: {calculate_age(age)[1]} months: {calculate_age(age)[2]} days")
        print(f"Age_words: {convert(calculate_age(age)[0])}")

    except ValueError:
        sys.exit("Invalid date")

def calculate_diff(BirthDate):
    y,m,d =BirthDate.split("-")
    birth_date = datetime(int(y), int(m), int(d))
    now = datetime.now()
    age = now - birth_date
    return age.days

def calculate_age(age):
    years = age // 365
    months = (age % 365) // 30
    days = (age % 365) % 30
    return years,months,days

def convert(years):
    return f"{(p.number_to_words(years, andword='')).capitalize()} years"

if __name__ == "__main__":
    main()
