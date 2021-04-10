from flask import Flask, render_template, request

# Declare the app
app = Flask(__name__)

# Start an app route which is '/'
@app.route('/')
# Declare the main function
def main():
    return render_template('app.html')

# Form Submission Route
"""
@app.route('/send', methods=['POST'])


def calc_size():
    if request.method == 'POST':
        # Start pulling data from form input
        length = request.form['length']
        width = request.form['width']
        height = request.form['height']
        #weight = request.form['weight']
    
        size = ''
        # Calculation 
        volume = float(length) * float(width) * float(height) 
        if volume >= 1000:
            size ='Large'
            return render_template('app.html', size=size)
        
        elif (volume >=500 and volume <1000):
            size ='Medium'
            return render_template('app.html', size=size)

        else:
            size ='Small'
            return render_template('app.html', size=size)

def calc_cost():
    if request.method == 'POST':
        # Start pulling data from form input
        #length = request.form['length']
        #width = request.form['width']
        #height = request.form['height']
        weight = request.form['weight']
        cost = 0
        # Calculation 
        if weight >= 10:
            cost = 50
            return render_template('app.html', cost=cost)
        
        elif weight >= 5:
            cost = 20
            return render_template('app.html', cost=cost)
        else:
            cost = 10
            return render_template('app.html', cost=cost)
    
"""




if __name__ == '__main__':
    app.run(host='localhost', debug=True)