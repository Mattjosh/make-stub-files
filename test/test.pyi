def is_known_type(s: str) -> Any: ...
    #   0: return True
    #   0: return bool
    #   1: return True
    #   1: return bool
    #   2: return is_known_type(inner) if inner else True
    #   2: return Any
    #   3: return is_known_type(inner) if inner else True
    #   3: return Any
    #   4: return True
    #   4: return bool
    #   5: return True
    #   5: return bool
    #   6: return all(is_known_type(z.strip()) for z in split_types(s3))
    # ? 6: return all(is_known_type(z.strip()) for z in split_types(s3))
    #   7: return True
    #   7: return bool
    #   8: return False
    #   8: return bool
def match_entire_string(self, s: str) -> Union[Any,bool]: ...
def return_every_kind(a: Any, b: Any) -> Union[
    Dict[List[str, str]],
    Dict[{str:str}],
    Dict[{}],
    List[number, number],
    Tuple[str, str],
    complex(number, number),
    float(number),
    int(number),
    long(number),
    number,
]: ...
def splitLines(self, s: str) -> Union[List[],str]: ...
