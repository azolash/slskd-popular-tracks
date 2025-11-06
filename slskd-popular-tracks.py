import json
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path

def get_filename_only(filepath):
    """Extract just the filename from a full path"""
    return os.path.basename(filepath)

def process_popular_track(data, popular_file):
    filename = get_filename_only(data['transfer'].get('filename', 'unknown_file'))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    popular_tracks = defaultdict(int)
    
    if os.path.exists(popular_file):
        try:
            with open(popular_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and '\t' in line and not line.startswith('#'):
                        parts = line.split('\t', 1)
                        if len(parts) == 2:
                            try:
                                count = int(parts[0].strip())
                                track_name = parts[1].strip()
                                popular_tracks[track_name] = count
                            except ValueError:
                                continue
        except Exception as e:
            print(f"Error reading popular file: {e}")
    
    popular_tracks[filename] += 1
    
    sorted_tracks = sorted(popular_tracks.items(), key=lambda x: (-x[1], x[0]))
    
    try:
        with open(popular_file, 'w', encoding='utf-8') as f:
            f.write("# Popular Tracks - Files sorted by upload frequency\n")
            f.write(f"# Last updated: {timestamp}\n")
            f.write("# Format: count\\tfilename (tab-separated)\n")
            f.write("# Use 'sort -n' to sort by count, 'sort -k2' to sort by filename\n\n")
            
            for track, count in sorted_tracks:
                f.write(f"{count}\t{track}\n")
        
        print(f"Updated popular tracks: {filename} (now {popular_tracks[filename]} uploads)")
        
    except Exception as e:
        print(f"Error writing popular file: {e}")

def main():
    if os.name == 'nt':
        popular_file = os.path.join(os.environ['LOCALAPPDATA'], "slskd", "scripts", "popular-tracks.txt")
    else:
        popular_file = os.path.join(os.path.expanduser("~"), ".local", "share", "slskd", "scripts", "popular-tracks.txt")
    
    os.makedirs(os.path.dirname(popular_file), exist_ok=True)
    
    json_data = os.environ.get('SLSKD_SCRIPT_DATA')
    
    if not json_data:
        print("No SLSKD_SCRIPT_DATA environment variable found")
        return
    
    try:
        data = json.loads(json_data)
        process_popular_track(data, popular_file)
    except Exception as e:
        print(f"Error processing upload data: {e}")

if __name__ == "__main__":
    main()