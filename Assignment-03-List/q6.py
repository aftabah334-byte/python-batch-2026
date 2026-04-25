months = {
    "01": "January", "02": "February", "03": "March",
    "04": "April", "05": "May", "06": "June",
    "07": "July", "08": "August", "09": "September",
    "10": "October", "11": "November", "12": "December"
}

date = input("Date daalo (mm/dd/yyyy): ")
parts = date.split("/")
mm = parts[0]
dd = parts[1]
yyyy = parts[2]

print(f"{months[mm]} {int(dd)}, {yyyy}")
