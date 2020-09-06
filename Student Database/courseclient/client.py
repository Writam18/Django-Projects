import requests

URL = "http://127.0.0.1:8000"

# #Get auth token

# def get_token():
#     url = f"{URL}/api/auth/"
#     response = requests.post(url,data={'username': 'writam18','password': 'writcourse'})
#     return response.json()

# get_token()

def get_data():
    url = f"{URL}/api/users_list/"
    #header = {'Authorization': f'Token{get_token()}'}
    #response = requests.get(url,headers=header)
    response = requests.get(url)
    course_data = response.json()
    for c in course_data:
        print(c)

#get_data()

entry1 = {
    "name": "Education Courses",
    "subtitle": "Study for better future",
    "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    "timestamp": "1591850582",
    "created_by": "Admin A"
}

entry2 = {
    "name": "Architecture Courses",
    "subtitle": "Study for better future",
    "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    "timestamp": "1591850582",
    "created_by": "Admin A"
}

entry3 = {
    "name": "Medical Courses",
    "subtitle": "Study for better future",
    "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    "timestamp": "1591850582",
    "created_by": "Admin A"
}

entry4 = {
    "name": "Python Courses",
    "subtitle": "Study for better future",
    "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    "timestamp": "1591850582",
    "created_by": "Admin A"
}


def create_new(entry):
    url = f"{URL}/api/users_list/"
    data = entry
    response = requests.post(url,data = data)
    print(response.text)

def edit_data(course_id):
    url = f"{URL}/api/users_list/{course_id}"
    data = {
      
    }
    response = requests.put(url,data = data)
    print(response.text)

def delete_data(course_id):
    url = f"{URL}/api/users_list/{course_id}"
    response = requests.delete(url)
    print(response.status_code)

#edit_data(4)
delete_data(10)

#create_new(entry1)
#reate_new(entry2)
#create_new(entry3)
#create_new(entry4)
#create_new(entry5)