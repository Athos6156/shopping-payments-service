from flask import Flask

app = Flask("Payments")


@app.route('/')
def hello_world():
	return 'Hello World, I am the payments service. Wheres your money?!'


@app.route('/api/payment/pay')
def accept_payment():
	return 'Hello World, I am the payments service. Wheres your money?!'


@app.route('/api/payment/refund')
def refund_payment():
	return 'Hello World, I am the payments service. Wheres your money?!'


@app.route('/api/payment/find')
def find_payment():
	return 'Hello World, I am the payments service. Wheres your money?!'


if __name__ == '__main__':
	app.run()
