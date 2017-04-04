#! /usr/bin/env python3
"""Classes designed to take in a string of the form

[x]d[y] (modifier)*

and return an integer total"""

import re
import random

class Roller(object):
    def __init__(self, text = None):
        if text == None:
            self.number = 1
            self.sides = 1
            self.modifiers = []
        else:
            self.inputs = text.split(' ')
            self.number, self.sides = re.split('d|D', self.inputs[0])
            self.number = int(self.number)
            self.sides = int(self.sides)
            self.modifiers = self.inputs[1:]
    
    def roll(self, sides):
        """Rolls a die with 'sides' sides"""
        return random.randint(1, sides)

    def rolls(self, number, sides):
        """Rolls 'number' dice with 'sides' sides"""
        results = []
        for i in range(number):
            results.append(self.roll(sides))
        return results

    def reroll(self, rolls_in, number, sides):
        """Takes in a list of results, a number below which to reroll,
        and the number of sides of each die, and returns a list
        where low numbers have been rerolled."""
        result = rolls_in[:]
        for i in range(len(result)):
            if result[i] <= number:
                result[i] = self.roll(sides)
        return result

    def keep(self, rolls_in, number, end):
        """Takes in a list of results, a number of results to keep, and
        a side from which to start, and returns a smaller list."""
        if end == "l" or end == 'L':
            result = sorted(rolls_in)
        elif end == "h" or end == 'H':
            result = sorted(rolls_in, reverse=True)
        else:
            raise Exception("Keep() received invalid argument")
        
        result = result[:number]
        return result
        
    def total(self, rolls_in):
        """Takes in a list of rolls, totals them and returns that"""
        result = 0
        for i in range(len(rolls_in)):
            result += rolls_in[i]
        return result
    
    def evaluate(self, text=None):
        if text is not None:
            self.inputs = text.split(' ')
            self.number, self.sides = re.split('d|D', self.inputs[0])
            self.number = int(self.number)
            self.sides = int(self.sides)
            self.modifiers = self.inputs[1:]

        roll_results = self.rolls(self.number, self.sides)

        if self.modifiers != []:
            for i in range(len(self.modifiers)):
                if self.modifiers[i][0] == 'k':
                    roll_results = self.keep(roll_results, int(self.modifiers[i][1:-1]), self.modifiers[i][-1])
                elif self.modifiers[i][0:2] == 'rr':
                    roll_results = self.reroll(roll_results, int(self.modifiers[i][2:]), self.sides)
        
        total = self.total(roll_results)
        return total