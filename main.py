import lpro
import lpro_s

class Session:
    usr_state = "zeta"

def run():
    active = "s"
    while True:
        if active == "s":
            print("\nnot recording")
            lpro_s.change_username(Session.usr_state)
            lpro_s.main()
            Session.usr_state = lpro_s.raw_usr
            active = "l"
        else:
            print("\nrecording")
            lpro.change_username(Session.usr_state)
            lpro.main()
            Session.usr_state = lpro.raw_usr
            active = "s"

if __name__ == "__main__":
    run()