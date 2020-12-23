import re
from pprint import pprint
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def correct_names(contacts_list):
    formated_name_list = []
    pattern = re.compile(r'^([аА-яЯ]+)[\s|,]([аА-яЯ]+)[\s|,]([аА-яЯ]+|)')
    replace_names = r'\1, \2, \3'
    for people in contacts_list:
        people = ",".join(people)
        result = [pattern.sub(replace_names, people)]
        formated_name_list.append(result)
    return formated_name_list



def normal_phone(contacts_list):
    formated_phone_list = []
    pattern = re.compile("(8|\+7)(\s?)(\(?)(\d{3})(\)?)(\s?)(\-?)(\d{3})(\-?)(\d{2})(\-?)(\d{2})(\s*\(*(доб\.\s*\d+)*\)*)")
    replace_phone_numbers = r'+7(\4)\8-\10-\12 \14'
    for people in contacts_list:
      people = ",".join(people)
      result = pattern.sub(replace_phone_numbers, people)
      formated_phone_list.append(result)
    return formated_phone_list


def delete_duplicates(contacts_list):
  new_list_contact = []
  for contact in contacts_list:
    contact = ''.join(contact)
    contact = contact.split(',')
    new_list_contact.append(contact)


  for contact in new_list_contact:
    for contacts in contact:
        if contacts== '':
            del (contacts)
    while contact[3] == '':
      del (contact[3])

  name_list = []
  list_contact = []
  for contact in new_list_contact:
    if contact[0] not in name_list:
      name_list.append(contact[0])
      list_contact.append(contact)
  return list_contact

formated_phone_book = normal_phone(correct_names(contacts_list))
new_contacts_list = delete_duplicates(formated_phone_book)


with open("phonebook.csv", "w", encoding='utf8', newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)