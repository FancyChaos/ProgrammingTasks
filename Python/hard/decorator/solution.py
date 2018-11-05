def tag(tag_name):
    def tag_dec(func):
        def func_wrapper(*args, **kwargs):
            tags = tag_name.split()[::-1]
            s = "{text}"
            for t in tags:
                s = "<" + t + "> " + s + " </" + t + ">"
            return s.format(text=func(*args, **kwargs))
        return func_wrapper
    return tag_dec


@tag("p div span")
def wrap(text):
    return text


if __name__ == "__main__":
    print(wrap("Test"))
