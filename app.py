from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            hours = float(request.form["hours"])
            breaks = int(request.form["breaks"])

            if hours <= 0 or breaks < 0:
                raise ValueError

            total_minutes = round(hours * 60)
            study_blocks = breaks + 1
            minutes_per_block = total_minutes // study_blocks

            result = {
                "total_minutes": total_minutes,
                "study_blocks": study_blocks,
                "breaks": breaks,
                "minutes_per_block": minutes_per_block
            }

        except (ValueError, KeyError):
            error = "Please enter positive study hours and 0 or more breaks."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)