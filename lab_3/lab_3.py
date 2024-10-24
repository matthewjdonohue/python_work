# Lists
contact_names=[]
contact_phones=[]
contact_emails=[]

# Contacts

#contact_names= ["Alpha", "Bravo", "Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet"]
#contact_phones= ["1","2","3","4","5","6","7","8","9","10"]
#contact_emails= ["a@a","b@b","c@c","d@d","e@e","f@f","g@g","h@h","i@i","j@j"]

# 2 User Input

# 2.1 Contact loop

for i in range(10):
    name = input(f"please enter name for contact {i+1}: ")
    contact_names.append(name)

    phone=input(f"Please enter phone number for contact {i+1}: ")
    contact_phones.append(phone)

    email=input(f"Please enter email address for contact {i+1}: ")
    contact_emails.append(email)

print("==============")

# 3. Displaying a Single Contact
contact_input = int(input("Enter the contact number (1-10) that you would like to see: "))
contact_input = contact_input - 1

print(contact_names[contact_input])
print(contact_phones[contact_input])
print(contact_emails[contact_input])

# 4. Sorting the Contacts
print("==============")

print("Sorting contacts...")

sorted_combined = sorted(zip(contact_names, contact_phones, contact_emails))

contact_names.clear()
contact_phones.clear()
contact_emails.clear()

for name, phone, email, in sorted_combined:
    contact_names.append(name)
    contact_phones.append(phone)
    contact_emails.append(email)

print("=============")

# 5. Top 3 Contacts
print(f"Your first three contacts are: ")

for name in contact_names[:3]:
    print("     name: ",name)