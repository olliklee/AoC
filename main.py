import os
import AoC_2015

PRE = 'AoC_'


def show_summary(folder):
    year = folder[4:]
    folders = sorted(os.listdir(folder))
    for file_name in folders:
        if file_name.startswith('Day'):
            # script_path = os.path.join(file_name, f'{file_name[:5]}.py')
            try:
                day, title, rating = file_name.split('-')
                print(f'AoC {year} - {day} {rating:5} {title}')
            except ValueError:
                print(' # Skipped: Name pattern error #')
    print()

if __name__ == '__main__':
    years = [2015,2016,2021,2022,2023,2024, 2025]
    for y in years:
        show_summary(f'{PRE}{y}')
    
