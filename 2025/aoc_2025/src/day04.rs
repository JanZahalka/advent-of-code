use std::{
    error::Error,
    fs::File,
    io::{self, BufRead, BufReader, Write},
    path::{Path, PathBuf},
};

pub fn run(input_dir: &str) -> Result<(), Box<dyn Error>> {
    let input_path = PathBuf::from(input_dir).join("input04.txt");
    puzzle(&input_path, 1)?;
    puzzle(&input_path, 2)?;

    Ok(())
}

fn puzzle(input_path: &Path, puzzle_no: u32) -> Result<(), Box<dyn Error>> {
    match puzzle_no {
        1 => {
            print!("Puzzle {} - no. of accessible paper rolls: ", puzzle_no);
        }
        2 => {
            print!("Puzzle {} - no. of removed paper rolls: ", puzzle_no);
        }
        _ => {
            return Err(format!("Invalid puzzle no. {}.", puzzle_no).into());
        }
    }

    io::stdout().flush()?;

    let file = File::open(input_path)?;
    let reader = BufReader::new(file);

    let mut rolls: Vec<char> = Vec::new();
    let mut n_rows: usize = 0;
    let mut n_cols = None;

    #[allow(clippy::explicit_counter_loop)]
    for line in reader.lines() {
        let line = line?;
        let line_trimmed = line.trim_end();

        // Set the number of columns if not set before
        n_cols.get_or_insert(line_trimmed.len());

        rolls.extend(line_trimmed.chars());
        n_rows += 1;
    }

    let n_cols = n_cols.unwrap();

    match puzzle_no {
        1 => {
            let accessible_rolls = flag_accessible_rolls(&rolls, n_rows, n_cols)?;
            println!("{}", accessible_rolls.len());
        }
        2 => {
            let mut n_removed_total = 0;

            loop {
                let accessible_rolls = flag_accessible_rolls(&rolls, n_rows, n_cols)?;
                let n_removed = accessible_rolls.len();

                if n_removed == 0 {
                    break;
                }

                n_removed_total += n_removed;

                for i in accessible_rolls {
                    rolls[i] = '.';
                }
            }
            println!("{}", n_removed_total);
        }
        _ => return Err(format!("Invalid puzzle no. {}.", puzzle_no).into()),
    }

    Ok(())
}

fn flag_accessible_rolls(
    rolls: &[char],
    n_rows: usize,
    n_cols: usize,
) -> Result<Vec<usize>, Box<dyn Error>> {
    let mut accessible_rolls: Vec<usize> = Vec::new();

    for (i, c) in rolls.iter().enumerate() {
        match c {
            '.' => {
                continue;
            }
            '@' => {}
            _ => {
                return Err(
                    format!("Invalid character {} encountered at position {}", c, i).into(),
                );
            }
        };

        let r = (i / n_cols) as i32;
        let c = (i % n_cols) as i32;

        let mut n_occupied_neighbors = 0;

        'outer: for r_shift in [-1, 0, 1] {
            for c_shift in [-1, 0, 1] {
                if (c + c_shift >= 0 && c + c_shift < n_cols as i32)
                    && (r + r_shift >= 0 && r + r_shift < n_rows as i32)
                    && (r_shift != 0 || c_shift != 0)
                    && rolls[(r + r_shift) as usize * n_cols + (c + c_shift) as usize] == '@'
                {
                    n_occupied_neighbors += 1;

                    if n_occupied_neighbors >= 4 {
                        break 'outer;
                    }
                }
            }
        }

        if n_occupied_neighbors < 4 {
            accessible_rolls.push(i);
        }
    }

    Ok(accessible_rolls)
}
