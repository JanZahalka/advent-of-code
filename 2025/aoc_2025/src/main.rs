mod day01;

fn main() {
    let input_dir = "src/inputs";

    println!("+++ ADVENT OF CODE 2025 +++");

    println!("=== Day 1 ===");
    day01::run(input_dir).unwrap_or_else(|e| eprintln!("Error: {}", e));
}
