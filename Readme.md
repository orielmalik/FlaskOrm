# Flask Project with Pytest - SQL & No-SQL Libraries Research

This is an ongoing Flask project where we are exploring and researching various libraries for both SQL and No-SQL databases, while integrating Pytest for testing. The project aims to evaluate and compare different database libraries and setups for future use in a production environment.

**Requirements of Project**:
- Docker Desktop and Compose.yaml file
- Log file
- Decrypt data if needed

# Comparison of SQLAlchemy ORM, SQL EXEC Commands, and PyMongo

## Aims:

1. **Compare Performance, Usability, and Security**  
   - **SQLAlchemy ORM vs. SQL EXEC Commands with PyMySQL**  
     This section aims to evaluate the performance, usability, and security between SQLAlchemy ORM and raw SQL EXEC commands using PyMySQL. Key aspects include how both methods handle database interactions, the efficiency of each approach, and their ability to prevent security issues like SQL injection.

2. **Compare Query Complexity**  
   - **SQLAlchemy vs. PyMongo**  
     In this section, the complexity of queries will be compared between SQLAlchemy (a relational database ORM) and PyMongo (a MongoDB client). The goal is to assess the complexity of creating, reading, updating, and deleting data in both systems, highlighting the differences between working with relational and NoSQL databases.

3. **Demonstrate Knowledge**  
   - The final aim is to showcase a deep understanding of the technologies, how they interact with databases, and their trade-offs in terms of performance, ease of use, and security. This will involve a practical demonstration of the implementation and a clear explanation of the reasoning behind each approach.

```json
{
    "email": "email@example.com",
    "position": "forward",
    "speed": 10.5,
    "birth": "1990-01-02",
    "type": "type1"
}
```

- **SQLAlchemy**:
 is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL **

- **pyMysql**: This package contains a pure-Python MySQL client library, based on PEP 249. Requirements : MySQL Server

- **PyMongo**: No-SQL DB With Mongodb query language driver libary

SECURITY
- **SQL Injection & XSS Protection**: All user inputs are sanitized and validated to prevent SQL injection and Cross-Site Scripting (XSS).
- **Separation of Queries**: SQL queries are stored in separate files to maintain a clean and secure structure.
- **Prepared Statements**: The application uses prepared statements executed via `exec` to safeguard against malicious input.
- **Error Message Handling**: All error messages returned by the application are generic and do not reveal any details about the application's internal logic or structure, ensuring that potential attackers cannot infer sensitive information.




