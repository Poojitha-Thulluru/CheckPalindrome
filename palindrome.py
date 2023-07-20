def is_palindrome(given_string: str, start, end) -> int:
    if start > end:
        return 1
    if given_string[start] != given_string[end]:
        return 0
    return is_palindrome(given_string, start + 1, end - 1)


if __name__ == "__main__":
    string = input("Enter a string to check whether it is a palindrome or not : ")
    print(is_palindrome(string, 0, len(string) - 1))
