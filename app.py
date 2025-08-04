from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS globally

# Dummy user data
user_data = {
    "name": "Sai",
    "referral_code": "SAI4113",
    "total_donations": 1500
}

# Dummy leaderboard data
leaderboard_data = [
    {"name": "sai", "donations": 1500},
    {"name": "narasimha", "donations": 1200},
    {"name": "jhansi", "donations": 900},
    {"name": "akash", "donations": 800},
]

@app.route('/api/user')
def get_user():
    return jsonify(user_data)

@app.route('/api/leaderboard')
def get_leaderboard():
    return jsonify(leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)
