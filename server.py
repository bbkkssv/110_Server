from flask import Flask

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


# Coupon database
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

if __name__ == "__main__":
    app.run(debug=True)