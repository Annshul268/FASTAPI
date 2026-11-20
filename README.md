# FastAPI Learning Journey 🚀

A hands-on repository documenting my journey of learning **FastAPI**, from building basic APIs to implementing CRUD operations, request validation, and patient management.

The repository is organized into progressive modules, with each folder covering a specific FastAPI concept through practical Python examples.

## 📚 Learning Modules

| No. | Module | Concepts Covered |
|---|---|---|
| 01 | `1.basic_API` | Introduction to FastAPI, creating APIs, GET requests and routing |
| 02 | `2.patient_management_API` | Building a patient management API, path and query parameters |
| 03 | `3.pydantic` | Pydantic models, data validation, Field and computed fields |
| 04 | `4.Using_POST_Request` | POST requests, request body validation and creating patient records |
| 05 | `5.PUT` | Updating existing patient records using PUT requests |
| 06 | `6.DELETE` | Deleting patient records using DELETE requests |

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Data Validation:** Pydantic
- **Server:** Uvicorn
- **API Testing:** Swagger UI
- **Data Storage:** JSON

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Annshul268/FASTAPI.git
```

### 2. Navigate to the repository

```bash
cd FASTAPI
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

### 4. Run a learning module

Navigate to the folder you want to explore. For example:

```bash
cd 5.PUT
```

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

**Note:** Run the command from the folder containing `main.py`.

## 🌐 API Documentation

Once the server starts, access the following URLs:

| URL | Description |
|---|---|
| `http://127.0.0.1:8000` | API welcome endpoint |
| `http://127.0.0.1:8000/docs` | Interactive Swagger UI documentation |
| `http://127.0.0.1:8000/redoc` | ReDoc API documentation |

## 🧪 Practical Implementation

The patient management modules demonstrate practical API operations:

- **GET:** Retrieve all patient records or a specific patient's information.
- **POST:** Create new patient records with Pydantic validation.
- **PUT:** Update existing patient information.
- **DELETE:** Remove patient records.

Additional implementation concepts include:

- Path parameters and query parameters.
- Request body validation using Pydantic.
- Custom validation using `Field`.
- Computed fields for BMI and health verdict.
- Exception handling using `HTTPException`.
- Reading and writing patient records using JSON files.

## 🎯 Learning Objectives

Through this repository, I aim to develop a strong understanding of:

- Building RESTful APIs using FastAPI.
- Understanding HTTP methods and API request-response cycles.
- Validating incoming data using Pydantic.
- Implementing CRUD operations.
- Handling errors and HTTP status codes.
- Testing APIs using Swagger UI.

## 👨‍💻 Author

**Anshul Kumar Gupta**

- GitHub: [@Annshul268](https://github.com/Annshul268)

---
