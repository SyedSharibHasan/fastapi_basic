from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from data.database import SessionLocal, engine
from data.model import Base
from apis import candidate, employee, department
from meta.metadata import description, tags_metadata, contact


app = FastAPI(
    title="Database API",
    description=description,
    summary="EMPLOYEE DATABASE",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact=contact,
    openapi_tags=tags_metadata,
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Create the database tables if they don't already exist
Base.metadata.create_all(bind=engine, checkfirst=True)

@app.get("/")
def show_root():
    return {"Hello": "Go to 'url/docs' to view API end points"}

# Different API paths
app.include_router(candidate.router)
app.include_router(employee.router)
app.include_router(department.router)
