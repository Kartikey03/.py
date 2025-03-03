# python script to perform write, read and search operations on a csv file


'''
QUES. By default 2 records in  a csv file are separated with a new line character, How can this
      new line character be removed ?
ANS.  At the time opening the csv file we'll set the newline to a blank string.

QUES. The default delimiter between each field of a record in a csv file is a comma. How can the defalut delimiter 
      can be changed at the time of creating the writer object ?
ANS.  Using the writer function of csv module by setting the value of delimiter parameter to the desired parameter.
'''