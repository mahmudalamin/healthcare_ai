import random
import pandas as pd
import os
import chromadb

os.makedirs("d:/coding", exist_ok=True)

client = chromadb.Client()
collection = client.create_collection ("patient_records")

patient_id = [f"PT-{i+1:03d}" for i in range(15)]
first_name = [ "James", "Sarah", "Mohammed", "Emma", "David",
    "Fatima", "John", "Aisha", "Robert", "Grace",
    "Ahmed", "Mary", "Daniel", "Zara", "William"]
last_name = ["Smith", "Johnson", "Khan", "Williams", "Brown",
    "Patel", "Jones", "Ali", "Taylor", "Ahmed",
    "Wilson", "Begum", "Davies", "Clarke", "Evans"]
age = [44,20,90,34,56,78,60,46,23,70,47,38,55,86,67]
blood_group = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
condition = ["Type 2 Diabetes",
    "Hypertension",
    "Asthma",
    "COPD",
    "Heart Failure",
    "Atrial Fibrillation",
    "Chronic Kidney Disease",
    "Depression",
    "Anxiety Disorder",
    "Osteoarthritis",
    "Rheumatoid Arthritis",
    "Hypothyroidism",
    "Hyperlipidaemia",
    "Obesity",
    "Sleep Apnoea"]
medication = {
    "Type 2 Diabetes":         ["Metformin 500mg", "Metformin 1000mg", "Gliclazide 80mg", "Insulin Glargine"],
    "Hypertension":            ["Amlodipine 5mg", "Ramipril 10mg", "Losartan 50mg", "Bisoprolol 5mg"],
    "Asthma":                  ["Salbutamol Inhaler", "Beclometasone Inhaler", "Montelukast 10mg"],
    "COPD":                    ["Tiotropium Inhaler", "Salbutamol Inhaler", "Prednisolone 5mg"],
    "Heart Failure":           ["Furosemide 40mg", "Bisoprolol 5mg", "Ramipril 5mg", "Spironolactone 25mg"],
    "Atrial Fibrillation":     ["Warfarin 3mg", "Apixaban 5mg", "Digoxin 125mcg", "Bisoprolol 5mg"],
    "Chronic Kidney Disease":  ["Ramipril 5mg", "Furosemide 40mg", "Sodium Bicarbonate"],
    "Depression":              ["Sertraline 50mg", "Fluoxetine 20mg", "Citalopram 20mg"],
    "Anxiety Disorder":        ["Sertraline 50mg", "Propranolol 10mg", "Diazepam 2mg"],
    "Osteoarthritis":          ["Paracetamol 500mg", "Ibuprofen 400mg", "Naproxen 250mg"],
    "Rheumatoid Arthritis":    ["Methotrexate 15mg", "Hydroxychloroquine 200mg", "Prednisolone 5mg"],
    "Hypothyroidism":          ["Levothyroxine 50mcg", "Levothyroxine 100mcg"],
    "Hyperlipidaemia":         ["Atorvastatin 20mg", "Simvastatin 40mg", "Rosuvastatin 10mg"],
    "Obesity":                 ["Orlistat 120mg", "Dietary advice", "Metformin 500mg"],
    "Sleep Apnoea":            ["CPAP Therapy", "Weight management advice"]
}

data = {
    "patient_id": patient_id,
     "fname": first_name,
     "lname":last_name,
     "age":age,
     "blood_group": [random.choice(blood_group) for i in range(15)],
     "condition":condition,
     "medication":[medication[condition[i]][0] for i in range(15)]
    }
def patient_to_text(patient):
    return f"""Patient New Record
    id:{patient["patient_id"]}
    name:{patient["fname"]} {patient["lname"]}
    age:{patient["age"]}
    blood-group:{patient["blood_group"]}
    condition:{patient["condition"]}
   medication:{patient["medication"]}
    """

df=pd.DataFrame(data)
patient = df.iloc[0]
df.to_csv("d:/coding/pateintdatabase.csv", index=False)

pateint_document = []
for i in range(15):
    text= patient_to_text(df.iloc[i])
    pateint_document.append(text)
    print (text)
    print ("="*40)

collection.add(
    documents = pateint_document,
    ids = patient_id
)
print (f"Total records found: {len(pateint_document)}")
print (f"Total record documet store: {collection.count()}")