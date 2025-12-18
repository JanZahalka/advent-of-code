use std::{
    cmp::max,
    collections::HashSet,
    error::Error,
    fs::File,
    io::{self, BufRead, BufReader, Write},
    path::{Path, PathBuf},
};

pub fn run(input_dir: &str) -> Result<(), Box<dyn Error>> {
    let input_path = PathBuf::from(input_dir).join("input05.txt");

    puzzle1(&input_path)?;
    puzzle2(&input_path)?;

    Ok(())
}
fn puzzle1(input_path: &Path) -> Result<(), Box<dyn Error>> {
    print!("Puzzle 1 - no. of fresh ingredients: ");
    io::stdout().flush()?;

    let file = File::open(input_path)?;
    let reader = BufReader::new(file);
    let mut parsing_ranges = true;

    let mut ranges: Vec<Vec<usize>> = Vec::new();
    let mut ingredients: Vec<usize> = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let line = line.trim_end();

        if line.is_empty() {
            parsing_ranges = false;
            continue;
        }

        if parsing_ranges {
            let range: Vec<usize> = line
                .split("-")
                .map(|edge| edge.parse::<usize>().unwrap())
                .collect();
            ranges.push(range);
        } else {
            let ingredient = line.parse::<usize>().unwrap();
            ingredients.push(ingredient);
        }
    }

    let mut n_fresh = 0;

    for ingredient in ingredients {
        for range in &ranges {
            if ingredient >= range[0] && ingredient <= range[1] {
                n_fresh += 1;
                break;
            }
        }
    }

    println!("{}", n_fresh);

    Ok(())
}

fn puzzle2(input_path: &Path) -> Result<(), Box<dyn Error>> {
    print!("Puzzle 2 - no. of fresh ingredient IDs: ");
    io::stdout().flush()?;

    let file = File::open(input_path)?;
    let reader = BufReader::new(file);

    let mut ranges: Vec<Vec<usize>> = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let line = line.trim_end();

        if line.is_empty() {
            break;
        }
        let range: Vec<usize> = line
            .split("-")
            .map(|edge| edge.parse::<usize>().unwrap())
            .collect();
        ranges.push(range);
    }

    let mut changes_happened;

    loop {
        ranges.sort_by_key(|inner_vec| inner_vec[0]);

        // Merge overlapping intervals (with left neighbor), updating BOTH entries
        for i in 1..ranges.len() {
            if ranges[i][0] <= ranges[i - 1][1] {
                let new_right = max(ranges[i - 1][1], ranges[i][1]);

                ranges[i][0] = ranges[i - 1][0];
                ranges[i - 1][1] = new_right;
                ranges[i][1] = new_right;
            }
        }

        // Remove duplicates
        let old_ranges_len = ranges.len();
        let mut seen = HashSet::new();
        ranges.retain(|range| seen.insert(range.clone()));

        changes_happened = ranges.len() != old_ranges_len;

        if !changes_happened {
            break;
        }
    }

    let mut n_fresh_ids = 0;
    for range in ranges {
        n_fresh_ids += range[1] - range[0] + 1;
    }

    println!("{}", n_fresh_ids);

    Ok(())
}
