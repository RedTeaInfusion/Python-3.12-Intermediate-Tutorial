import pygame
import configparser
from button import Button
from enemy import Enemy
from tower import Tower
from message_box import MessageBox
from constants import (WIDTH, HEIGHT, GRID, CELL_SIZE, 
                       WHITE, BLACK, GRAY, BROWN, DARK_GREEN, DARK_RED)


def get_tower(grid_x, grid_y, type_towers, index):
    return Tower(
        x=grid_x * CELL_SIZE, 
        y=grid_y * CELL_SIZE, 
        level=type_towers[index][0],
        damage=type_towers[index][1], 
        fire_range=type_towers[index][2], 
        fire_rate=type_towers[index][3], 
        cost=type_towers[index][4], 
        upgrade_cost=type_towers[index][5], 
        image_path=type_towers[index][6]
    )

def draw_tower_stats(surface, selected_tower, level, damage, fire_range, fire_rate, cost, upgrade_cost, max_tower_level):
    font = pygame.font.SysFont('Arial', 20)
    stats_text = [
        f'Damge: {damage}',
        f"Range: {fire_range}",
        f"Fire rate: {fire_rate}",
        f'Level: {level}',
        f'Sell cost: {round(int(cost) * 0.9)}' if isinstance(selected_tower, Tower) else f'Cost: {cost}',
        f'Upgrade cost: {int(upgrade_cost)}' if int(level) < max_tower_level else '',
    ]
    for i, line in enumerate(stats_text):
        text = font.render(line, True, BLACK)
        surface.blit(text, (WIDTH - 350, 460 + i * 20))

def draw_grid_elements(screen, towers, enemies, projectiles):
    # Draw grid cells
    screen.fill(WHITE)
    for y, row in enumerate(GRID):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell in [0, 4]:
                pygame.draw.rect(screen, DARK_GREEN, rect)
            elif cell in [1, 2, 3]:
                pygame.draw.rect(screen, BROWN, rect)
    # Draw grid lines
    for x in range(len(GRID[0]) + 1):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, len(GRID) * CELL_SIZE), 1)
    for y in range(len(GRID) + 1):
        pygame.draw.line(screen, BLACK, (0, y * CELL_SIZE), (len(GRID[0]) * CELL_SIZE, y * CELL_SIZE), 1)
    # Draw towers, enemies, projectiles
    towers.draw(screen)
    enemies.draw(screen)
    projectiles.draw(screen)
    # Draw the healt bar for any enemy
    for enemy in enemies:
        enemy.draw_health_bar(screen)

def read_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    result = []
    for section in config.sections():
        section_values = []
        for key, value in config.items(section):
            try:
                section_values.append(int(value))
            except ValueError:
                section_values.append(value)
        result.append(section_values)

    return result

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 30)

    towers = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    
    game_running = True
    level_running = False
    selected_tower = None
    current_level = 1

    # Enemies
    total_enemies_spawned = 0
    spawn_counter = 0

    # Game
    score = 0
    lives = 20
    money = 300

    # Tower costs
    type_towers = read_config_file('towers.ini')
    levels = read_config_file('levels.ini')
    max_tower_level = 5

    # Create the buttons with the images
    button_tower1 = Button(WIDTH * 0.06, HEIGHT * 0.75, 32, 32, '', '', '', image_path="./images/tower1.png")
    button_tower2 = Button(WIDTH * 0.12, HEIGHT * 0.75, 32, 32, '', '', '', image_path="./images/tower2.png")
    button_tower3 = Button(WIDTH * 0.18, HEIGHT * 0.75, 32, 32, '', '', '', image_path="./images/tower3.png")

    # Buttons
    button_start = Button(WIDTH * 0.05, HEIGHT * 0.85, 190, 50, BROWN, "Start Level 1", WHITE, '')
    button_sell = Button(WIDTH - 180, HEIGHT * 0.73, 170, 40, DARK_RED, "Sell Tower", WHITE, '')
    button_upgrade = Button(WIDTH - 180, HEIGHT * 0.8, 170, 40, DARK_GREEN, "Upgrade", WHITE, '')

    # Main Loop
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.is_clicked(event) and not level_running:
                    level_running = True
                    total_enemies_spawned = 0
                    enemies.empty()
                    spawn_fire_rate, enemy_healt, speed, value, enemy_image, num_enemies = levels[current_level-1]
                elif button_tower1.is_clicked(event):
                    selected_tower = "Tower 1"
                elif button_tower2.is_clicked(event):
                    selected_tower = "Tower 2"
                elif button_tower3.is_clicked(event):
                    selected_tower = "Tower 3"
                elif button_sell.is_clicked(event) and selected_tower and isinstance(selected_tower, Tower):
                    money += int(round(selected_tower.cost * 0.90))
                    GRID[selected_tower.rect.y // CELL_SIZE][selected_tower.rect.x // CELL_SIZE] = 0
                    towers.remove(selected_tower)
                    selected_tower = None
                elif button_upgrade.is_clicked(event) and selected_tower:
                    if money >= selected_tower.upgrade_cost and selected_tower.level < max_tower_level and isinstance(selected_tower, Tower):
                        money -= selected_tower.upgrade_cost
                        selected_tower.level += 1
                        selected_tower.damage = int(round(selected_tower.damage * (100 + selected_tower.level*3) / 100))
                        selected_tower.fire_range = int(round(selected_tower.fire_range * (100 + selected_tower.level*3) / 100))
                        selected_tower.fire_rate = int(round(selected_tower.fire_rate * (100 + selected_tower.level*3) / 100))
                        selected_tower.upgrade_cost = int(round(selected_tower.upgrade_cost * (100 + selected_tower.level*3) / 100))
                        selected_tower.cost = int(round(selected_tower.cost * (100 + selected_tower.level*3) / 100))
                elif event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if y < CELL_SIZE * len(GRID):
                        grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
                        try:
                            if GRID[grid_y][grid_x] == 0:
                                if selected_tower == "Tower 1" and money >= type_towers[0][4]:
                                    towers.add(get_tower(grid_x, grid_y, type_towers, 0))
                                    money -= type_towers[0][4]
                                    GRID[grid_y][grid_x] = 4
                                elif selected_tower == "Tower 2" and money >= type_towers[1][4]:
                                    towers.add(get_tower(grid_x, grid_y, type_towers, 1))
                                    money -= type_towers[1][4]
                                    GRID[grid_y][grid_x] = 4
                                elif selected_tower == "Tower 3" and money >= type_towers[2][4]:
                                    towers.add(get_tower(grid_x, grid_y, type_towers, 2))
                                    money -= type_towers[2][4]
                                    GRID[grid_y][grid_x] = 4
                        except IndexError as e:
                            print(f'Index error: {e}')
                        # Check for tower clicks on the grid
                        for tower in towers:
                            if tower.rect.collidepoint(event.pos):
                                selected_tower = tower
                                break
                        else:
                            selected_tower = None
                    else:
                        selected_tower = None
        if level_running:
            for tower in towers:
                projectile = tower.update(enemies)
                if projectile:
                    projectiles.add(projectile)
            for enemy in enemies:
                if enemy.progress_path(enemy.find_path(GRID)):
                    lives -= 1
                    enemy.kill()
                if enemy.health <= 0:
                    enemy.kill()
                    score += 10
                    money += value
            # Inflict damage to an enemy
            projectiles.update()
            if total_enemies_spawned < num_enemies:
                spawn_counter += 1
                if spawn_counter >= spawn_fire_rate:
                    spawn_counter = 0
                    enemies.add(Enemy(enemy_healt, speed, value, enemy_image))
                    total_enemies_spawned += 1
        # Draw Grid            
        draw_grid_elements(screen, towers, enemies, projectiles)
        # Draw the button to go to the next level if the current it's finished
        if not level_running:
            button_start.text = f"Start Level {current_level}"
            button_start.draw(screen)
        # Draw the Score, Lives and Money
        score_text = font.render(f"Score: {score}", True, BLACK)
        money_text = font.render(f"Money: ${money}", True, BLACK)
        lives_text = font.render(f"Lives: {lives}", True, BLACK)
        screen.blit(score_text, (10, 590))
        screen.blit(money_text, (WIDTH // 2 - 90, 590))
        screen.blit(lives_text, (WIDTH - 130, 590))

        # Draw the buttons to pick the towers
        button_tower1.draw(screen)
        button_tower2.draw(screen)
        button_tower3.draw(screen)
        # Select a tower on the grid
        if selected_tower and isinstance(selected_tower, Tower):
            # Draw the grey rectangle
            pygame.draw.rect(screen, GRAY, (WIDTH - 350, 455, 350, 130))
            # Draw the stats of the selected tower
            draw_tower_stats(
                screen, 
                selected_tower,
                selected_tower.level,
                selected_tower.damage, 
                selected_tower.fire_range, 
                selected_tower.fire_rate,
                selected_tower.cost, 
                selected_tower.upgrade_cost,
                max_tower_level
            )
            # Draw upgrade button
            if selected_tower.level < max_tower_level:
                button_upgrade.draw(screen)
            # Draw sell button
            button_sell.draw(screen)
            # Draw range to tower
            pygame.draw.circle(screen, GRAY, selected_tower.rect.center, selected_tower.fire_range, 1)
        
        # Select a tower on the menu
        for i in range(len(type_towers)):
            if selected_tower == f'Tower {i+1}':
                # Draw the grey rectangle
                pygame.draw.rect(screen, GRAY, (WIDTH - 350, 455, 200, 130))
                # Draw the stats of the selected tower
                draw_tower_stats(
                    screen, 
                    selected_tower,
                    level=type_towers[i][0],
                    damage=type_towers[i][1], 
                    fire_range=type_towers[i][2], 
                    fire_rate=type_towers[i][3], 
                    cost=type_towers[i][4], 
                    upgrade_cost=type_towers[i][5], 
                    max_tower_level=max_tower_level
                )

        # Verify if the level is complete.
        if level_running:
            if(total_enemies_spawned == num_enemies and len(enemies) == 0):
                level_running = False
                current_level += 1

        # Verify if the game is complete
        if current_level > len(levels):
            msg_box = MessageBox(screen, "You Win", f"Final score: {score * lives * money}")
            if msg_box.show():
                game_running = False

        # Verify if you lost
        if lives <= 0:
            msg_box = MessageBox(screen, "You Lose", f"Final score: {score * money}")
            if msg_box.show():
                game_running = False

        # Refreshes the display to show updates
        pygame.display.flip()
        # Limits the frame rate to 60 FPS
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
