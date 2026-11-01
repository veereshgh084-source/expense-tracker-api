
from fastapi import FastAPI
from pydantic import BaseModel          #DEFINES THE STRUCUTURE OF INCOMING DATA
app=FastAPI()                           #CREATES AN API APPLICATION
class Expense(BaseModel):
    title:str
    amount:float
    category:str

expenses=[]                             #TEMP STORAGE
@app.get("/")                            #CREATES A GET ENDPOINT
def home():                               #DEFINES A PYTHON FUNCTION
    return{"message":"welcome to expense Tracker API"}  #SENDS JSON RESPONSE

@app.post("/expenses")                      #CREATE POST END POINT 
def create_expense(expense:Expense):
    new_expense=expense.model_dump()
    new_expense["id"]=len(expenses)+1
    expenses.append(new_expense)          #MODELDUMP CONVERTS THE PYDANTIC MODEL INTO PY DICT
    return new_expense
    #     "message":"Expense added sucusfully",
    #     "expense":expense                   #ACCEPTS AND VALIDATES EXPENSE DATA
    # }

#GET RETRIVE ALLL DATA
@app.get("/expenses")                       #THIS CREATES A ENDPOINT
def get_expenses():
    return{
        "total_expenses":len(expenses),
        "expenses":expenses
    }

@app.put("/expenses/{id}")
def update_id(id:int,update_exp:Expense):
    for expense in expenses:
        if expense["id"] == id:
            expense["title"]=update_exp.title
            expense["amount"]=update_exp.amount
            expense["category"]=update_exp.category
            return{
                "message":"expenses updated",
                "expense":expense
            }
    raise HTTPException(status_code=404,detail="expense not found")