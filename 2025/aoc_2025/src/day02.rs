use std::{
    error::Error,
    fs,
    io::{self, Write},
    path::{Path, PathBuf},
};

pub fn run(input_dir: &str) -> Result<(), Box<dyn Error>> {
    let input_path = PathBuf::from(input_dir).join("input02.txt");

    puzzle(&input_path, 1)?;
    puzzle(&input_path, 2)?;

    Ok(())
}

fn puzzle(input_path: &Path, puzzle_no: i32) -> Result<(), Box<dyn Error>> {
    print!("Puzzle {} - invalid ID sum: ", puzzle_no);
    io::stdout().flush()?;

    let content = fs::read_to_string(input_path)?;
    let id_ranges: Vec<&str> = content.trim_end().split(",").collect();
    let checking_fn = match puzzle_no {
        1 => invalid_puzzle1,
        2 => invalid_puzzle2,
        _ => return Err(format!("Invalid puzzle no. {}", puzzle_no).into()),
    };

    let mut invalid_id_sum: i64 = 0;

    for id_range in id_ranges {
        let edges: Vec<i64> = id_range.split("-").map(|e| e.parse().unwrap()).collect();
        let min = edges[0];
        let max = edges[1];

        for id in min..=max {
            if checking_fn(&(id.to_string())) {
                invalid_id_sum += id;
            }
        }
    }

    println!("{}", invalid_id_sum);

    Ok(())
}

fn invalid_puzzle1(s: &str) -> bool {
    if s.len().is_multiple_of(2) {
        return false;
    }

    let (first_half, second_half) = s.split_at(s.len() / 2);
    first_half == second_half
}

fn invalid_puzzle2(s: &str) -> bool {
    if s.len() < 2 {
        return false;
    }

    let possible_pattern_lengths = pattern_lengths(s.len());

    for p_len in possible_pattern_lengths {
        let chunks: Vec<String> = s
            .chars()
            .collect::<Vec<char>>()
            .chunks(p_len)
            .map(|chunk| chunk.iter().collect())
            .collect();

        let all_equal = chunks.iter().all(|chunk| chunk == &chunks[0]);

        if all_equal {
            return true;
        }
    }

    false
}

fn pattern_lengths(n: usize) -> Vec<usize> {
    let mut divisors = Vec::new();
    let sqrt_n = (n as f64).sqrt() as usize;

    for i in 1..=sqrt_n {
        if n.is_multiple_of(i) {
            divisors.push(i);

            if i != n / i && n / i != n {
                divisors.push(n / i);
            }
        }
    }

    divisors.sort();
    divisors
}
