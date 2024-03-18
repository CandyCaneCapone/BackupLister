import argparse
def display_banner():
    print(r"""
  ____             _                _      _     _            
 |  _ \           | |              | |    (_)   | |           
 | |_) | __ _  ___| | ___   _ _ __ | |     _ ___| |_ ___ _ __ 
 |  _ < / _` |/ __| |/ / | | | '_ \| |    | / __| __/ _ \ '__|
 | |_) | (_| | (__|   <| |_| | |_) | |____| \__ \ ||  __/ |   
 |____/ \__,_|\___|_|\_\\__,_| .__/|______|_|___/\__\___|_|   
                             | |                              
                             |_|                            

    Backup Lister
    Tool for generating backup wordlists from a given input host.
    For example, it can generate filenames like example.bak, example.zip, etc.

    Usage: python backuplister.py -i <input_host> [-o <output_file>]
    """)

parser = argparse.ArgumentParser(description="Wordlist Generator v1")
parser.add_argument("-i", "--input", type=str, help="Enter Host")
parser.add_argument("-o", "--output", type=str, help="Output file to write the result")

  

args = parser.parse_args()

display_banner()


user_input = args.input
output_file = args.output


backup_extensions = [
    ".bak",
    ".zip",
    ".tar",
    ".tar.gz",
    ".tgz",
    ".tar.bz2",
    ".tar.xz",
    ".sql",
    ".dump",
    ".db",
]

backup_files = []

if user_input:
    for ext in backup_extensions:
        backup_files.append(user_input + ext)

    if output_file:
        with open(output_file, "w") as f:
            for file_name in backup_files:
                f.write(file_name + "\n")
        print("Result written to " + args.output)
    else:
        for file_name in backup_files : 
            print(file_name)

else:
    print("Missing flag -i or --input")
