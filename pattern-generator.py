"""
pattern_generator.py

This script helps generate structured pattern loader files for Automated Test Equipment (ATE),
such as Advantest V93000. It is designed for engineers who need to generate many vector loader
files programmatically for different patterns and pin groups.
"""

def wrfile(out_name, pat_name, port_name):
    text = """# Example pattern loader content
# Replace this block with your actual pattern vector structure
# This could include tester-specific commands, signal definitions, or any required headers.

# Port: {0}
# Output File: {1}@{0}
# Pattern Name: {2}

# Insert your pattern commands here (e.g., DMAS, SQLB, SQPG, etc.)
""".format(port_name, out_name, pat_name)

    try:
        with open("{}@{}.txt".format(out_name, port_name), 'w') as file:
            file.write(text)
    except Exception as e:
        print("Error writing file: {}@{} — {}".format(out_name, port_name, e))


def main():
    pattern_base = "your_pattern_prefix_"  # Replace with your actual base pattern name
    range_suffixes = [
        "0_999", "1000_1999", "2000_2999", "3000_3999", "4000_4999", "5000_5000"
    ] # Replace with your extension of your patterns

    ports = [
        ("pmf_vector_name", "actual_pin_name"),
        ("", "fallback_default_port")  # Uses full base name + suffix as pattern name
    ]

    for suffix in range_suffixes:
        out_name = "{}{}_burst".format(pattern_base, suffix)

        for pat_prefix, port in ports:
            pat_name = "{}{}".format(pattern_base, suffix) if pat_prefix == "" else pat_prefix
            wrfile(out_name, pat_name, port)

if __name__ == "__main__":
    main()
