from datetime import date, timedelta

past = date(1970,1,1)
today = date.today()
since = (today - past).total_seconds()

first_message = past.strftime("Seconds since %B %e, %Y: ")
first_message += "{:,.4f}".format(since) + " or "
first_message += "{:.2e}".format(since) + " in scientific notation"

second_message = today.strftime("%b %d %Y")

print(first_message)
print(second_message)
