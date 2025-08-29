def load_blacklist(filepath="data/blacklist.txt"):
    try:
        with open(filepath, "r") as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        return []
