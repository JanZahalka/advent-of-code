use std::{
    error::Error,
    fs::File,
    io::{self, BufRead, BufReader, Write},
    path::{Path, PathBuf},
};

pub fn run(input_dir: &str) -> Result<(), Box<dyn Error>> {
    let input_path = PathBuf::from(input_dir).join("input03.txt");

    puzzle(&input_path, 1)?;

    Ok(())
}

fn puzzle(input_path: &Path, puzzle_no: i32) -> Result<(), Box<dyn Error>> {
    print!("Puzzle {} - joltage sum: ", puzzle_no);
    io::stdout().flush()?;

    let file = File::open(input_path)?;
    let reader = BufReader::new(file);

    let mut joltage_total = 0;

    for line in reader.lines() {
        let line = line?;
        let line_trimmed = line.trim_end();

        let mut max_first = -1;
        let mut i_max_first = 0;
        let mut max_second = -1;

        for (i, c) in line_trimmed
            .chars()
            .enumerate()
            .take(line_trimmed.len() - 1)
        {
            let digit = c.to_digit(10).unwrap() as i32;

            if digit > max_first {
                max_first = digit;
                i_max_first = i;
            }
        }

        for c in line_trimmed.chars().skip(i_max_first + 1) {
            let digit = c.to_digit(10).unwrap() as i32;

            if digit > max_second {
                max_second = digit;
            }
        }

        let joltage = max_first * 10 + max_second;
        joltage_total += joltage;
    }

    println!("{}", joltage_total);
    Ok(())
}
