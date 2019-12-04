from flask import Flask, jsonify
import pyodbc


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello! Welcome to Azure Application of GS Bot."

@app.route("/home")
def home():
    return jsonify({'status': 'success', 'description': 'Endpoint is working fine.'})
	
	
@app.route("/view")
def view():
	server = 'gsbotdb.database.windows.net'
	database = 'gsbotdb'
	username = 'gsbot'
	password = 'admin!23'
	driver= '{ODBC Driver 17 for SQL Server}'
	cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("SELECT TOP (10) * FROM [dbo].[BotData]")
	row = cursor.fetchall()
	print(row)
	
	return jsonify({'status': 'success', 'description': 'Endpoint is working fine.'})


if __name__ == "__main__":
    app.run()


if __name__ == "__main__":
    app.run()

