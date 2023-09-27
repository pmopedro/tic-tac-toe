import asyncio

from game import TicTacToe
from game import window_size, screen
import pygame 

async def main():
    global g
    g = TicTacToe(window_size[0])
    screen.fill(g.background_color)
    g.draw_table()

    while g.running:
        g.message()
        for g.event in pygame.event.get():
            if g.event.type == pygame.QUIT:
                g.running = False

            if g.event.type == pygame.MOUSEBUTTONDOWN:
                if g.taking_move:
                    g.move(g.event.pos)

        pygame.display.flip()
        g.FPS.tick(60)
        
        
        await asyncio.sleep(0)  # Very important, and keep it 0

asyncio.run(main())
