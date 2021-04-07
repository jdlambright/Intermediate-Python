import json

# write in json or json.dump()
with open("data.json", "w") as data_file:
    # new_data says what we are writing, data file says where its going, indent 4 makes it format correctly
    json.dump(new_data, data_file, indent=4)
    website_entry.delete(0, END)
    password_entry.delete(0, END)



#read in json or json.load()
with open("data.json", "r") as data_file:
    quote = json.load(data_file)


#append in json or  json.update()
with open("data.json", "r") as data_file:
    # reading old data
    quote = json.load(data_file)
    #updating old data with new data
    quote.update(new_data)

with open("data.json", "w") as data_file:
    #saving updated data
    json.dump(quote, data_file, indent=4)