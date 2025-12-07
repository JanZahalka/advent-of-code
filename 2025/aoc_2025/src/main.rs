use clap::Parser;
use std::error::Error;

mod day01;
mod day02;
mod day03;

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    #[arg(short, long)]
    day: Option<usize>,
}

type DayRunner = fn(&str) -> Result<(), Box<dyn Error>>;

const DAY_FNS: &[DayRunner] = &[day01::run, day02::run, day03::run];

fn main() {
    let args = Args::parse();
    let input_dir = "src/inputs";

    println!("+++ ADVENT OF CODE 2025 +++");

    match args.day {
        Some(day) => run_day(day, input_dir),
        None => run_all_days(input_dir),
    }
    .unwrap_or_else(|e| eprintln!("Error: {}", e));
}

fn run_day(day: usize, input_dir: &str) -> Result<(), Box<dyn Error>> {
    println!("=== Day {} ===", day);

    if day == 0 || day > DAY_FNS.len() {
        return Err(format!("Day {} not implemented.", day).into());
    }

    DAY_FNS[day - 1](input_dir)
}

fn run_all_days(input_dir: &str) -> Result<(), Box<dyn Error>> {
    for day in 1..=DAY_FNS.len() {
        run_day(day, input_dir)?;
    }

    Ok(())
}
