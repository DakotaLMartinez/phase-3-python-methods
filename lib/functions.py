#!/usr/bin/env python3

def greet_programmer():
    """
    greet_programmer() prints "Hello, programmer!"
    """
    print("Hello, programmer!")

def greet(name):
    '''greet(name) accepts a name and includes it in a greeting'''
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    '''accepts an optional name and includes it in a greeting'''
    print(f"Hello, {name}!")

def add(num1, num2):
    '''accepts 2 numbers and returns their sum'''
    return num1 + num2

def halve(number):
    '''accepst a number as an argument and returns half its value'''
    return number/2
