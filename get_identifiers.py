# necessary libraries -------->
import re

# functions definition -------->
def get_identifiers_from_file(filename):
    # local variables
    modules_list = []
    tf_re = r"(.*tf\..*)|(.*tensorflow\..*)"
    re_tokenizer = r"(tf\.[a-zA-Z_\.]+)|(tensorflow\.[a-zA-Z_\.]+)"
    # open file
    with open(filename, 'r') as source_code:
        # get all the lines contained by the file
        lines_array = source_code.readlines()
        # iterate through each line looking for used tensorflow modules
        for line in lines_array:
            # tf module(s) found
            if re.search(tf_re, line):
                print(line)
                print(re.findall(re_tokenizer,line))

# include all the modules/classes/functions/members that go after tf
