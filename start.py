import os
import re
import requests

# Set up your API key
PEXELS_API_KEY = '  '                           #ENTER your PEXEL API KEY
HEADERS = {'Authorization': PEXELS_API_KEY}
DOWNLOAD_FOLDER = 'downloads'

# Your single input string with numbered prompts

# each prompt must be either spearated by commas or
# be preceded with a number with a dot and a space  e.g. "1. MAN WALKING IN FOREST"

input_string = """

Burned warrior standing in ruins, portrait vertical,
Man alone in fiery shadows, vertical frame,
Close-up of scarred hands in dim light, vertical shot,
Ashes blowing in the wind at sunrise, tall aspect,
Intense eyes glowing in darkness, vertical crop,
Lone figure training in a shadowy gym, portrait view,
Man walking through rain with a focused face, vertical,
Person lifting weights while others sleep, vertical orientation,
Silhouette rising through smoke, vertical framing,
Stormy sky over determined lone figure, portrait layout



"""

# def parse_prompts(text):
#     # Extract prompts from numbered list
#     matches = re.findall(r"(\d+)\.\s+(.*)", text)
#     return [(int(num), prompt.strip()) for num, prompt in matches]




def parse_prompts(text):
    # Extract numbered items using regex
    numbered = [match.strip() for _, match in re.findall(r"(\d+)\.\s+(.*?)(?=\d+\.|$)", text)]

    # Extract all comma-separated segments
    comma_parts = [part.strip() for part in text.split(',') if part.strip()]

    # Combine both lists and remove duplicates while preserving order
    seen = set()
    result = []
    for item in numbered + comma_parts:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def search_and_download(prompt_num, prompt, media_type='image', count=1):
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    url = f"https://api.pexels.com/v1/search?query={prompt}&per_page={count}" if media_type == 'image' else \
          f"https://api.pexels.com/videos/search?query={prompt}&per_page={count}"

    response = requests.get(url, headers=HEADERS)
    data = response.json()

    results = data.get('photos' if media_type == 'image' else 'videos', [])

    for idx, item in enumerate(results):
        if media_type == 'image':
            file_url = item['src']['original']
            file_ext = 'jpg'
        else:
            file_url = item['video_files'][0]['link']
            file_ext = 'mp4'

        filename = f"{prompt_num}_{prompt.replace(' ', '_')}_{idx}.{file_ext}"
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)

        file_data = requests.get(file_url).content
        with open(filepath, 'wb') as f:
            f.write(file_data)

        print(f"Downloaded: {filename}")

# Run the bot
prompts = parse_prompts(input_string)
for num, prompt in enumerate(prompts):
    search_and_download(num, prompt, media_type='video', count=3)  # You can change 'image' to 'video' , 
                                                                    #change count to number of images you wanna generate
