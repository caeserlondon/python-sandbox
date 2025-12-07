import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USER_NAME = "caeseribrahim"
TOKEN = "jjzdfghbftunmzh"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


#Post a pixel value to the graph
today = str(datetime.today().strftime("%Y-%m-%d").replace("-", ""))
# print(today)

pixel_data = {
    "date": today,
    "quantity": input("How many kilometers did you run today?"),
}


pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
print(response.text)


# UPDATE a graph

pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"
pixel_update = {
    "quantity": "18.74",
}
# response = requests.put(url=pixel_update_endpoint, headers=headers, json=pixel_update)
# print(response.text)


# UPDATE a graph


# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)