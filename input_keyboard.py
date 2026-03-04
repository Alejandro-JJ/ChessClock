import pygame

class KeyboardInput:

    def poll(self):
        events = []
        for event in pygame.event.get():
            # If user closes window
            if event.type == pygame.QUIT:
                events.append("QUIT")

            # If the user has pushed a button
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:     # switch to P1
                    events.append("P1")

                elif event.key == pygame.K_l:   # switch to P2
                    events.append("P2")

                elif event.key == pygame.K_x:   # quit
                    events.append("QUIT")

                elif event.key == pygame.K_UP:  # rotate through selection in menu
                    events.append("ROTATE")

                elif event.key == pygame.K_RETURN: # make selection in menu / exit gave_over
                    events.append("ENTER")


        return events
