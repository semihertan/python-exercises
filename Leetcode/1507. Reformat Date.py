given_date = "6th Jun 1933".split(" ")

month_dict = {"Jan": "01", "Feb": "02",
              "Mar": "03", "Apr": "04",
              "May": "05", "Jun": "06",
              "Jul": "07", "Aug": "08",
              "Sep": "09", "Oct": "10",
              "Nov": "11", "Dec": "12"}

day = given_date[0][:-2]
month = month_dict[given_date[1]]
year = given_date[2]

if int(day) < 10:
    day = "0" + day

reformatted_date = year + "-" + month + "-" + day
print(reformatted_date)