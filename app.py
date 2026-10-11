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
            break_minutes = 0 if breaks == 0 else 10
            focus_minutes = total_minutes - (breaks * break_minutes)
            minutes_per_block = focus_minutes // study_blocks

            result = {
                "total_minutes": total_minutes,
                "break_minutes": break_minutes,
                "minutes_per_block": minutes_per_block,
                "study_blocks": study_blocks,
            }
        except (ValueError, KeyError):
            error = "Please enter a positive number of hours and 0 or more breaks."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)