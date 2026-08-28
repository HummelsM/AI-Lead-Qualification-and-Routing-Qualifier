from flask import Flask, jsonify, request

app = Flask(__name__)

def qualify_and_route_lead(data):
    score = 0

    intent = data.get("intent", "").lower()
    urgency = data.get("urgency", "").lower()
    company_size = data.get("company_size", 0)

    # Intent
    if intent == "high":
        score += 30
    elif intent == "medium":
        score += 15

    # Urgency
    if urgency == "high":
        score += 25
    elif urgency == "medium":
        score += 15

    # Company size
    if company_size >= 100:
        score += 20
    elif company_size >= 50:
        score += 15
    elif company_size >= 10:
        score += 10
    else:
        score += 5

    category = data.get("category", "").lower()

    if category in [
        "business automation",
        "ai classification",
        "lead automation",
        "api integration",
        "data processing automation"]:
        score += 20

    # Routing
    if score >= 70:
        priority = "High"
        recommended_action = "Sales follow-up"
    elif score >= 35:
        priority = "Medium"
        recommended_action = "Standard response"
    else:
        priority = "Low"
        recommended_action = "To be evaluated later"

    return {
        "score": score,
        "priority": priority,
        "recommended_action": recommended_action
    }

'''
@app.route("/api/qualify-lead", methods=["POST"])
def handle_lead():
    incoming_data = request.get_json()

    if not incoming_data:
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    result = qualify_and_route_lead(incoming_data)

    response_data = {
        "status": "success",
        "lead_received": incoming_data,
        "qualification": result
    }

    return jsonify(response_data), 201

'''

@app.route("/api/qualify-lead", methods=["GET", "POST"])
def handle_lead():

    if request.method == "GET":
        return jsonify({"message": "Endpoint exists"})

    incoming_data = request.get_json(silent=True)

    print("RAW JSON RECEIVED:", incoming_data)

    if not incoming_data:
        return jsonify({
            "error": "Invalid or missing JSON payload",
            "received": incoming_data
        }), 400

    result = qualify_and_route_lead(incoming_data)

    return jsonify({
        "status": "success",
        "lead_received": incoming_data,
        "qualification": result
    })

@app.route("/", methods=["GET"])
def home():
    return {"status": "running"}

@app.route("/test", methods=["GET"])
def test():
    return {"message": "test works"}



import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
