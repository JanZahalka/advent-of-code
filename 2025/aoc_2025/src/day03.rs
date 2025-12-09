use std::{
    error::Error,
    fs::File,
    io::{self, BufRead, BufReader, Write},
    path::{Path, PathBuf},
};

pub fn run(input_dir: &str) -> Result<(), Box<dyn Error>> {
    let input_path = PathBuf::from(input_dir).join("input03.txt");

    puzzle(&input_path, 1)?;
    puzzle(&input_path, 2)?;

    Ok(())
}

fn puzzle(input_path: &Path, puzzle_no: i32) -> Result<(), Box<dyn Error>> {
    print!("Puzzle {} - joltage sum: ", puzzle_no);
    io::stdout().flush()?;

    let file = File::open(input_path)?;
    let reader = BufReader::new(file);

    let joltage_len = match puzzle_no {
        1 => 2,
        2 => 12,
        _ => return Err(format!("Invalid puzzle no. {}", puzzle_no).into()),
    };

    let mut joltage_total: i64 = 0;

    for line in reader.lines() {
        let line = line?;
        let line_trimmed = line.trim_end();

        let joltage_str = recursive_joltage(line_trimmed, joltage_len);
        joltage_total += joltage_str.parse::<i64>().unwrap();
    }

    println!("{}", joltage_total);
    Ok(())
}

fn recursive_joltage(battery_bank: &str, joltage_pos: usize) -> String {
    if joltage_pos == 0 {
        return "".to_string();
    }

    let mut max = 0;
    let mut i_max: usize = 0;

    for (i, c) in battery_bank
        .chars()
        .take(battery_bank.len() - joltage_pos + 1)
        .enumerate()
    {
        let digit = c.to_digit(10).unwrap() as i32;

        if digit > max {
            max = digit;
            i_max = i;
        }
    }

    let joltage_lower = recursive_joltage(&battery_bank[i_max + 1..], joltage_pos - 1);
    let joltage = format!("{}{}", max, joltage_lower);

    joltage
}
