Download the file using github commands or by any other ways, extract the file and run the following commands.

To Activate the virtual Env :
cd your_repo/env/Scripts/activate.bat

Install this requireents :
pip install -r requirements.txt
pip install flask
pip install --upgrade category_encoders
pip install categorical encoders
pip install pickle-mixin

After activating the virtual env and install the respective requirements, run the .ipynb file for understanding.

About Project:
To predict the mortgage backed securities prepayment risk usimg machine learning models like Random forest and Support Vector Machines. Deployment done using flask and heroku.

About Dataset :
The data is obtained from Freddie Mac official portal for home loans. The size of the home loans data is (291452 x 28). It contains 291452 data points and 28 columns or parameters which denote different features of the data.

Some of the noteworthy features of the dataset are:
Credit score of the client, The maturity date of the mortgage, The amount or percentage of insurance on the mortgage, Debt to income ration of the borrower, Mortgage interest rate, Prepayment Penalty Mortgage - denotes if there is any penalty levied on prepayment of loan, Loan sequence number - denotes the unique loan ID, The purpose of the loan, The number of borrowers issued on the loan, The property type, the state in which property is and its postal code and address, The information about the seller and service company. HARP indicator – denotes if the loan is HARP or non-HARP and Interest only indicator - Denotes if the loan requires only the interest
payments over the period of maturity or not.

Conclusion:

Above the output predicted by our model is There is a risk of prepayment . if there a prepayment risk for the loan then the model predicts No risk of prepayment.

Deployment link :
https://prepayment-prediction.herokuapp.com/
