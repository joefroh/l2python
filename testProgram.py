from LearningClasses.testClass import HelloWorldPrinter

def main():
    test = HelloWorldPrinter()
    test.HelloWorld()

    test2 = HelloWorldPrinter()
    test2.testString = "foo"
    test2.HelloWorld()
    test.HelloWorld()

if __name__ == '__main__':
    main()