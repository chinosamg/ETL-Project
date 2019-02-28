from flask import Flask, jsonify

# Dictionary of Top10 Companies
Top10_Companies = [
    {"Company": "Walmart", "Rank": "#1"},
    {"Company": "Berkshire Hathaway", "Rank": "#2"},
    {"Company": "Apple", "Rank": "#3"},
    {"Company": "Exxon Mobil", "Rank": "#4"},
    {"Company": "McKesson", "Rank": "#5"},
    {"Company": "UnitedHealth Group", "Rank": "#6"},
    {"Company": "CVS Health", "Rank": "#7"},
    {"Company": "General Motors", "Rank": "#8"},
    {"Company": "AT&T", "Rank": "#9"},
    {"Company": "Ford Motor", "Rank": "#10"}
]

# Dictionary of Stock Price end 2017
Top10_Stock = [
    {"Company": "Walmart", "Stock Price": "1"},
    {"Company": "Berkshire Hathaway", "Stock Price": "2"},
    {"Company": "Apple", "Stock Price": "3"},
    {"Company": "Exxon Mobil", "Stock Price": "4"},
    {"Company": "McKesson", "Stock Price": "5"},
    {"Company": "UnitedHealth Group", "Stock Price": "6"},
    {"Company": "CVS Health", "Stock Price": "7"},
    {"Company": "General Motors", "Stock Price": "8"},
    {"Company": "AT&T", "Stock Price": "9"},
    {"Company": "Ford Motor", "Stock Price": "10"}
]

#################################################

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/Top10_2017")
def Top10_Company():
    """Return the Forbes500 Top10 data as json"""

    return jsonify(Top10_Companies)

#################################################

@app.route("/api/v2.0/Top10_Stock_Price")
def Top10_Stock_Price():
    """Return the Forbes500 Top10 Stock Price data as json"""

    return jsonify(Top10_Stock)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Forbes 500 Top 10 Companies of 2017!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/Top10_2017<br/>"
        f"/api/v2.0/Top10_Stock_Price"
    )


if __name__ == "__main__":
    app.run(debug=True)


