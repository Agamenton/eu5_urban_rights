from pathlib import Path

here = Path(__file__).parent
localization = here / "main_menu" / "localization"
english = localization / "english" / "aga_town_rights_l_english.yml"


def extract_variables(file_path):
    variables = {}
    start = False
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            if ':' in line:
                if start:
                    key, value = line.split(':', 1)
                    variables[key.strip()] = value.strip()
                else:
                    start = True
    return variables

def add_missing_keys(missing_variables, loc_file):
    with open(loc_file, 'a', encoding='utf-8-sig') as file:
        file.write("\n#+++++++++++++++++++++++++++++++++++++\n# Missing variables added from English localization\n")
        for key, value in missing_variables.items():
            file.write(f"{key}: {value}\n")

def main():
    find_other_localizations = localization.glob("**/*.yml")
    english_variables = extract_variables(english)

    localizations = {}
    for loc_file in find_other_localizations:
        if loc_file != english:
            other_variables = extract_variables(loc_file)
            localizations[loc_file] = other_variables

    for loc_file, other_variables in localizations.items():
        missing_variables = {key: english_variables[key] for key in english_variables if key not in other_variables}
        if missing_variables:
            print(f"Missing {len(missing_variables)} variables in {loc_file}:")
            #add_missing_keys(missing_variables, loc_file)



if __name__ == "__main__":
    main()
