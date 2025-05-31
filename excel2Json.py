import pandas as pd
import json

# File paths
input_path = "D:/Sample_Upload/Sample_Upload_Telegram_Quiz_Poll.xlsx"
output_path = "D:/Sample_Upload/Sample_Upload_Telegram_Quiz_Poll_Json.json"

# Read Excel file
df = pd.read_excel(input_path)

# Convert to the required JSON format
data = []
for _, row in df.iterrows():
    question_data = {
        "question": row["question"],
        "options": [
            str(row["option_1"]).replace(",", ""),
            str(row["option_2"]).replace(",", ""),
            str(row["option_3"]).replace(",", ""),
            str(row["option_4"]).replace(",", "")
        ],
        "correctOptionIndex": row["correct_option_index"],
        "explanation": row["explanation"],
        "type": row["type"],
        "status": row["status"]
    }
    data.append(question_data)

# Write JSON file
with open(output_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"JSON data has been successfully written to {output_path}")
