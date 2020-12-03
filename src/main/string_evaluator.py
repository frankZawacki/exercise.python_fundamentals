# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World"

    def concatenate(self, value_to_be_added_to, value_to_add):
        return value_to_be_added_to + value_to_add

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index : ending_index]

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index +1 : ending_index -1]

    def compare(self, first_value, second_value):
        return first_value == second_value

    def get_middle_character(self, string_to_fetch_from):
        middleIndex = len(string_to_fetch_from)/2
        return string_to_fetch_from[middleIndex]

    def get_first_word(self, string_to_fetch_from):
        return string_to_fetch_from.split(" ")

    def get_second_word(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1]