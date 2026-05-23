def greet(fx):
    def mfx():
        print ("Hello Omkar")
        fx()
        print ("Thank you for running this function")
    return mfx

@greet
def fx():
    print("This line is printed by Main function")

fx()
