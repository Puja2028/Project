use rust_log_counter::{count_log_file, count_log_levels};
use std::io::Write;
use tempfile::NamedTempFile;

#[test]
fn counts_mixed_levels() {
    let input = "INFO boot\nWARN slow\nERROR fail\nINFO ok\n";
    let counts = count_log_levels(input);
    assert_eq!(counts.info, 2);
    assert_eq!(counts.warn, 1);
    assert_eq!(counts.error, 1);
}

#[test]
fn empty_file_has_zero_counts() {
    let counts = count_log_levels("");
    assert_eq!(counts.info, 0);
    assert_eq!(counts.warn, 0);
    assert_eq!(counts.error, 0);
}

#[test]
fn reads_from_file() {
    let mut file = NamedTempFile::new().unwrap();
    writeln!(file, "INFO one").unwrap();
    writeln!(file, "ERROR two").unwrap();
    let counts = count_log_file(file.path()).unwrap();
    assert_eq!(counts.info, 1);
    assert_eq!(counts.error, 1);
}

#[test]
fn missing_file_returns_not_found() {
    let result = count_log_file("/nonexistent/path/sample.log");
    assert!(result.is_err());
    assert_eq!(result.unwrap_err().kind(), std::io::ErrorKind::NotFound);
}
