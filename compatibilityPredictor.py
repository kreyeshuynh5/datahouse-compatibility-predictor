# Created By  : Kaianu Reyes-Huynh
# Created Date: 4/12/2023
# version ='1.0'

import json #For reading and writing .json files

#Open .json file
with open('input.json', encoding='utf-8') as f:
    file_contents = json.load(f)

MAX_SCORE = 10

#Categorizing necessary members (both team and applicant attributes as well as the applicant names)
team_attributes = [member['attributes'] for member in file_contents['team']]
applicant_attributes = [member['attributes'] for member in file_contents['applicants']]
applicant_names = [member['name'] for member in file_contents['applicants']]


#Determine which attributes within the team has the lowest values and put them into min_attributes[]
min_value = MAX_SCORE
min_attributes = []
for attribute in team_attributes[0]:
    values = [member[attribute] for member in team_attributes]
    attribute_min = min(values)
    #Finding a minimum and putting it into the min_attributes[]
    if attribute_min < min_value:
        min_value = attribute_min
        min_attributes = [attribute]
    #If there is multiple with the same minimum, add them to min_attributes[]
    elif attribute_min == min_value:
        min_attributes.append(attribute)


#Determine the number of min_attributes and create equal weights for each attribute
num_min_weight_attributes = len(min_attributes)
if num_min_weight_attributes > 1:
    weight = 1 / num_min_weight_attributes
else:
    weight = 1


#Find the values of each min_attributes corresponding to the applicants attribute scores
#Use those scores and divide them by 10 to create a score with 1 being the best for that attribute
#If there is a weight we can multiply the total score by the weight to find the best score 
#given each min_attribute of the team
output_dict = []
for i, applicant in enumerate(applicant_attributes):
    scores = []
    for attribute in min_attributes:
        score = applicant[attribute] / MAX_SCORE
        scores.append(score)
    total_score = sum(scores) * weight
    output_dict.append({"name": applicant_names[i], "score": round(total_score,2)})


#Output data into format of scoredApplicants
output_dict = {"scoredApplicants": output_dict}

with open('output.json', 'w') as f:
    json.dump(output_dict, f, indent=4)