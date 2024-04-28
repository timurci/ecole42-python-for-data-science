def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, str(type(object)))
    elif isinstance(object, bool) and not object:
        print("Fake:", object, str(type(object)))
    elif isinstance(object, float) and object != object:
        print("Cheese:", object, str(type(object)))
    elif isinstance(object, int) and object == 0:
        print("Zero:", object, str(type(object)))
    elif isinstance(object, str) and len(object) == 0:
        print("Empty:", object, str(type(object)))
    else:
        print("Type not found")
        return 1
    return 0
