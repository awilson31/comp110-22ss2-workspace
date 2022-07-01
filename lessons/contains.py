""Example of writing a function to process a list.""

#DEFINE A FUNCTION
def main() -> None:
    """Entrypoint of program."""
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kevin", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in the haystack"""
    # Move throught each item in list until needle is found
    i: int = 0 
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1

    return False


if __name__ == "__main__":
    main()
    #Name 'contains'
    # Two parameter (needle (str), haystack (list[str]))
    # Return True if needle is found in the haystack
        # Move throught each item in list until needle is found
        # As soon as needle is found return True
        # If all items have been checked return False