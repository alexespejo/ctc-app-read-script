import pandas as pd
import argparse
from rich.console import Console
from rich.table import Table
from rich.text import Text

# unnecessary params hidden
ROW_INDEX = 0
CSV_FILE = "applications.csv"
COLUMNS_TO_READ = [
    'Timestamp',
    'Email Address',
    'Name (first last)',
    'UCI Email\nex. "peteranteater1@uci.edu"',
    'Pronouns\n',
    'Year',
    'Expected Graduation Date',
    'Major',
    'Please attach a link (NOT attachment) to your resumé with the file titled "First Name Last Name - Resume" (ex: "Kaitlin Leung - Resume").',
    'Linkedin Link',
    'What experience are you looking for in Commit the Change?',
    'What are your areas of growth? Pick one of those areas and tell us how you improved on it recently.',
    ' What is something you are passionate about and why?',
    'Tell us about a time when you had to choose between 2 time commitments. Explain how you came to a conclusion for which work to prioritize.',
    # 'What experience do you hope to have this year with CTC?',
    # 'What did you learn from being in the club last year?',
    # 'What was your biggest contribution last year? What skill do you wish you had more of a chance to make use of or showcase?',
    # 'Tell us about a time when you had to choose between 2 time commitments. Explain how you came to a conclusion for which work to prioritize..1',
    # 'After your previous experience in CTC, what is one way that experience could be improved this year, either through your own initiative or through a change in the club?',
    'Which programming languages are you most comfortable coding in?',
    'Please select which best describes you.',
    'If not new to web dev, please describe the related work. If new to web dev or coding, briefly describe whatever technical/coding experience you have and the work you have completed.',
    '[Optional] Please include any links to your GitHub, personal website, portfolio, or related materials that showcase any previous work you have completed. ',
    # 'Reviewer 1 Name',
    # 'Reviewer 1 Rating',
    # 'Reviewer 1 Notes',
    # 'Reviewer 2 Name',
    # 'Reviewer 2 Rating',
    # 'Reviewer 2 Notes',
    # 'Final Decision',
    # 'Column 1',
    # 'Unnamed: 33',
]

console = Console()
df = pd.read_csv(CSV_FILE, usecols=COLUMNS_TO_READ)

def display_row(row_idx):
    row = df.iloc[row_idx]

    console.rule(f"[bold yellow]Application Row {row_idx}[/bold yellow]")

    idx = 0
    for col, val in row.items():
        col_text = Text(col, style="bold green")
        val_text = str(val) if pd.notna(val) else "(no response)"

        idx += 1

        if (idx > 8):
          console.print(col_text)   # print title
          console.print(val_text + "\n")  # print response below
        else:
          console.print(val_text)  # print response below

def _parse_args():
    parser = argparse.ArgumentParser(description="View application rows from CSV")
    parser.add_argument(
        "offset",
        nargs="?",
        type=int,
        default=0,
        help="Optional integer offset added to ROW_INDEX",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    target_index = ROW_INDEX + args.offset
    if target_index < 0 or target_index >= len(df):
        console.print(f"[red]Row index out of range:[/red] {target_index}. Valid range is 0 to {len(df)-1}.")
    else:
        display_row(target_index)
