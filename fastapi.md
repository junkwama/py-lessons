# FastAPI

## Path params vs query params

### Path params
- Path params are used to identify a specific resource and they are part of the URL
- Path params are required (...)  and as function arguments, they are defined with the Path function imported from fastapi lib

### Query params
- Query params are optional and they are used to filter the resources. They are defined as function arguments with a default value
- Query params are optional and can be defined with default value (None) in the function arguments