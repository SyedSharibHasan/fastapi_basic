description = """
This API is to interact with employee_database, having following tables

## Candidate
* You can do **CRUD** operations
* Get all candidates with pattern matching on _name_ & _skills_.

## Department
* You can do **CRUD** operations
* Get all departments.

## Employee
* You can do **CRUD** operations
* Get all employee.
* While an existing employee is added as a new employee, his previous end date will be changed to current date and new employee is created.

"""


tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic and Token based authentications are also here. **_Not implemented_**.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
    {
        "name": "candidates",
        "description": "Manage candidates. CRUD operations and get all candidates.",
    },
    {
        "name": "departments",
        "description": "Manage departments. CRUD operations and get all departments.",
    },
    {
        "name": "employees",
        "description": "Manage employees. CRUD operations and get all employees.",
    },
]


contact={
        "name": "Akhil",
        "url": "https://www.akhil.pl/",
        "email": "akhilp@datapmi.com",
    }