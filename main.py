import pandas as pd

my_details = pd.read_csv('input\employeedata.csv', encoding="unicode_escape")

initial_email = my_details['Emails'].tolist()
updated_email = []
for email in initial_email:
    updated_email.append(email.replace("@helpinghands.cm", "@handsinhands.org"))

names = my_details['Names'].tolist()
phone = my_details['Phone number'].tolist()

header = ['Name', 'Email', 'Phone']
my_dict = {"Name": names, "Email": updated_email, "Phone": phone}

frame = pd.DataFrame(my_dict)

frame.to_csv('output/update.csv')
frame.to_excel('output/update.xlsx')
