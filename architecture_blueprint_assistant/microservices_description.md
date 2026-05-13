# Microservices Architecture

- **API Gateway**: Single entry point that handles routing, rate limiting, and request authentication before forwarding to downstream microservices.  
- **Auth Service**: Manages user registration, secure credential validation, and JWT token issuance with its own isolated database instance.  
- **Itinerary Service**: Core functional microservice responsible for creating, updating, and storing personalized travel itineraries.  
- **Supplier Aggregator Service**: Handles asynchronous non-blocking connection pipelines to fetch and cache third-party flight and hotel pricing metrics.  
- **Collaboration Sync Service**: Uses persistent web-socket connections to coordinate concurrent multi-user schedule mutations without blocking other application data paths.  
- **Budget Optimization Service**: High-compute algorithmic worker instance that analyzes cost metrics to isolate economical travel alternatives based on user financial triggers.  
- **Notification Service**: Event-driven worker that consumes message queue topics to dispatch real-time multi-channel push updates, SMS text alerts, and operational email receipts.  
- **Analytics & Metrics Service**: Collects real-time transactional footprints and structural tracing data to generate auditing metrics and system performance monitoring logs.
