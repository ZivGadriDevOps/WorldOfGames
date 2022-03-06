from os import path

SCORES_FILE_PATH = path.abspath(r"Resources/scores.txt")


def add_score_with_user(difficulty, user_name):

    points_to_add = (difficulty * 3) + 5

    try:
        with open(SCORES_FILE_PATH, 'r') as file_rw:
            data = file_rw.readlines()
            count = 0
            if len(data) > 0:
                for data_item in data:
                    count += 1
                    user_name_score = {
                        "USER_NAME": str(data_item.split(" : ")[0]),
                        "USER_SCORE": str(data_item.split(" : ")[1])
                    }
                    if user_name_score.get("USER_NAME").upper() == user_name.upper():
                        user_current_points = int(user_name_score.get("USER_SCORE"))
                        user_new_points = user_current_points + points_to_add
                        file_rw.close()
                        change_score_to_user(user_name, user_current_points, user_new_points)
                        break
                    elif count == len(data):
                        add_new_user_score(user_name, points_to_add, "a")
            else:
                add_new_user_score(user_name, points_to_add, "a")

    except FileNotFoundError:
        add_new_user_score(user_name, points_to_add, "w")


def change_score_to_user(user_name, old_score, new_score):
    try:
        reading_file = open(SCORES_FILE_PATH, "r")
        new_file_content = ""
        read = reading_file.readlines()
        max_lines = len(read)
        count = 0
        for line in read:
            count += 1
            stripped_line = line.strip()
            new_line = stripped_line.replace(f"{user_name.upper()} : {old_score}", f"{user_name.upper()} : {new_score}")
            if count == max_lines:
                new_file_content += new_line
            else:
                new_file_content += new_line + "\n"
        reading_file.close()
        if not new_file_content == "":
            writing_file = open(SCORES_FILE_PATH, "w")
            writing_file.write(new_file_content)
            writing_file.close()
    except FileNotFoundError:
        print(FileNotFoundError.with_traceback())


def add_new_user_score(user_name, score, file_mode):
    try:
        with open(SCORES_FILE_PATH, file_mode) as write_new:
            if file_mode == "a":
                write_new.write(f"\n{user_name.upper()} : {score}")
            elif file_mode == "w":
                write_new.write(f"{user_name.upper()} : {score}")
    except FileNotFoundError:
        print(FileNotFoundError.with_traceback())
