nenodots = input("Vai Jums ir kāds nenodots izdevums?(j/n):")
if nenodots == 'j':
    print("Jūs nedrīkstat neko izņemt.")
elif nenodots == 'n':
    pieprasits=input("Vai šī publikācija ir pieprasīta?(j/n)")
    if pieprasits == 'j':
        print("Izsniedz uz 2 dienām.")
    elif pieprasits == 'n':
        zurnals=input("Vai publikācija ir žurnāls?")
        if zurnals == 'j':
            print("Izsniedz uz 7 dienām")
        elif zurnals == 'n':
            students = input("Vai Jūs esat students?(j/n)")
            if students == 'j':
                print("Izsniedz uz 14 dienām.")
            elif students == 'n':
                print("Izsniedz uz 28 dienām.")

