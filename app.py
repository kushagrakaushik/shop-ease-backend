from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database
products = [
    {
        "id": 1,
        "name": "Boat Rockerz 450",
        "category": "Electronics",
        "price": 1299,
        "image": "https://m.media-amazon.com/images/I/51xxA+6E+xL._SX522_.jpg",
        "description": "Wireless Bluetooth Headphone"
    },
    {
        "id": 2,
        "name": "Noise ColorFit Pro 4",
        "category": "Electronics",
        "price": 2499,
        "image": "https://m.media-amazon.com/images/I/611ZzBpm9IL._SX679_.jpg",
        "description": "Smartwatch with Bluetooth Calling"
    },
    {
        "id": 3,
        "name": "Skybags Casual Backpack",
        "category": "Bags",
        "price": 899,
        "image": "https://m.media-amazon.com/images/I/81B-vJp+g-L._SY879_.jpg",
        "description": "Stylish and spacious backpack"
    },
    {
        "id": 4,
        "name": "Red Tape White Sneakers",
        "category": "Footwear",
        "price": 1999,
        "image": "https://m.media-amazon.com/images/I/61vYpD9nIEL._SY695_.jpg",
        "description": "Comfortable casual sneakers"
    }
]
current_id = 5

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/add-product', methods=['POST'])
def add_product():
    global current_id
    data = request.get_json()

    # Validation
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    name = data.get('name')
    price = data.get('price')
    category = data.get('category')
    image = data.get('image')
    
    if not name or not str(name).strip():
        return jsonify({"error": "Product name is required"}), 400
        
    try:
        price = float(price)
        if price <= 0:
            return jsonify({"error": "Price must be greater than 0"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Valid price is required"}), 400
        
    new_product = {
        "id": current_id,
        "name": str(name).strip(),
        "category": str(category).strip() if category else "Uncategorized",
        "price": price,
        "image": str(image).strip() if image else "https://via.placeholder.com/200",
        "description": data.get('description', '')
    }
    
    products.append(new_product)
    current_id += 1
    
    return jsonify({"message": "Product added successfully", "product": new_product}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
