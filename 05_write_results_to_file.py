import pandas as pd

# write results to file if user wants
def write_results_to_file(team_name, results):
    # ask user if they want to write results to file
    write_to_file = input("Do you want to write these results to file? (y/n): ")
    if write_to_file.upper() == "Y":
        filename = f"{team_name.replace(" ", "_")}.csv"
        results.to_csv(filename, index=False)
        print(f"Results saved to {filename}")


data = {
    "Manu": [1, 1, 2],
    "Mieke": [25, 30, 35],
}

df = pd.DataFrame(data)
write_results_to_file("Crash Team Racers", df)