# Algorithm for file updates in Python

import_file = "allow_list.txt"
with open(import_file, "r") as file:

  ip_addresses = file.read()
  ip_addresses = ip_addresses.split()

  for element in remove_list:
    if element in ip_addresses:
      ip_addresses.remove(element)

  ip_addresses = "\n".join(ip_addresses)
  with open(import_file, "w") as import_file:
    file.write(ip_addresses)
