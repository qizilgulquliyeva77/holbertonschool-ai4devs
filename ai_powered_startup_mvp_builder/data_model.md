# Data Model

### 1. User
- **id**: UUID (PK)
- **email**: String (Unique)
- **github_token**: String

### 2. Project
- **id**: UUID (PK)
- **user_id**: FK (User.id)
- **tech_stack**: Enum (Python, JS, CPP)

### 3. Requirement
- **id**: UUID (PK)
- **project_id**: FK (Project.id)
- **content**: Text
- **priority**: Enum (Must, Should, Nice)
