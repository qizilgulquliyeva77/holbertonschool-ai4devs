# Benchmark Tasks – AI Productivity Sprint

## Task 1 - CRUD Endpoint with Validation
**Requirements**: Implement a REST API endpoint `POST /users` that registers a user and validates input schema.  
**Inputs**: JSON body with `{ "name": "string", "email": "string" }`  
**Outputs**: JSON body with `{ "id": "integer", "name": "string", "email": "string", "createdAt": "string" }`  
**Acceptance Criteria**:  
- Returns `201 Created` with stored user object on successful input.  
- Returns `400 Bad Request` if the email format is invalid or if fields are missing.  
- Returns `409 Conflict` if the email address already exists in the system.

## Task 2 - Data Processing and Filtering Function
**Requirements**: Write a service function that filters a product catalog array based on availability status and minimum rating, sorted by price.  
**Inputs**: An array of product objects, a boolean flag `onlyAvailable`, and a float `minRating`.  
**Outputs**: Filtered and sorted array of items matching criteria.  
**Acceptance Criteria**:  
- Items with status `available: false` must be excluded if `onlyAvailable` is true.  
- Only products with a rating greater than or equal to `minRating` are retained.  
- Final list must be ordered ascendingly by price.

## Task 3 - Utility and Helper Algorithm
**Requirements**: Implement an authorization utility function that extracts a JWT bearer token from HTTP request headers and validates expiration.  
**Inputs**: Request headers object containing `Authorization: Bearer <token_string>`.  
**Outputs**: Object with `{ "isValid": boolean, "payload": object }`.  
**Acceptance Criteria**:  
- Correctly extracts token text following the "Bearer " schema indicator.  
- Returns `isValid: false` if token is corrupted or current timestamp exceeds expiration data limit.  
- Safely decrypts or reads payload without raising uncaught program exceptions.
