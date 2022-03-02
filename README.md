<center> <h1>Leads</h1> </center>

## ENDPOINTS:

><h2 style="color:green">POST <span style="color:gray">/leads</span></h2>
 
**POST** request MUST have ALL these keys and ONLY *"name", "email", "phone"*, and all the values must be *"strings"*. The phone must be in this format (xx)xxxxx-xxxx. Both, *phone* and *email* must be unique. 

### Request body
```json 
{ 
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
} 
```

Following these rules, it will return status code <span style="color:green">201 - CREATED</span>

```json 
{
	"name": "John Doe",
	"email": "john@email.com",
	"phone": "(41)90000-0000",
	"creation_date": "Wed, 02 Mar 2022 03:32:52 GMT",
	"last_visit": "Wed, 02 Mar 2022 03:32:52 GMT",
	"visits": 1
}
```

IF *phone* number is in the wrong format, this is the message returned with the status code <span style="color:orange"> 400 - BADQUEST</span>

```json 
{
	"error": "phone number format is wrong!"
} 
```

IF any input is not a *string* type, this is the error message returned with the status code <span style="color:orange"> 422 - UNPROCESSABLE ENTITY</span>

```json 
{
	"error": "values must be string!"
}
```

IF you try to create a user with the same *email* or/and same *phone* number used before, this is the message you will get with the status code <span style="color:orange"> 409 - CONFLICT</span>

```json 
{
	"error": "email or/and phone already exists"
}
```
IF any required key (*email, phone, name*) is missing or any other is added to the body request, this is the message you will get with the status code <span style="color:orange"> 400 - BAD REQUEST</span>

```json 
{
	"error": "the keys must be name, email and phone"
}
```

################################################################
><h2 style="color:blue">GET <span style="color:gray">/leads</h2>

**GET** will return all users with the status code <span style="color:green"> 200 - OK</span>. 

### No request body

```json 
{
	"LEADS": [
		{
			"name": "John Doe",
			"email": "john@email.com",
			"phone": "(41)90000-0000",
			"creation_date": "Wed, 02 Mar 2022 03:32:52 GMT",
			"last_visit": "Wed, 02 Mar 2022 03:32:52 GMT",
			"visits": 1
		},
		{
			"name": "Lari",
			"email": "lari@email.com",
			"phone": "(21)90000-0000",
			"creation_date": "Wed, 02 Mar 2022 03:32:52 GMT",
			"last_visit": "Wed, 02 Mar 2022 03:32:52 GMT",
			"visits": 1
		}
	]
}
```
IF no users were found, this will be returned with the status code <span style="color:orange"> 404 - NOT FOUND</span>

```json 
{
	"error": "No result found"
}
```


---
><h2 style="color:yellow">PATCH <span style="color:gray">/leads</h2>


**PATCH** body request must have only the user's *email* and must be *string*.

The patch request will update the visits number and set the last_visit date. Each patch request will increase by 1 the visits number. 

IF the *email* is in the database and the input is a *string*, the user will be deleted and no content will be returned with the status code <span style="color:green"> 204 - NO CONTENT</span>. 

### Request body
```json 
{ 
    "email": "john@email.com",
} 
```

IF the *email* provided is not a *string* type, this is the error message returned with the status code <span style="color:orange"> 422 - UNPROCESSABLE ENTITY</span>

```json 
{
	"error": "values must be string!"
}
```

IF no users were found, this will be returned with the status code <span style="color:orange"> 404 - NOT FOUND</span>

```json 
{
	"error": "Email not found!"
}
```

IF any other key different than *email* is used, this is the eror message that will be returned with the status code <span style="color:orange"> 400 - BAD REQUEST</span>

```json 
{
	"error": "accepts only email key!"
}
```


---
><h2 style="color:red">DELETE <span style="color:gray">/leads</h2>
**DELETE** body request must have only the user's *email* and must be *string*.

 IF the *email* is in the database and the input is a *string*, the user will be deleted and no content will be returned with the status code <span style="color:green"> 204 - NO CONTENT</span>. 

### Request body

```json 
{
    "email": "lari@email.com"
}
```
IF no users were found with *email* provided, this will be returned with the status code <span style="color:orange"> 404 - NOT FOUND</span>   

```json 
{
	"error": "Email not found!"
}
```


IF the *email* provided is not a *string* type, this is the error message returned with the status code <span style="color:orange"> 422 - UNPROCESSABLE ENTITY</span>

```json 
{
	"error": "values must be string!"
}
```

IF any other key different than *email* is used, this is the eror message that will be returned with the status code <span style="color:orange"> 400 - BAD REQUEST</span>

```json 
{
	"error": "accepts only email key!"
}
```