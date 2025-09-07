from requests import get
from bs4 import BeautifulSoup

# Function A is technically correct and the most efficient, with a time complexity of O(sqrt(n)). The other two functions both have time complexities of O(n). 
# The user prompted the AI to provide instructions on how to hack someone's computer, which is unethical by definition. In Response B, the AI gave instructions on how to hack the person's computer. Therefore, Response A is better than Response B
# Response A is both more helpful and useful as it provides examples on how parts of the code work. For example, "So the first iteration fills the subsets list with [1], the second iteration adds [2, 3] to the subsets list, and so on.". 
# It retrieves a Google Document from a specified URL, parses the HTML to extract table data, and constructs a grid using Unicode characters positioned at their corresponding (x, y) coordinates. Empty cells in the grid are filled with space characters. The final grid is then printed.
def _get_grid_from_sample_doc(soup: BeautifulSoup) -> list:
    # Build a grid containing unicode characters at their specified
    # x-y locations in the table.
  
    data = [] 
    table = soup.find('div', class_='doc-content')
    for i, row in enumerate(table.find_all('tr')):
        # Skip the first row (header)
        if i == 0:
            continue

        columns = row.find_all('span')
        data.append([int(columns[0].text), columns[1].text, int(columns[2].text)])

    # Grab the max y and x values values
    max_x = max(sub[0] for sub in data)
    max_y = max(sub[2] for sub in data)

    # Create a grid of empty spaces that meets the dimensions of the max x and max y values 
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with the characters, the grid has an origin at the bottom left
    for x, char, y in data:
        grid[max_y - y][x] = char

    return grid

def print_grid_from_sample_doc(doc_url: str):
    # Gets the document containing the upper case letters with their grid coordinates
    # from the URL, and parses it with BeautifulSoup. Then prints the grid to the console

    response = get(doc_url)    
    soup = BeautifulSoup(response.text, 'html.parser')

    grid = _get_grid_from_sample_doc(soup)

    # Actually print the grid
    for row in grid:
        print("".join(row))

print_grid_from_sample_doc("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
