# API Documentation
​A simple and easy to use API for performing basic CRUD ( Create, Read, Update and Delete) operations on a Name resource. By simply providing the id of the user and by specifying the corresponding HTTP requests, you can create, update, retrieve and delete a user record.
### API Endpoints
#### Using the API
​
The API provides the following endpoints for managing persons:
​
- POST `/api`: Create a new person.
- GET `/api/:id`: Get person by their ID.
- PUT `/api/:id`: Update a person by their ID.
- DELETE `/api/:id`: Delete a person by their ID.
​
#### Standard Request and Response Formats
​
- For the `POST` and `PUT` endpoints, send a JSON request body with the name field.
- For the `GET` endpoint, you would receive a JSON response with the person's name and ID if found.
- For the `DELETE` endpoint, no request body is required, and a successful deletion will return a 200 status code.
​
#### Create a New Person
​
- **URL:** `/api`
- **Method:** `POST`
- **Request Format:**
​
```
    {
        "name": "Mark Essien"
    }
```
​
- **Response Format:**
  ```
  {
      "name": "Mark Essien"
      "id": int,
  }
  ```
​
#### Get Person by ID
​
- **URL:** `/api/:id`
- **Method:** `GET`
  
- **Response Format:**
  ```
    {
        "name": "string",
        "id": int,
    }
  ```
​
#### Update Person
​
- **URL:** /api/:id
- **Method:** PUT
- **Request Format:**
​
```
{
    "name": "Updated_Name"
}
```
​
**Response Format:**
​
```
{
      "name": "Updated_Name"
      "id": int,
}
```
​
#### Delete Person
​
- **URL:** `/api/:id`
- **Method:** `DELETE`

- **Response Format:**
​
```
{
    "detail": "User with ID {id} Successfully deleted"
}
```
​
## Test Request and Response
​
#### Create a New Person
​
**Request:**
​
```sh
    POST /api
    Content-Type: application/json
​
    {
        "name": "Mark Essien"
    }
```

**Response:**
​
```sh
    HTTP/1.1 200 Created
    Content-Type: application/json
​
    {
          "name": "Mark Essien",
          "id": "<id>"
    }
```
​
#### Get Person by ID
​
**Request:**
​
```sh
    POST /api/<id>
```
​
**Response:**
​
```sh
    HTTP/1.1 200 OK
    Content-Type: application/json
​
    {
          "name": "Mark Essien",
          "id": "<id>",
    }
```
​
#### Update Person
​
**Request:**
​
```sh
    PUT /api/<id>
    Content-Type: application/json
​
    {
        "name": "Updated_Name"
    }
```
​
**Response:**
​
```sh
    HTTP/1.1 200 OK
    Content-Type: application/json
​
    {
          "name": "Updated_Name",
          "id": "<person-id>",
    }
```
​
#### Delete Person
​
**Request:**
​
```sh
    DELETE /api/<id>
```
​
**Response:**
​
```sh
    HTTP/1.1 200
    {
        detail: "User with ID {id} Successfully deleted"
    }
```
​
## Local Setup and Deployment
​
- Clone the repository and follow the installation steps mentioned in the `README.md`` file.
- Start the API by uvicorn restapi.main:app --reload.
- The API will be available at http://127.0.0.1:8000/. 
