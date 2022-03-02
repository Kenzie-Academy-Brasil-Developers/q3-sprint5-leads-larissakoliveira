<center> <h1>Leads</h1> </center>

## ENDPOINTS:

><h2 style="color:green">POST <span style="color:gray">/leads</span></h2>
 
### Request body
**POST** request must have all these keys *"name", "email", "phone"*, and all the values must be *"strings"*. The phone must be in this format (xx)xxxxx-xxxx. Both, *phone* and *email* must be unique. 

Following these rules, it will return status code <span style="color:green">201 - CREATED</span>
```json 
{ 
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
} 
```

IF *phone* number is in the wrong format, this is the message returned:

```json 
{
	"error": "phone number format is wrong!"
} 
```

IF any value is not a *string*, this is the error message returned:

```json 
{
	"error": "values must be string!"
}
```

IF you try to create a user with the same *email* or/and same *phone* number, this is the message you will get:

```json 
{
	"error": "email or/and phone already exists"
}
```



### Body returned

><h2 style="color:blue">GET <span style="color:gray">/leads</h2>

><h2 style="color:yellow">PATCH <span style="color:gray">/leads</h2>


><h2 style="color:red">DELETE <span style="color:gray">/leads</h2>
