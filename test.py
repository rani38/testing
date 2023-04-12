from flask import Flask, request, jsonify,render_template
import uuid
from read_csvfiles import fun_readcsvfile
from categoricalData import funCategoricalData
app = Flask(__name__)

# Define a dictionary of valid API keys
valid_api_keys = {}

@app.route("/",methods=["POST","GET"])
def index():
    return render_template('token.html')

#method to generate an api key
@app.route('/apigen',methods=["GET"])
def apikeygen():
    #generate an api key
    api_key = str(uuid.uuid4())

    #store the api key in dict
    valid_api_keys['api_key'] = api_key
    print(valid_api_keys,"valid_api_keys")
    response_data = {
        'api_key' : api_key
    }

    #return a json response
    return render_template('display.html',response_data = response_data)

@app.route('/upload-csv',methods=["GET","POST"])
def uploadcsvfile():
    if request.method == "GET":
        return render_template("uploadcsvfile.html")

    if request.method == "POST":
        csv_file_list = []
        csv_file1 = request.files['csv-file1']
        csv_file2 = request.files['csv-file2']
        csv_file_list.append(csv_file1)
        csv_file_list.append(csv_file2)
        print(csv_file_list)
        for file in csv_file_list:
            file_path = 'static/uploads/' + file.filename
            file.save(file_path)

        message = {"message": "file uploaded successfuly"}
        return render_template('message.html',message=message)

#method to use an api key to authorize
@app.route('/api/data',methods=["GET"])
def authorize():

    args = request.args
    path = args.get("api_key")
    #get the api_key from request headers    
    print(path)
    #check if the api_key is valid,so return the valid response
    #check if the api key is valid
    if path in valid_api_keys.values():
        data = {
            "message" : "You api key is correct"
        }

        return jsonify(data),200
    else:
        error_message ={
            "message": "not valid"
        }

        return error_message,400
    
@app.route('/dataframes',methods=["GET","POST"])
def get_dataframes():
    # extracted data frames of two files
    df,df_trail = fun_readcsvfile()
    # print(df.head())
    # funCategoricalData(df,df_trail)
    return str(df.head())

if __name__ == "__main__":
    app.run()





