
# 🔥 Pexels Media Downloader Bot

This Python script automates the process of searching and downloading **images or videos** from [Pexels](https://www.pexels.com/) using their free API. Given a string of comma-separated prompts or a numbered list, the bot parses the input and fetches the desired media.

---

## 🚀 Features

- Parses prompts from both **comma-separated** and **numbered-list** formats.
- Downloads **images or videos** from Pexels.
- Saves files in a structured and uniquely named format.
- Automatically creates a `downloads/` folder for storing media.

---

## 🛠️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pexels-media-downloader.git
cd pexels-media-downloader
```

### 2. Install Requirements
```bash
pip install requests
```

### 3. Get Your Pexels API Key
- Sign up at [Pexels Developer Portal](https://www.pexels.com/api/)
- Copy your **API Key** and paste it into the script:

```python
PEXELS_API_KEY = 'YOUR_API_KEY_HERE'
```

---

## 📥 Usage

Update the `input_string` variable in the script with your custom prompts. Then simply run:

```bash
python downloader.py
```

You can toggle between images or videos by changing:

```python
search_and_download(num, prompt, media_type='video', count=3)
```

- Change `'video'` to `'image'` if you want photos instead.
- Change `count` to set how many results you want per prompt.

---

## 🧠 How It Works

1. **Prompt Parsing**: Supports both:
   - Numbered prompts (e.g., `1. Prompt`)
   - Comma-separated prompts

2. **Media Search**:
   - Uses the Pexels API to search for images or videos.
   - Retrieves the top `count` matches for each prompt.

3. **File Saving**:
   - Downloads media to the `/downloads` folder.
   - Filenames are prefixed with the prompt index and sanitized.

---

## 📁 Output Example

For a prompt like: `Burned warrior standing in ruins`

The output file might look like:

```
0_Burned_warrior_standing_in_ruins_0.mp4
0_Burned_warrior_standing_in_ruins_1.mp4
...
```

---

## 🧾 License

This project is licensed under the MIT License.

---

## 🤝 Contributions

PRs and suggestions are welcome! Feel free to fork and improve the project.

---

## 📸 Credits

Media content is provided by [Pexels](https://www.pexels.com/).
