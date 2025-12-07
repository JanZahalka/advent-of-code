use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
    path::{Path, PathBuf},
};

pub fn run(input_dir: &str) -> Result<(), Box<dyn Error>> {
    let input_path = PathBuf::from(input_dir).join("input01.txt");

    puzzle(&input_path, 1)?;
    puzzle(&input_path, 2)?;

    Ok(())
}

fn puzzle(input_path: &Path, puzzle_no: i32) -> Result<(), Box<dyn Error>> {
    let file = File::open(input_path)?;
    let reader = BufReader::new(file);

    print!("Puzzle {} - password: ", puzzle_no);

    let mut password = 0;
    let mut position = 50;

    for (i, line) in reader.lines().enumerate() {
        let line = line?;
        let direction = line
            .chars()
            .next()
            .ok_or(format!("Cannot parse direction from line {} of input.", i))?;

        let dir_multiplier = match direction {
            'R' => 1,
            'L' => -1,
            _ => {
                return Err(format!(
                    "Invalid direction multiplier '{}' on input line {}",
                    direction, i
                )
                .into());
            }
        };

        let n_steps_str: String = line.chars().skip(1).collect();
        let n_steps: i32 = n_steps_str.parse()?;

        match puzzle_no {
            1 => {
                position += dir_multiplier * n_steps;
                position = position.rem_euclid(100);

                if position == 0 {
                    password += 1;
                }
            }
            2 => {
                let huge_constant = 1000000;
                let old_position = position + huge_constant;
                let mut new_position = old_position + dir_multiplier * n_steps;

                let n_zero_ticked = (new_position / 100 - old_position / 100).abs();

                new_position = (new_position - huge_constant).rem_euclid(100);

                position = new_position;
                password += n_zero_ticked
            }
            _ => return Err(format!("Invalid puzzle number: '{}'.", puzzle_no).into()),
        };
    }

    println!("{}", password);
    Ok(())
}
