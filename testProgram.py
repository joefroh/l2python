from os import sys

sys.path.append("./LearningClasses")

from testClass import HelloWorldPrinter

def main():
    test = HelloWorldPrinter()
    test.HelloWorld()

    test2 = HelloWorldPrinter()
    test2.testString = "foo"
    test2.HelloWorld()
    test.HelloWorld()

if __name__ == '__main__': # This is the thing that defines main as main. Basically if you execute this file, it parses through all of it, then runs main.
    main()