"""
Define a function called count_evens.

The count_evens function accepts a non-empty list of integers called readings.

The count_evens function must return a tuple that contains two integers.
The first value in the tuple must be the number of even integers in the list called readings.
The second value must be the sum of the even integers in the list called readings.

You may not modify the list passed as an argument in any way, even temporarily, if you do you
will earn zero marks for this question.

You must provide a full docstring for this function including all pre- and post-conditions.
You must create two useful and different doctests for this function.
No main function is required.
"""


def count_evens(readings):
    """
    Counts and sum up all the even numbers in the list.

    :param readings: a non-empty list which consists only of integers
    :precondition: readings must be a non-empty list
    :precondition: readings must consist only of integers
    :postcondition: the numbers and the sum of even integers in the list are calculated correctly
    :return: a tuple consists of 'the number of even integers in readings' and 'the sum of the even integers'

    >>> count_evens([2, 4, 5, 9])
    (2, 6)
    >>> count_evens([3])
    (0, 0)
    """

    count_of_even_integers = 0
    sum_of_even_integers = 0

    for integer in readings:
        if integer % 2 == 0:
            sum_of_even_integers += integer
            count_of_even_integers += 1

    tuple_to_be_returned = (count_of_even_integers, sum_of_even_integers)

    return tuple_to_be_returned


def main():
    """Execute the program."""

    list_main_1 = [3, 4, 5, 8, 9]
    print("when", list_main_1, "is given to this function, the result is", count_evens(list_main_1))

    list_main_2 = [10, 2, 1]
    print("when", list_main_2, "is given to this function, the result is", count_evens(list_main_2))


if __name__ == '__main__':
    main()
