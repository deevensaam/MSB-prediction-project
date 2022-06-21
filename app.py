from flask import Flask,render_template,request,url_for,jsonify,redirect
import pandas as pd
import numpy as np
import pickle

with open('pipe_rf.pkl' , 'rb') as f:
  model1 = pickle.load(f)

app = Flask(__name__)


@app.route("/", methods =['GET','POST'])

def home():
    
    return render_template("index.html")


@app.route("/output", methods =['GET','POST'])

def output():
    features=[]
    CreditScore=request.json['user_CreditScore']
    CreditScore=int(CreditScore)
    features.append(CreditScore)

    FirstTimeHomebuyer=request.json['user_FirstTimeHomebuyer']
    features.append(FirstTimeHomebuyer)
    
    MSA=request.json['user_MSA']
    MSA=int(MSA)
    features.append(MSA)
    
    MIP=request.json['user_MIP']
    MIP=int(MIP)
    features.append(MIP)
    
    Units=request.json['user_Units']
    features.append(Units)
    
    Occupancy=request.json['user_Occupancy']
    features.append(Occupancy)
    
    OCLTV=request.json['user_OCLTV']
    OCLTV=int(OCLTV)
    features.append(OCLTV)

    DTI=request.json['user_DTI']
    DTI=int(DTI)
    features.append(DTI)

    OrigUPB=request.json['user_OrigUPB']
    OrigUPB=int(OrigUPB)
    features.append(OrigUPB)

    OrigInterestRate=request.json['user_OrigInterestRate']
    OrigInterestRate=int(OrigInterestRate)
    features.append(OrigInterestRate)

    Channel=request.json['user_Channel']
    features.append(Channel)


    PPM=request.json['user_PPM']
    features.append(PPM)

    PropertyState=request.json['user_PropertyState']
    features.append(PropertyState)

    PropertyType=request.json['user_PropertyType']
    features.append(PropertyType)

    LoanPurpose=request.json['user_LoanPurpose']
    features.append(LoanPurpose)

    OrigLoanTerm=request.json['user_OrigLoanTerm']
    OrigLoanTerm=int(OrigLoanTerm)
    features.append(OrigLoanTerm)

    NumBorrowers=request.json['user_NumBorrowers']
    features.append(NumBorrowers)

    SellerName=request.json['user_SellerName']
    features.append(SellerName)

    ServicerName=request.json['user_ServicerName']
    features.append(ServicerName)

    MonthsDelinquent=request.json['user_MonthsDelinquent']
    MonthsDelinquent=int(MonthsDelinquent)
    features.append(MonthsDelinquent)

    MonthsInRepayment=request.json['user_MonthsInRepayment']
    MonthsInRepayment=int(MonthsInRepayment)
    features.append(MonthsInRepayment)

    feat = [np.asarray(features)]
    
    t_2=pd.DataFrame(feat)
    t_2.rename(columns = {0:'CreditScore', 
                   1:'FirstTimeHomebuyer',
                  2:'MSA', 
                   3:'MIP',
                  4:'Units', 
                   5:'Occupancy',
                  6:'OCLTV', 
                  7:'DTI',
                  8:'OrigUPB',
                   9:'OrigInterestRate',
                   10:'Channel',              
                   11:'PPM',
                   12:'PropertyState',
                   13:'PropertyType',
                   14:'LoanPurpose',
                   15:'OrigLoanTerm',
                   16:'NumBorrowers',
                    17:'SellerName',
                   18:'ServicerName',
                   19:'MonthsDelinquent',
                   20:'MonthsInRepayment',

                             }, 
        inplace = True)
    
   
    prediction = model1.predict(t_2)
    pre=int(prediction)

    if pre == 0:
        risk = 'There is a risk of prepayment.'
    else:
        risk = 'No risk of prepayment.'

    sen= ('Prediction: {}'.format(risk))    

    return jsonify(sen)
   
    
 

if __name__ == "__main__":
    app.run(debug=False)
    
    
