================
CODE SNIPPETS
================
TITLE: GET /api/v1/suppliers
DESCRIPTION: Retrieves a list of suppliers. Supports filtering by various supplier attributes.

SOURCE: https://snipe-it.readme.io/reference/suppliers

LANGUAGE: APIDOC
CODE:
```
## GET /api/v1/suppliers

### Description
Retrieves a list of suppliers. Supports filtering by various supplier attributes such as name, address, city, country, and more.

### Method
GET

### Endpoint
https://develop.snipeitapp.com/api/v1/suppliers

### Parameters
#### Query Parameters
- **name** (string) - Optional - Filter by supplier name.
- **address** (string) - Optional - Filter by supplier address.
- **address2** (string) - Optional - Filter by supplier address line 2.
- **city** (string) - Optional - Filter by supplier city.
- **zip** (string) - Optional - Filter by supplier zip code.
- **country** (string) - Optional - Filter by supplier country.
- **fax** (string) - Optional - Filter by supplier fax number.
- **email** (string) - Optional - Filter by supplier email address.
- **url** (string) - Optional - Filter by supplier URL.
- **notes** (string) - Optional - Filter by supplier notes.

### Request Example
```bash
curl --request GET \
     --url https://develop.snipeitapp.com/api/v1/suppliers \
     --header 'Accept: application/json' \
     --header 'Authorization: Bearer YOUR_API_KEY'
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the success of the operation.
- **messages** (object) - Contains a list of messages related to the operation.
- **payload** (array) - An array of supplier objects.
  - **supplier** (object)
    - **id** (integer) - The unique identifier for the supplier.
    - **name** (string) - The name of the supplier.
    - **city** (string) - The city where the supplier is located.
    - **country** (string) - The country where the supplier is located.
    - **email** (string) - The email address of the supplier.
    - **created_at** (string) - The timestamp when the supplier was created.
    - **updated_at** (string) - The timestamp when the supplier was last updated.

#### Response Example
```json
{
  "status": "success",
  "messages": [],
  "payload": [
    {
      "id": 1,
      "name": "Example Supplier",
      "city": "Example City",
      "country": "Example Country",
      "email": "contact@example.com",
      "created_at": "2023-01-01T10:00:00Z",
      "updated_at": "2023-01-01T10:00:00Z"
    }
  ]
}
```

#### Error Response (400)
- **status** (string) - Indicates the failure of the operation.
- **messages** (object) - Contains a list of error messages.
```json
{
  "status": "error",
  "messages": {
    "error": "Invalid parameter provided."
  }
}
```