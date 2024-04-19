import json
from difflib import get_close_matches


def write_data(queries_answers):
    with open("questions_answers.json", "w") as file:
        json.dump(queries_answers, file, indent=2)


def closest_matches(query, questions):
    matches = get_close_matches(query, questions, cutoff=0.6)
    return matches[0] if matches else None


def load_data():
    with open("questions_answers.json", "r") as file:
        return json.load(file)

queries_answers = load_data()

def find_answer(query, question_answers):
    for question_answer in question_answers:
        if question_answer["question"] == query:
            return question_answer["answer"]
            break


while True:
    user_query = input().strip()
    if user_query == "q":
        break

    finded_answer = ""
#    for query_answer in queries_answers["questions"]:
    all_queries = [soru_cevaplar["question"] for soru_cevaplar in queries_answers["questions"]]
    closest_result = closest_matches(user_query, all_queries)
    if closest_result:
        finded_answer = find_answer(closest_result, queries_answers["questions"])
        if finded_answer:
            print(finded_answer)


    if user_query == "skip":
        break

    if not finded_answer:
        print(f"Bilemedim ama ogrenmek isterim : ")
        new_answer = input()
        queries_answers["questions"].append({"question": user_query, "answer": new_answer})
        write_data(queries_answers)
        queries_answers = load_data()





