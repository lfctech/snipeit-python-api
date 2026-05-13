# Companies API Documentation

## GET /api/v1/companies

### Description
Retrieves a paginated list of all companies in the Snipe-IT system. Supports filtering by company name.

### Method
GET

### Endpoint
https://develop.snipeitapp.com/api/v1/companies

### Parameters
#### Query Parameters
- **name** (string) - Optional - Company name to filter the results.

### Response
#### Success Response (200)
```json
{
  "total": 10,
  "rows": [
    {
      "id": 1,
      "name": "Company A",
      "image": "/uploads/companies/default.png",
      "created_at": {
        "formatted": "2023-11-15 10:00:00",
        "timezone": "UTC",
        "zone": "UTC"
      },
      "updated_at": {
        "formatted": "2023-11-15 10:00:00",
        "timezone": "UTC",
        "zone": "UTC"
      },
      "assets_count": 5,
      "licenses_count": 2,
      "accessories_count": 3,
      "consumables_count": 1,
      "components_count": 0,
      "users_count": 1,
      "available_actions": {
        "update": true,
        "restore": false
      }
    }
  ]
}
```

#### Error Response (401)
```json
{
  "status": "error",
  "messages": "Unauthorized",
  "payload": "invalid_token"
}
```

#### Error Response (405)
```json
{
  "status": "error",
  "messages": "Method Not Allowed",
  "payload": ""
}
```

## POST /api/v1/companies

### Description
Creates a new company in the Snipe-IT system. The 'name' field is the only required parameter.

### Method
POST

### Endpoint
https://develop.snipeitapp.com/api/v1/companies

### Parameters
#### Request Body
- **name** (string) - required - The name of the company. Defaults to "Google, inc."

### Request Example
```json
{
  "name": "Google, inc."
}
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the success of the operation.
- **payload** (object) - Contains the details of the created company.
  - **name** (string) - The name of the company.
  - **updated_at** (string) - The timestamp when the company was last updated.
  - **created_at** (string) - The timestamp when the company was created.
  - **id** (integer) - The unique identifier for the company. Defaults to 0.
- **messages** (string) - A message indicating the result of the operation.

#### Response Example (200)
```json
{
  "status": "success",
  "payload": {
    "name": "Google, inc.",
    "updated_at": "2023-11-16 10:22:49",
    "created_at": "2023-11-16 10:22:49",
    "id": 1
  },
  "messages": "Company Created Successfully"
}
```

#### Error Response (401)
- **status** (string) - Indicates an error.
- **message** (string) - A message describing the authentication error.

#### Error Response (405)
- **status** (string) - Indicates an error.
- **messages** (string) - A message describing the method not allowed error.

## GET /api/v1/companies/{id}

### Description
Retrieve the specific details of a company by its ID. This endpoint allows you to fetch all information associated with a particular company in the Snipe-IT system.

### Method
GET

### Endpoint
https://develop.snipeitapp.com/api/v1/companies/{id}

### Parameters
#### Path Parameters
- **id** (integer) - required - company id

### Response
#### Success Response (200)
- **id** (integer) - Defaults to 0
- **name** (string)
- **image** (string)
- **created_at** (object: datetime, formatted)
- **updated_at** (object: datetime, formatted)
- **assets_count** (integer) - Defaults to 0
- **licenses_count** (integer) - Defaults to 0
- **accessories_count** (integer) - Defaults to 0
- **consumables_count** (integer) - Defaults to 0
- **components_count** (integer) - Defaults to 0
- **users_count** (integer) - Defaults to 0
- **available_actions** (object)
  - **update** (boolean) - Defaults to true
  - **delete** (boolean) - Defaults to true

#### Response Example (200)
```json
{
  "id": 1,
  "name": "Example Company",
  "image": "/uploads/companies/company_image.png",
  "created_at": {
    "datetime": "2023-10-27T10:00:00+00:00",
    "formatted": "October 27, 2023"
  },
  "updated_at": {
    "datetime": "2023-10-27T10:00:00+00:00",
    "formatted": "October 27, 2023"
  },
  "assets_count": 15,
  "licenses_count": 5,
  "accessories_count": 3,
  "consumables_count": 2,
  "components_count": 8,
  "users_count": 10,
  "available_actions": {
    "update": true,
    "delete": true
  }
}
```

#### Error Response (401)
- **status** (string)
- **messages** (string)
- **payload** (string)

#### Error Response (404)
- **status** (string)
- **messages** (string)

#### Error Response (405)
- **status** (string)
- **messages** (string)
- **payload** (string)

## PUT /api/v1/companies/{id}

### Description
Updates a company's details.

### Method
PUT

### Endpoint
https://develop.snipeitapp.com/api/v1/companies/{id}

### Parameters
#### Path Parameters
- **id** (int32) - required - company id

#### Query Parameters
None

#### Request Body
- **name** (string) - required - company name

### Request Example
```json
{
  "name": "New Company Name"
}
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the status of the operation (e.g., 'success').
- **message** (string) - A message confirming the update.

#### Response Example
```json
{
  "status": "success",
  "message": "Company updated successfully"
}
```

#### Error Responses
- **401 Unauthorized**
  - **status** (string) - Indicates an authorization error.
  - **message** (string) - Error message, likely related to authentication.
- **405 Method Not Allowed**
  - **status** (string) - Indicates that the HTTP method is not allowed for this endpoint.
  - **messages** (string) - Details about why the method is not allowed.

## PATCH /api/v1/companies/{id}

### Description
Updates a part of a company's details.

### Method
PATCH

### Endpoint
https://develop.snipeitapp.com/api/v1/companies/{id}

### Parameters
#### Path Parameters
- **id** (int32) - required - company id

#### Query Parameters
None

#### Request Body
- **name** (string) - required - The new name for the company.

### Request Example
```json
{
  "name": "Updated Company Name"
}
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the status of the operation.
- **message** (string) - A message confirming the update.

#### Response Example (200)
```json
{
  "status": "success",
  "message": "Company updated successfully"
}
```

#### Error Responses
- **401 Unauthorized**
  - **status** (string) - Indicates unauthorized access.
  - **message** (string) - Error message detailing the authentication issue.
- **404 Not Found**
  - **status** (string) - Indicates the resource was not found.
  - **message** (string) - Error message indicating the company was not found.
- **405 Method Not Allowed**
  - **status** (string) - Indicates the HTTP method is not allowed.
  - **messages** (string) - Error message detailing the disallowed method.

## DELETE /api/v1/companies/{id}

### Description
Deletes a specific company from the Snipe-IT system. Requires the company's ID as a path parameter.

### Method
DELETE

### Endpoint
/api/v1/companies/{id}

### Parameters
#### Path Parameters
- **id** (int32) - required - The ID of the company to delete.

### Response
#### Success Response (200)
- **status** (string) - Indicates the success of the operation.
- **message** (string) - A message confirming the company deletion.

#### Error Response (401)
- **status** (string) - Indicates an authentication error.
- **message** (string) - A message detailing the authentication issue.

#### Error Response (404)
- **status** (string) - Indicates a "Not Found" error.
- **message** (string) - A message indicating the company was not found.

#### Error Response (405)
- **status** (string) - Indicates a method not allowed error.
- **messages** (string) - A message detailing why the method is not allowed.