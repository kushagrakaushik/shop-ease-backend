# Shop Ease Backend 🛒

<p align="center">
  <b>Fast, clean Flask backend for product listing + product creation APIs</b><br/>
  Built for quick frontend integration and demo-ready development.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-3.0.3-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/CORS-Enabled-20C997?style=for-the-badge" alt="CORS Enabled" />
  <img src="https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge" alt="Status" />
</p>

---

## ✨ Why This Project?

This backend powers a simple e-commerce flow for Shop Ease.
It keeps things lightweight and frontend-friendly, with ready-to-use JSON APIs.

- 🚀 Simple REST API responses
- 🌐 CORS enabled for frontend apps
- 📦 Seed product data included
- ✅ Server-side validation for new products
- 🧪 Great for demos, learning, and rapid prototyping

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 🍶 Flask
- 🔄 Flask-CORS

## 🗂️ Project Structure

```text
backend/
├── app.py
├── requirements.txt
└── README.md
```

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/kushagrakaushik/shop-ease-backend.git
cd shop-ease-backend
```

### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the server

```bash
python app.py
```

Backend URL:

- 🔗 http://127.0.0.1:5000

## 📚 API Reference

### `GET /products`

Returns all available products.

- ✅ Success: `200 OK`

```bash
curl http://127.0.0.1:5000/products
```

### `POST /add-product`

Creates a new product.

- ✅ Success: `201 Created`
- ❌ Validation error: `400 Bad Request`

```bash
curl -X POST http://127.0.0.1:5000/add-product \
  -H "Content-Type: application/json" \
  -d '{
    "name": "OnePlus Nord Buds 2",
    "category": "Electronics",
    "price": 2799,
    "image": "https://example.com/product.jpg",
    "description": "TWS earbuds with ANC"
  }'
```

## 🛡️ Validation Rules

When creating a product:

- `name` is required and cannot be empty
- `price` must be a valid number greater than `0`
- `category` defaults to `Uncategorized` if omitted
- `image` defaults to `https://via.placeholder.com/200` if omitted

## 🧠 Important Notes

- Data is stored in-memory inside `app.py`
- Restarting the server resets newly added products
- Best suited for local development and prototypes

## 📦 Example Success Response

`POST /add-product`

```json
{
  "message": "Product added successfully",
  "product": {
    "id": 5,
    "name": "OnePlus Nord Buds 2",
    "category": "Electronics",
    "price": 2799.0,
    "image": "https://example.com/product.jpg",
    "description": "TWS earbuds with ANC"
  }
}
```

## 🛣️ Roadmap

- [ ] Add persistent storage (SQLite/PostgreSQL)
- [ ] Add update and delete endpoints
- [ ] Add filtering, search, and pagination
- [ ] Add auth for admin-only product creation
- [ ] Add automated tests

## 📄 License

Licensed under the MIT License.
