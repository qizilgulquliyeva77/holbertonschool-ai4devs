# API Requirements – Inventory API

## Domain
E-commerce inventory management

## Target Users
- Developers: manage product stock
- Analysts: generate stock reports

## Core Operations
- Create product
- Update stock
- Get product by ID
- Search products
- Delete product
- Bulk update inventory
- Get low stock alerts
- Reserve stock for order

## Data Rules
- SKU must be unique
- Price must be > 0

## Non-Functional
- Response time < 200ms
- JWT authentication required
- Rate limit 100 req/min
