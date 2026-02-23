project/
├── src/ # <-- all importable code lives here
│ ├── core/ # Business logic, reusable across services
│ ├── api/ # FastAPI (or Flask, gRPC) endpoints
│ ├── data/ # ETL helpers, dataset loaders
│ ├── models/ # ML/DL model classes + training loops
│ ├── utils/ # Tiny helpers: logging, timers, etc.
│ └── config/ # Pydantic or YAML-backed settings
