from flask import Flask, jsonify

# Top10 Companies 2017
Top10_Companies_2017 = [
    {"Walmart": "#1"},
    {"Berkshire Hathaway": "#2"},
    {"Apple": "#3"},
    {"Exxon Mobil": "#4"},
    {"McKesson": "#5"},
    {"UnitedHealth Group": "#6"},
    {"CVS Health": "#7"},
    {"General Motors": "#8"},
    {"AT&T": "#9"},
    {"Ford Motor": "#10"}
]

# Top10 Companies 2016
Top10_Companies_2016 = [
    {"Walmart": "#1"},
    {"Exxon Mobil": "#2"},
    {"Apple": "#3"},
    {"Berkshire Hathaway": "#4"},
    {"McKesson": "#5"},
    {"UnitedHealth Group": "#6"},
    {"CVS Health": "#7"},
    {"General Motors": "#8"},
    {"Ford Motor": "#9"},
    {"AT&T": "#10"}
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
def Top10_Company_2017():
    """Return the Forbes Top10 in 2017data as json"""

    return jsonify(Top10_Companies_2017)

#################################################

@app.route("/api/v2.0/Top10_2016")
def Top10_Company_2016():
    """Return the Forbes Top10 in 2016 data as json"""

    return jsonify(Top10_Companies_2016)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Forbes 500 Top 10 Companies of 2017!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/Top10_2017<br/>"
        f"/api/v2.0/Top10_2016"
    )


if __name__ == "__main__":
    app.run(debug=True)


