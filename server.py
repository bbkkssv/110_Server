from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask Framework"

@app.route("/hello", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

# http://127.0.0.1:5000/cohort-63
@app.route("/cohort-63", methods=["GET"])
def cohort63():
    student_list = ["Robert", "Barney", "Luis", "Lemuel", "Reece", "John", "Angel"]
    return student_list

# http://127.0.0.1:5000/cohort-99
@app.route("/cohort-99", methods=["GET"])
def cohort99():
    student_list = ["Pam", "Dwight", "Michael", "Angela"]
    return student_list

@app.route("/contact", methods=["GET"])
def contact():
    information = {
        "email": "lmiranda@sdgku.edu",
        "phone": "619 1234567"
    }
    return information

@app.route("/course-information", methods=["GET"])
def course_information():
    course_data = {
        "title": "Introduction Web API with Flask",
        "duration": "4 Sessions",
        "level": "Beginner"
    }
    return course_data

# Path Parameter
# Is a dynamic part of the URL used to identify a specific item or resource within an API.
# http://127.0.0.1:5000/greet/john
@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    print(f"this is the name {name}")
    return jsonify({"message": f"Hello, {name}"}), 200 # OK


# ------------------------- PRODUCTS -------------------------

products = [
    {
        "_id": 1,
        "title": "Nintendo Switch",
        "price": 499.99,
        "category": "Electronics",
        "image": "https://picsum.photos/seed/1/300/300"
    },
    {
        "_id": 2,
        "title": "Smart Refrigerator",
        "price": 999.99,
        "category": "Kitchen",
        "image": "https://picsum.photos/seed/2/300/300"
    },
    {
        "_id": 3,
        "title": "Bluetooth Speaker",
        "price": 79.99,
        "category": "Electronics",
        "image": "https://picsum.photos/seed/3/300/300"
    },
]

# GET /api/products, endpoint that returns a list of products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully",
        "products": products
    }), 200 # OK

# GET /api/products/3
@app.route("/api/products/<int:product_id>")
def get_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), 200 # OK
    
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 # Not Found

# POST /api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    print(new_product)
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Product created successfully",
        "data": new_product
    }), 201 # Created


# --------------------------------Coupon database-------------------------
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

# GET /api/coupons - Returns all coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons

# GET /api/coupons/count - Returns the total number of coupons
@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    count = len(coupons)
    return {"count": count}

# POST /api/coupons - Adds a new coupon to the coupons list
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    coupons.append(new_coupon)
    return jsonify({
        "success": True,
        "message": "Coupon added successfully",
        "data": new_coupon
    }), 201 # Created

# GET /api/coupons/<int:id> - Returns a coupon that matches the given id
@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify({
                "success": True,
                "message": "Coupon retrieved successfully",
                "data": coupon
            }), 200 # OK
    
    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), 404 # Not Found

if __name__ == "__main__":  # Checks if the script is run directly and not imported as a module to see if debug is run.
    app.run(debug=True)