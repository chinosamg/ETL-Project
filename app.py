from flask import Flask, jsonify, render_template

# Top10 Companies 2017
Top10_Companies_2017 = [
    {
        "Rank": 1.0,
        "Company": "Walmart",
        "Additional Info": [
            {
                "Ticker": "WMT",
                "Revenues": 485873.0,
                "Profits": 13643
            }
        ]
    },
    {
        "Rank": 2.0,
        "Company": "Berkshire Hathaway",
        "Additional Info": [
            {
                "Ticker": "BRKA",
                "Revenues": 223604.0,
                "Profits": 24074
            }
        ]
    },
    {
        "Rank": 3.0,
        "Company": "Apple",
        "Additional Info": [
            {
                "Ticker": "AAPL",
                "Revenues": 215639.0,
                "Profits": 45687
            }
        ]
    },
    {
        "Rank": 4.0,
        "Company": "Exxon Mobil",
        "Additional Info": [
            {
                "Ticker": "XOM",
                "Revenues": 205004.0,
                "Profits": 7840
            }
        ]
    },
    {
        "Rank": 5.0,
        "Company": "McKesson",
        "Additional Info": [
            {
                "Ticker": "MCK",
                "Revenues": 192487.0,
                "Profits": 2258
            }
        ]
    },
    {
        "Rank": 6.0,
        "Company": "UnitedHealth Group",
        "Additional Info": [
            {
                "Ticker": "UNH",
                "Revenues": 184840.0,
                "Profits": 7017
            }
        ]
    },
    {
        "Rank": 7.0,
        "Company": "CVS Health",
        "Additional Info": [
            {
                "Ticker": "CVS",
                "Revenues": 177526.0,
                "Profits": 5317
            }
        ]
    },
    {
        "Rank": 8.0,
        "Company": "General Motors",
        "Additional Info": [
            {
                "Ticker": "GM",
                "Revenues": 166380.0,
                "Profits": 9427
            }
        ]
    },
    {
        "Rank": 9.0,
        "Company": "AT&T",
        "Additional Info": [
            {
                "Ticker": "T",
                "Revenues": 163786.0,
                "Profits": 12976
            }
        ]
    },
    {
        "Rank": 10.0,
        "Company": "Ford Motor",
        "Additional Info": [
            {
                "Ticker": "F",
                "Revenues": 151800.0,
                "Profits": 4596
            }
        ]
    }
]

# Top10 Companies 2016
Top10_Companies_2016 = [
    {
        "Rank": 1.0,
        "Company": "Walmart",
        "Additional Info": [
            {
                "Ticker": "WMT",
                "Revenues": 482130.0
            }
        ]
    },
    {
        "Rank": 2.0,
        "Company": "Exxon Mobil",
        "Additional Info": [
            {
                "Ticker": "XOM",
                "Revenues": 246204.0
            }
        ]
    },
    {
        "Rank": 3.0,
        "Company": "Apple",
        "Additional Info": [
            {
                "Ticker": "APPL",
                "Revenues": 233715.0
            }
        ]
    },
    {
        "Rank": 4.0,
        "Company": "Berkshire Hathaway",
        "Additional Info": [
            {
                "Ticker": "BRK.B",
                "Revenues": 210821.0
            }
        ]
    },
    {
        "Rank": 5.0,
        "Company": "McKesson",
        "Additional Info": [
            {
                "Ticker": "MCK",
                "Revenues": 181241.0
            }
        ]
    },
    {
        "Rank": 6.0,
        "Company": "UnitedHealth Group",
        "Additional Info": [
            {
                "Ticker": "UNH",
                "Revenues": 157107.0
            }
        ]
    },
    {
        "Rank": 7.0,
        "Company": "CVS Health",
        "Additional Info": [
            {
                "Ticker": "CVS",
                "Revenues": 153290.0
            }
        ]
    },
    {
        "Rank": 8.0,
        "Company": "General Motors",
        "Additional Info": [
            {
                "Ticker": "GM",
                "Revenues": 152356.0
            }
        ]
    },
    {
        "Rank": 9.0,
        "Company": "Ford Motor",
        "Additional Info": [
            {
                "Ticker": "F",
                "Revenues": 149558.0
            }
        ]
    },
    {
        "Rank": 10.0,
        "Company": "AT&T",
        "Additional Info": [
            {
                "Ticker": "T",
                "Revenues": 146801.0
            }
        ]
    }
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

    #return jsonify(Top10_Companies_2016)
    return jsonify(Top10_Companies_2016)

@app.route("/")
def welcome():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)