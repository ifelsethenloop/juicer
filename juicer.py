# E-juice nicotine mixing calculator
import math
from flask import Flask, render_template, request

Flask_App = Flask(__name__)

@Flask_App.route('/', methods=['GET'])
def index():
    """ Display the index page at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """ Route where to send calculator form input """

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name="
    amount = request.form['Input1']
    current = request.form['Input2']
    nic_base = request.form['Input3']
    target = request.form['Input4']

    try:
        # amount = int(input('Bottle size in (ml): '))
        # current = int(input('Current nicotine concentration of E-liquid (mg/ml): '))
        # nic_base = int(input('Nicotine base strength (mg/ml): '))
        # target = int(input('Desired nicotine strength (mg/ml): '))

        input1 = float(amount)
        input2 = float(current)
        input3 = float(nic_base)
        input4 = float(target)

        # Calculate what the new target should be from user input if current is > 0mg
        # target_converted = int(target) - int(current)
        target_converted = float(input4) - float(input2)

        # Run calculation based on 0mg ejuice
        # if current == 0:
            # result = round(amount / nic_base * target, 2)
        if input2 == 0:
            result = round(input1 / input3 * input4, 2)

        # Run calculation based on  > 0mg ejuice
        # else:
        #     result = round(amount / nic_base * target_converted, 2)
        else:
            result = round(input1 / input3 * target_converted, 2)

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            input3=input3,
            input4=input4,
            result=result,
            calculation_success=True
        )

    except ValueError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            input3=input3,
            input4=input4,
            result="Bad Input",
            calculation_success=False,
            error="Cannot perform calculation based on input"            
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()