use std::collections::HashMap;
use std::fs;
use std::io;
use std::path::Path;

#[derive(Debug, Default, PartialEq, Eq)]
pub struct LogCounts {
    pub info: usize,
    pub warn: usize,
    pub error: usize,
}

pub fn count_log_levels(content: &str) -> LogCounts {
    let mut counts = LogCounts::default();

    for line in content.lines() {
        if line.contains("INFO") {
            counts.info += 1;
        }
        if line.contains("WARN") {
            counts.warn += 1;
        }
        if line.contains("ERROR") {
            counts.error += 1;
        }
    }

    counts
}

pub fn count_log_file<P: AsRef<Path>>(path: P) -> io::Result<LogCounts> {
    let content = fs::read_to_string(path)?;
    Ok(count_log_levels(&content))
}

pub fn format_counts(counts: &LogCounts) -> HashMap<&'static str, usize> {
    let mut map = HashMap::new();
    map.insert("INFO", counts.info);
    map.insert("WARN", counts.warn);
    map.insert("ERROR", counts.error);
    map
}
