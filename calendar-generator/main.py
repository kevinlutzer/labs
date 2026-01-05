import calendar
import matplotlib.pyplot as plt

YEAR = 2026
NAME = "kevin"
OUTPUT_FILE = f"{NAME}_calendar_{YEAR}.png"

def get_days_in_month(year, month):
  """
  Returns the number of days in a specific month and year.

  :param year: The year (e.g., 2024).
  :param month: The month (1 for January, 12 for December).
  :return: The number of days as an integer.
  """
  # monthrange returns (weekday_of_first_day, num_days_in_month)
  num_days = calendar.monthrange(year, month)[1]
  return num_days


def get_day_name(year, month, day):
    """
    Returns the name of the day for a specific date.

    :param year: The year (e.g., 2024).
    :param month: The month (1 for January, 12 for December).
    :param day: The day of the month.
    :return: The name of the day (e.g., "Monday").
    """
    day_index = calendar.weekday(year, month, day)
    return calendar.day_name[day_index]

def is_weekend_day(year, month, day):
    """
    Checks if a specific date falls on a weekend (Saturday or Sunday).

    :param year: The year (e.g., 2024).
    :param month: The month (1 for January, 12 for December).
    :param day: The day of the month.
    :return: True if the date is a weekend, False otherwise.
    """
    day_index = calendar.weekday(year, month, day)
    return day_index in (5, 6)  # Saturday=5, Sunday=6

def main():
    """
    Actually builds the calendar
    """

    months = list(calendar.month_name)[1:]

    _, ax = plt.subplots(figsize=(36, 24))
    ax.set_axis_off()

    # Title
    ax.text(
        0.5, 0.97,
        f"{NAME.upper()}'S {YEAR} CALENDAR",
        ha="center", va="top",
        fontsize=48, fontweight="bold", color="#1f77b4",
        transform=ax.transAxes
    )

    # Table positioning
    top = 0.92
    left = 0.05
    cell_width = 0.9 / 30
    cell_height = 0.9 / len(months)

    # Draw grid
    for row, month in enumerate(months):

        num_days = get_days_in_month(YEAR, row + 1)
        y = top - (row + 1) * cell_height

        # Month label
        ax.text(
            left - 0.01, y + cell_height / 2,
            month[:3].upper(),
            ha="right", va="center",
            fontsize=22, fontweight="bold",
            color="#1f77b4",
            transform=ax.transAxes
        )

        for col, day in enumerate(list(range(1, num_days + 1))):
            x = left + (col) * cell_width

            # check if weekend
            is_weekend = is_weekend_day(YEAR, row + 1, day)

            # Alternate shading for readability
            fill = "#eef4f8" if is_weekend else "white"

            rect = plt.Rectangle(
                (x, y),
                cell_width,
                cell_height,
                fill=True,
                color=fill,
                ec="#b0c4de",
                lw=0.5,
                transform=ax.transAxes
            )
            ax.add_patch(rect)

            # Day name
            ax.text(
                x + 0.01 * cell_width,
                y + cell_height - 0.0025,
                str(get_day_name(YEAR, row + 1, day)[:3]).upper(),
                ha="left", va="top",
                fontsize=11,
                color="#4a6fa5",
                transform=ax.transAxes
            )

            # Day name
            ax.text(
                x + cell_width - 0.01 * cell_width,
                y + cell_height - 0.0025,
                str(day),
                ha="right", va="top",
                fontweight="bold",
                fontsize=11,
                color="#4a6fa5",
                transform=ax.transAxes
            )

    # Save image
    plt.savefig(OUTPUT_FILE, dpi=1000, bbox_inches="tight")
    plt.close()

    print(f"Calendar saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()