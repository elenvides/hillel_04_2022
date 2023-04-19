from typing import Any


def players_repr(players: list[dict], verbose: bool = False) -> None:
    if verbose:
        print(">>>> TEAM:")

    for player in players:
        print(f"{player['name']=}, {player['age']=}, {player['number']=}")


def players_add(players: list[dict], player: dict) -> list[dict]:
    return players + [player]


def players_del(players: list[dict], name: str) -> list[dict]:
    return [player for player in players if player["name"] != name]


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    if field in players[0]:  # Check if field exists in dictionary
        for player in players:
            if isinstance(value, str):
                if player[field] == value:
                    return [player]
            elif isinstance(value, int):
                if player[field] == int(value):
                    return [player]
    return []


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """If multiple players with same name - return the first one."""
    for player in players:
        if player["name"] == name:
            return player
    return None


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        if not (user_input := input(f"Enter your choice {options}:\n")):
            break

        if user_input == "add":
            new_player = {
                "name": input("Enter player name: "),
                "age": int(input("Enter player age: ")),
                "number": int(input("Enter player number: ")),
            }
            team = players_add(players=team, player=new_player)
            print(team)

        elif user_input == "del":
            player_name = input("Enter player name to delete: ")
            team = players_del(players=team, name=player_name)
            print(team)

        elif user_input == "find":
            field = input("Enter field name: ")
            value = input("Enter value to find: ")
            result = players_find(players=team, field=field, value=value)
            print(result)

        elif user_input == "get":
            player_name = input("Enter player name: ")
            result = players_get_by_name(players=team, name=player_name)
            print(result)

        elif user_input == "repr":
            players_repr(players=team, verbose=True)

        elif user_input == "exit":
            break

        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
