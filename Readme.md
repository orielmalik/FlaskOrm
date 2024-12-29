# Flask Project with Pytest - SQL & No-SQL Libraries Research

This is an ongoing Flask project where we are exploring and researching various libraries for both SQL and No-SQL databases, while integrating Pytest for testing. The project aims to evaluate and compare different database libraries and setups for future use in a production environment.

**Requirements of Project**:
- Docker Desktop and Compose.yaml file
- Log file
- Decrypt data if needed





ORM VS DIRECT COMMANDS

- **SQLAlchemy**:
 is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL **

- **pyMysql**: This package contains a pure-Python MySQL client library, based on PEP 249. Requirements : MySQL Server


SECURITY
- **SQL Injection & XSS Protection**: All user inputs are sanitized and validated to prevent SQL injection and Cross-Site Scripting (XSS).
- **Separation of Queries**: SQL queries are stored in separate files to maintain a clean and secure structure.
- **Prepared Statements**: The application uses prepared statements executed via `exec` to safeguard against malicious input.
- **Error Message Handling**: All error messages returned by the application are generic and do not reveal any details about the application's internal logic or structure, ensuring that potential attackers cannot infer sensitive information.




