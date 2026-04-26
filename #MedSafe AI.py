# MedSafe AI - Simple Google Colab Version

# Medicine interaction database
medicine_interactions = {
    ("aspirin", "warfarin"):"Warning! High risk of bleeding.",
    ("paracetamol","ibuprofen"):"Usually safe in normal doses.",
    ("metformin","insulin"):"Monitor blood sugar level carefully",
    ("aspirin", "ibuprofen"): " Ibuprofen may reduce aspirin's heart protection.",
    ("warfarin", "ibuprofen"): " Increased risk of bleeding.",
    ("warfarin", "paracetamol"): "Use cautiously. May increase bleeding risk if taken often.",
    ("metformin", "alcohol"): " Can increase risk of lactic acidosis.",
    ("insulin", "alcohol"): " Alcohol may cause low blood sugar.",
    ("aspirin", "alcohol"): " Increased stomach bleeding risk.",
    ("ibuprofen", "alcohol"): " May irritate stomach and cause ulcers.",
    ("aspirin", "ibuprofen"): " Ibuprofen may reduce aspirin's heart protection.",
    ("warfarin", "ibuprofen"): " Increased risk of bleeding.",
    ("warfarin", "paracetamol"): "Use cautiously. May increase bleeding risk if taken often.",
    ("metformin", "alcohol"): " Can increase risk of lactic acidosis.",
    ("insulin", "alcohol"): " Alcohol may cause low blood sugar.",
    ("aspirin", "alcohol"): " Increased stomach bleeding risk.",
    ("ibuprofen", "alcohol"): " May irritate stomach and cause ulcers."
          
}

# Symptom database
symptom_database = {
    
    "headache": "You may take paracetamol for mild headache. Stay hydrated and rest.",
    "fever": "Paracetamol or ibuprofen may help reduce fever. Drink plenty of fluids.",
    "cough": "Warm fluids and cough syrup may help. If cough persists, consult a doctor.",
    "cold": "Rest, hydration, and antihistamines may help relieve symptoms.",
    "stomach pain": "Avoid heavy foods. If severe pain occurs, consult a doctor.",
    "nausea": "Drink small amounts of water and avoid oily foods.",
    "dizziness": "Sit or lie down immediately and hydrate. If frequent, seek medical advice.",
    "sore throat": "Warm salt water gargles and lozenges may help.",
    "muscle pain": "Rest and mild pain relievers like ibuprofen may help.",
    "fatigue": "Ensure proper sleep, hydration, and balanced nutrition."
}

print("Welcome to medsafe AI")

while True:

    num1=input("do you want to continue?(yes/no) :")
    if num1=="yes":
        print("1️ Check Medicine Interaction")
        print("2️ Symptom Checker")

        choice = input("Enter 1 or 2: ")
        if choice == "1":
            med1 = input("Enter first medicine: ").lower()
            med2 = input("Enter second medicine: ").lower()
    
            result = medicine_interactions.get(
                (med1, med2),
                medicine_interactions.get((med2, med1),
                "No known interaction found in database."))
    
            print("\nResult:", result)

        elif choice == "2":
            symptom = input("Enter your symptom: ").lower()
            result = symptom_database.get(
                symptom,
                "Symptom not found in database."
            )
    
            print("\nResult:", result)

        else:
            print("Invalid choice. Please restart.")   
    else:
        print("THANK YOU FOR YOUR KIND VISIT :)")
        break
                 

