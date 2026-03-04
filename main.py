from States import AppState
from input_keyboard import KeyboardInput
from display_pygame import PygameDisplay
from TimeControls import TIME_CONTROLS
from clock import Clock
import time


def main():

    # The code starts in menu
    current_state = AppState.MENU
    menu_index = 0
    N_modes = len(TIME_CONTROLS)
    keyboard = KeyboardInput()
    display = PygameDisplay()
    running = True


    while running==True:
        events = keyboard.poll()
        # Once check for QUIT in MENU
        if "QUIT" in events and current_state==AppState.MENU:
            running = False

        #################
        # MENU STATE
        #################
        if current_state==AppState.MENU:

            for event in events:
                # Change game mode to be displayed / played
                if event == "ROTATE":
                    menu_index = (menu_index+1)%N_modes
                # Change machine state to playing
                elif event == "ENTER":
                    current_state = AppState.PLAYING
                    # Initialize a new clock and player
                    clock = Clock(TIME_CONTROLS[menu_index])
                    # clock.playing initializes as P1 always

            # Display the currently selected mode, only if we are still in menu
            if current_state==AppState.MENU:
                display.render_menu(TIME_CONTROLS[menu_index].label)


        #################
        # RUNNING STATE
        #################
        if current_state==AppState.PLAYING:

            times = clock.telltime()
            #display.render_game(times)
            display.render_game_BW(times)

            # Check for loss
            # not implemented

            for event in events:
                if event=="QUIT":
                    current_state = AppState.MENU
                #Both switches, if playing player presses
                if event=="P1" and clock.playing =="P1":
                    clock.switch()

                elif event=="P2" and clock.playing =="P2":
                    clock.switch()

        #################
        # GAME_OVER STATE
        #################
        # to be implemented



        # Limit loop speed
        time.sleep(0.05)


if __name__ == "__main__":
    main()

