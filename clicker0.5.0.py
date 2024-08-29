import time
import keyboard
import os
import keyboard.mouse

LC_K = 'left'
RC_K = 'right'
ONOFF_K = 'capslock'
CLR_K = ' + c'
ABT_K = ' + a'
EXIT_K = ' + x'
HELP_K = ' + h'
SPD_K = ' + s'
SPD_V = 0.1

INTRO = ("      #_Auto_Clicker_# \n\n$ Clicker ON/OFF [ Capslock ] \n$ Help [ ESC + H ] \n$ Set Speed [ ESC + S ] \n$ About [ ESC + A ] \n$ Exit [ ESC + X ] \nTIP: use [ ESC + C] to clear screen !")
ABOUT = ("\n\n Developer: Tension_IDK [Jihad]\n Coded in Python.\n Converted to EXE using: AUTO_PYTO_EXE.\n")
HELP_1 = ("         #_HELP_# \n  >> How To Use << \n1. Toggle Clicker on. \n2. Left click or Right Click To Start Auto Clicker. \n3. Click the opposite Button To stop Clicker or use capslock.")
HELP_2 = ("@@ To stop Left Click, Do right click @@ \n@@ To Stop Right Click, Do Left Click @@ \n>>> Use [ CAPSLOCK ] To stop and toggle clicker off <<<")

while True:
    os.system('CLS')
    print(INTRO)
    
    while True:
        ON = keyboard.is_pressed(ONOFF_K)
        EXIT = keyboard.is_pressed(EXIT_K)
        SPD = keyboard.is_pressed(SPD_K)
        ABT = keyboard.is_pressed(ABT_K)
        CLR = keyboard.is_pressed(CLR_K)
        HELP1 = keyboard.is_pressed(HELP_K)

        while ON:
            OFF = keyboard.is_pressed(ONOFF_K)
            print('Clicker ON \n See Help [ ESC + H ]')
            time.sleep(0.3)

            while True:
                LC = keyboard.mouse.is_pressed('left')
                RC = keyboard.mouse.is_pressed('right')
                SPD = keyboard.is_pressed(SPD_K)
                CLR = keyboard.is_pressed(CLR_K)
                HELP2 = keyboard.is_pressed(HELP_K)
                OFF = keyboard.is_pressed(ONOFF_K)
                EXIT = keyboard.is_pressed(EXIT_K)

                while LC:
                    keyboard.mouse.click(LC_K)
                    time.sleep(SPD_V)
                    LCS = keyboard.mouse.is_pressed(RC_K)
                    EXIT = keyboard.is_pressed(EXIT_K)
                    OFF = keyboard.is_pressed(ONOFF_K)

                    if LCS:
                        keyboard.mouse.release('left')
                        print('LEFT Click Stoped')
                        time.sleep(0.3)
                        break

                    elif OFF:
                        keyboard.mouse.release('left')
                        print('Clicker OFF')
                        time.sleep(0.3)
                        break

                    elif EXIT:
                        exit()

                while RC:
                    keyboard.mouse.click(RC_K)
                    time.sleep(SPD_V)
                    RCS = keyboard.mouse.is_pressed(LC_K)
                    EXIT = keyboard.is_pressed(EXIT_K)
                    OFF = keyboard.is_pressed(ONOFF_K)

                    if RCS:
                        keyboard.mouse.release(RC_K)
                        print('RIGHT Click Stoped')
                        time.sleep(0.3)
                        break

                    elif OFF:
                        keyboard.mouse.release('left')
                        print('Clicker OFF')
                        time.sleep(0.3)
                        break

                    elif EXIT:
                        exit()

                if HELP2:
                    print(HELP_2)
                    time.sleep(0.3)

                elif OFF:
                    print('Clicker OFF')
                    break

                elif CLR:
                    os.system('CLS')
                    print(INTRO)
                    time.sleep(0.3)

                elif SPD:
                    time.sleep(0.3)
                    SPD_V = input("Enter the Speed(sec):")

                    try:
                        SPD_V = float(SPD_V)
                        print("Speed set to:", SPD_V, " sec")

                    except ValueError:
                        if not type(SPD_V) is float or int:
                            SPD_V = 0.1
                            print("Please Enter Integer Data!!\nTry again.")

                elif EXIT:
                    exit()

            if OFF:
                time.sleep(0.3)
                break

        if HELP1:
            print(HELP_1)
            time.sleep(0.3)

        elif SPD:
            time.sleep(0.3)
            SPD_V = input("Enter the Speed(sec):")

            try:
                SPD_V = float(SPD_V)
                print("Speed set to:", SPD_V, " sec")

            except ValueError:
                if not type(SPD_V) is float or int:
                    SPD_V = 0.1
                    print("Please Enter Integer Data!!\nTry again.")

        elif CLR:
            os.system('CLS')
            print(INTRO)
            time.sleep(0.3)

        elif ABT:
            print(ABOUT)
            time.sleep(0.3)

        elif EXIT:
            exit()
        