# SLSKD POPULAR TRACKS

## Description

This is a simple python script that tracks your most popular uplaods.
It creates a txt file containing all your uploades with the number of uploads next to them.
The file will be automatically sorted showing the most popular uploads on top. 

## Example

```txt
popular-tracks.txt
# Popular Tracks - Files sorted by upload frequency
# Last updated: 2025-11-06 05:16:14
# Format: count\tfilename (tab-separated)
# Use 'sort -n' to sort by count, 'sort -k2' to sort by filename

15	Artist - Song (Extended Mix).mp3
10	Artist - Track (Original Mix).mp3
9	Singer - Song (Extended Mix).mp3
5	Singer - Track (Original Mix).mp3
```

## Requirements:
- slskd-popular-tracks.py
- Latest version of Python
- Integration in the slskd.yml file.

## Usage
Download slskd-popular-tracks.py and copy it to %localappdata%/slskd/scripts
The script will start automatically with slskd if the integration is correct and python is isntalled. 
The output folder is configured to be %localappdata%/scripts but you can change it in the code if you want. 
To make sure the script is working check the folder for new txt files called popular-tracks.txt

## Integration

locate your slskd.yml file, usually in %localappdata%/slskd
copy this piece of code to the perspective area of "integration".
Make sure the indentation stays the same or slskd won't start.
An example of slskd.yml is available to see how integration should look like.

slskd.yml

```yaml
  integration:
    scripts:
      upload_tracker:
        on:
          - UploadFileComplete
        run:
          command: 'python %localappdata%\slskd\scripts\slskd-popular-tracks.py'
```

## License
MIT

## Acknowledgement 
Thanks to slskd and its developers for creating this great software. 
