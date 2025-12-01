# Crowdfunding Back End
Michaela Gyasi-Agyei

Link to depployed project: https://pakyi-library-fundraiser-5eb04ac099ec.herokuapp.com/fundraisers/

## Planning:
### Concept/Name
My website concept is a crowdfunding site called Sankofa Shelves which allows people to contribute to the purchase of books relating to Africa and the diaspora which will be included in libraries in Pakyi, other Ghanaian towns and cities, and other cities around the world. 

### Intended Audience/User Stories
My intended audience is anyone who is interested in literature, education and African culture. An example user may be an African based overseas who wants to contribute to a library in their family's hometown by pledging to a fundraiser. Another example user may be a teacher based in Ghana who creates a fundraiser raise more funds for books in their school's library. 

### Insomnia Screenshots

 A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.

 A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
 
 A screenshot of Insomnia, demonstrating a token being returned.


### Instructions
To register a new user and create a new fundraiser the following steps should be followed.
## Step 1: Register a New User
        
    **Endpoint:** `POST /users/`
        
        **Body (JSON):**
        ```json
        {
          "username": "john_doe",
          "email": "john@example.com",
          "password": "securepassword123"
        }
        ```
        
        **Response (201 Created):**
        ```json
        {
          "id": 1,
          "username": "john_doe",
          "email": "john@example.com"
        }
        ```
        
        ---
        
        ## Step 2: Get Authentication Token
        
        **Endpoint:** `POST /api-token-auth/`
        
        **Body (JSON):**
        ```json
        {
          "username": "john_doe",
          "password": "securepassword123"
        }
        ```
        
        **Response (200 OK):**
        ```json
        {
          "token": "0123456789abcdefghijklmnop"
        }
        ```
        
        Save this token — you'll use it to authenticate the next request.
        
        ---
        
        ## Step 3: Create a New Fundraiser
        
        **Endpoint:** `POST /fundraisers/`
        
        **Headers:**
        ```
        Authorization: Token 0123456789abcdefghijklmnop
        Content-Type: application/json
        ```
        
        **Body (JSON):**
        ```json
        {
          "title": "Fundraiser one",
          "description": "The first fundraiser.",
          "goal": 150,
          "image": "https://via.placeholder.com/300.jpg",
          "is_open": true
        }
        ```
        
        **Response (201 Created):**
        ```json
        {
          "id": 1,
          "title": "Fundraiser one",
          "description": "The first fundraiser.",
          "goal": 150,
          "image": "https://via.placeholder.com/300.jpg",
          "is_open": true,
          "date_created": "2025-11-21T20:22:01Z",
          "owner": 1
        }
        ```



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
