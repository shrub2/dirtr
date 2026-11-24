fn main() -> Result<(), Box<dyn std::error::Error>> {
    let root = std::env::current_dir()?;
    let entries = std::fs::read_dir(&root)?;
    for entry in entries {
        let entry = entry?;
        println!("{}", entry.path().display());
    }
    Ok(())
}

