from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Union
import re

app = FastAPI()

# 🔹 Replace these with your actual details
FULL_NAME = "john_doe"
DOB = "17091999"  # format: ddmmyyyy
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class DataRequest(BaseModel):
    data: List[str]

def process_data(data: List[str]):
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    sum_numbers = 0

    concat_alpha = []

    for item in data:
        if re.fullmatch(r"-?\d+", item):  # it's a number
            num = int(item)
            sum_numbers += num
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        elif item.isalpha():  # alphabets
            alphabets.append(item.upper())
            concat_alpha.append(item)
        else:  # special chars
            special_characters.append(item)

    # alternating caps in reverse order
    concat_string = ""
    rev = "".join(concat_alpha)[::-1]
    for i, ch in enumerate(rev):
        if i % 2 == 0:
            concat_string += ch.upper()
        else:
            concat_string += ch.lower()

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(sum_numbers),
        "concat_string": concat_string
    }

@app.post("/bfhl")
async def bfhl(request: DataRequest):
    try:
        return process_data(request.data)
    except Exception as e:
        return {"is_success": False, "error": str(e)}