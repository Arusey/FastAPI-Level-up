def ask_for_passcode(func):
    def inner():
        print("what is the passcode")
        passcode = input()

        if passcode != '1234':
            print('wrong passcode')
        else:
            print('access granted')
            func()
    return inner

@ask_for_passcode
def start():
    print("server has been started")
@ask_for_passcode
def end():
    print("server has been stopped")
    

start()
end()