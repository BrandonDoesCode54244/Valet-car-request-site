from flask import Flask, render_template, request
import os
import win32print
import win32api

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        unit = request.form['unit']
        car = request.form['car']
        time_needed = request.form['time']

        # Create ticket content
        ticket_text = f"Unit: {unit}\nCar Info: {car}\nPickup Time: {time_needed}"

        # Save ticket to file (optional)
        with open('ticket.txt', 'w') as f:
            f.write(ticket_text)

        printer_name = "SHARP MX-C357F"  # <- replace this with your printer name

        handle = win32print.OpenPrinter(printer_name)
        try:
            win32api.ShellExecute(0, "printto", "ticket.txt", f'"{printer_name}"', ".", 0)
        finally:
            win32print.ClosePrinter(handle)

        return "Ticket submitted and sent to printer!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
