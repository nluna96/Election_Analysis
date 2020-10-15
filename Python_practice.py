# counties = ["Arapahoe","Denver","Jefferson"]

# for county in counties:
#     print(county)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for dic in voting_data:
    print(dic['county'], dic['registered_voters'])



