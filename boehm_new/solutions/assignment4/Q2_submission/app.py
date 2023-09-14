from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index_schedule.html')
def schedule():
    return render_template('index_schedule.html')

@app.route('/subscribe', methods=["POST"])
def subscribe():
    lines = []
    # Open the file
    with open("subscribers.txt", "a+") as file:
        # Move read cursor to the start of file.
        file.seek(0)
        lines = file.readlines()
        for line in lines:
            if line.rstrip('\n') == request.form.get("email_address"):
                file.close()
                return "Error! This address is already in the list"

        file.seek(0)
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")

        file.write(request.form.get("email_address"))
        file.close()
        return "Thanks! for subscribing"

if __name__ == "__main__":
    app.run(debug=False)