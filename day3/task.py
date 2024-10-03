import requests
postalCode = int(input("Enter a postal code: "))
response = requests.get(f"https://api.postalpincode.in/pincode/{postalCode}")
details = response.json()
postOfficeName = details[0]['PostOffice'][0]['Name']
postOfficeDetails = details[0]['PostOffice'][0]
print(f"Name of Post office is: {postOfficeName}" )

choice = int(input("Do you want more details? (1/0)"))
if choice:
    print(postOfficeDetails)
print("That's all!!")