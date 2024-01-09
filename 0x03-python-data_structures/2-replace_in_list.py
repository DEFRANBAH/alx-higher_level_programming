#!/usr/bin/python3

#that replaces an element of a list in aspecific position like in C

def replace_in_list(my_list, idx, element):
	if idx < 0 or idx >= len(my_list):
		return my_list
	my_list[idx] = element
	return my_list
