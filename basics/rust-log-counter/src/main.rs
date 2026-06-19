use rust_log_counter::{count_log_file, format_counts};
use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} <log-file-path>", args[0]);
        process::exit(1);
    }

    let path = &args[1];
    match count_log_file(path) {
        Ok(counts) => {
            let formatted = format_counts(&counts);
            println!("INFO: {}", formatted["INFO"]);
            println!("WARN: {}", formatted["WARN"]);
            println!("ERROR: {}", formatted["ERROR"]);
        }
        Err(err) if err.kind() == std::io::ErrorKind::NotFound => {
            eprintln!("Error: file not found: {path}");
            process::exit(2);
        }
        Err(err) => {
            eprintln!("Error reading file: {err}");
            process::exit(3);
        }
    }
}
