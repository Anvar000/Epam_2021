# I decided to write a code that generates data filtering object
# from a list of keyword parameters:

class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data
            if all(func(item) for func in self.functions)
        ]

# example of usage:
# positive_even = Filter(lamba a: a % 2 == 0, lambda a: a > 0,
#                        lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def request(key, value):
            def keyword_filter_func(item):
                if item.get(key):
                    return item[key] == value
                else:
                    raise KeyError(f"Can't find key '{key}'")

            return keyword_filter_func

        filter_funcs.append(request(key, value))
    return Filter(filter_funcs)


if __name__ == "__main__":
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly"
        }
    ]

# make_filter(name='polly', type='bird').apply(sample_data)
# should return only second entry from the list

# There are multiple bugs in this code. Find them all and
# write tests for faulty cases.

    # print(make_filter(name="Bill").apply(sample_data))
    # positive_even = Filter([lambda a: a % 2 == 0,
    #                         lambda a: a > 0, lambda a: isinstance(a, int)])
    # print(positive_even.apply(range(100)))