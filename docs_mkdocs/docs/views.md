# API Endpoints

## Operation

ViewSet: OperationViewSet  
Model: Operation  
Serializer: OperationSerializer  
Base URL: /api/operations/

---

### Available Actions

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/operations/ | List all operations |
| POST | /api/operations/ | Create new operation |
| GET | /api/operations/{id}/ | Retrieve specific operation |
| PUT | /api/operations/{id}/ | Fully update operation |
| PATCH | /api/operations/{id}/ | Partially update operation |
| DELETE | /api/operations/{id}/ | Delete operation |

---

### Request/Response Examples

List Operations (GET /api/operations/)
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "normative_time": 120,
            "allocated_resources": 5,
            "resource_availability_coefficient": 0.85,
            "labor_productivity_coefficient": 0.92,
            "duration_estimate": 98.7
        },
        {...}
    ]
}

```