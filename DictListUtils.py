# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

def main():
    pass


def getMissingKeys(dictRef,dictToCompare):
    dictRef = {1:1, 2:2, 3:3}
    dictToCompare = {2:2}
    return dictRef.has_key(dictToCompare)

if __name__ == '__main__':
    main()