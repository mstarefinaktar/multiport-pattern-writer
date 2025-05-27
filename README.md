# multiport-pattern-writer

This Python script automates the generation of pattern loader files used in Automated Test Equipment (ATE) environments,
such as the Advantest V93000. It is designed for test engineers who need to create structured vector loading files for
multiple port and pattern combinations.

## ✨ Features

- Dynamically generates loader files based on pattern name prefixes, suffixes, and pin ports
- Supports multiple port mappings per pattern
- Helps scale vector development for high-volume or multi-core test scenarios
- Easy to customize and extend

## 📄 Output Format

Each output file is named as:
```
<pattern_prefix>_<range>_burst@<port>.txt
```

### Example:
```
your_pattern_prefix_0_999_burst@REFCLK.txt
your_pattern_prefix_0_999_burst@CUSTOM_PORT.txt
```

## 🛠 How to Use

1. Edit `pattern_generator.py`:
   - Set your base pattern prefix in `pattern_base`
   - Adjust `range_suffixes` to match your vector splits
   - Update the `ports` list with pattern labels and tester port names

2. Run the script:
```bash
python pattern_generator.py
```

3. The script will generate `.txt` files in your current directory for each suffix and port combination.

## 🧑‍💻 Author

This tool was created to assist engineers and simplify ATE vector loader file creation. Feel free to fork or contribute!


