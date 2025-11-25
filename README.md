# Crowdfunding Back End
Michaela Gyasi-Agyei

## Planning:
### Concept/Name
My website concept is a crowdfunding site called Sankofa Shelves which allows people to contribute to the purchase of books relating to Africa and the diaspora which will be included in libraries in Pakyi, other Ghanaian towns and cities, and other cities around the world. 

### Intended Audience/User Stories
My intended audience is anyone who is interested in literature, education and African culture. An example user may be an African based overseas who wants to contribute to a library in their family's hometown by pledging to a fundraiser. Another example user may be a teacher based in Ghana who creates a fundraiser raise more funds for books in their school's library. 

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
|  http://localhost:8000/pledges/ | GET | View all existing pledges | N/A | 200 OK | N/A |  
 http://localhost:8000/pledges/ | POST | Make a new pledge |{"amount": 50, "comment": "First book in library", 		"anonymous": false, "fundraiser": 1} | 201 CREATED | Bearer token |  
 | http://localhost:8000/fundraisers/ | GET | View all existing fundraisers | N/A | 200 OK | N/A |  
 | http://localhost:8000/fundraisers/ | POST | Make a new fundraiser | {"title": "Example Fundraiser", "description": "An example description", "goal": 100, "image": "https://via.placeholder.com/300.jpg", "is_open": true} | 201 CREATED | Bearer token |  
| http://localhost:8000/api-token-auth/ | POST | Return token | {"username": "[insert username]", "password": "[insert password]"} | 200 OK | N/A |  
|  | DELETE | Delete pledge |  |  |  |  
|  | DELETE | Delete fundraiser |  |  |  |  
|  | PUT | Update pledge |  |  |  |  
|  | PUT | Update fundraiser |  |  |  |  



### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
