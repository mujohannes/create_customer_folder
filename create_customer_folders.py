# prologue
# script to create folders based on customer names
# version 1.0.0
# created on 15 June 2020
# created by Johannes

# import modules
import os
# specify name of file
file = 'customers.txt'
# check if text file does not exist
if not os.path.exists(file):
  # if it doesn't exist stop with error message
  print('Error: file ' + file +' does not exist!')
# if file exists create List from names
else:
  print('File found: ' + file )


# loop though the List
#   create path using name
#   if folder already exists
#     output message "name already exists"
#   else (folder does not exist)
#   create folder