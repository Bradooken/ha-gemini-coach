# 🤖 Gemini AI Morning Health Coach & Image Generator

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-FFDD00.svg?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/bradooken)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Blueprint-blue.svg?style=for-the-badge&logo=home-assistant)](https://www.home-assistant.io/)

Turn your Garmin/Health stats into a personalized, AI-generated morning briefing. 

This Blueprint analyzes your sleep and energy data to generate a **custom "Vibe" image** (using Google Imagen 4) and a **personalized coaching tip** (using Google Gemini) delivered straight to your email every morning.

<img width="636" height="687" alt="image" src="https://github.com/user-attachments/assets/14b9d418-6a1b-4694-a8ac-d269c875638a" />


---

## ✨ Features

* **Dynamic Visuals:** Generates a unique 16:9 header image every morning based on your biometric data (Sleep/Body Battery) and your chosen sport.
* **AI Coaching:** Uses the Gemini "Coach" persona to review your raw stats and provide a specific, under-60-word technical tip for your workout.
* **Sport Specific:** Supports modes for Triathlon, Running, Cycling, Swimming, and General Wellness.
* **Safety Filter Handling:** Includes "Safe" prompt engineering to prevent Google's safety filters from blocking images.

---

## ⚙️ Prerequisites (Read Carefully)

### 1. For the Data (Garmin Connect)
You need actual health data for the AI to analyze. This blueprint is designed to work with the **Garmin Connect** integration.

* **Install via HACS:** Search for "Garmin Connect".
* **Repository:** [cyberjunky/home-assistant-garmin_connect](https://github.com/cyberjunky/home-assistant-garmin_connect)
* **Verify:** Ensure you have sensors like `sensor.garmin_connect_sleep_score` available.

This automation uses two different parts of the Google AI ecosystem.

### 2. For the Text (The Coach)
You must have the **Google Generative AI Conversation** integration set up in Home Assistant.
* Go to **Settings > Devices & Services > Add Integration > Google Generative AI**.

### 3. For the Image (The Visuals)
Image generation requires the **Vertex AI API**. Standard "Free Tier" AI Studio keys often fail for image requests.
1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Select your project.
3.  Go to **APIs & Services** and enable the **Vertex AI API**.
4.  Search for "Vertex AI Model Garden", find **Imagen 4**, and click **Enable**.

---

## 🚀 Installation

### Step 1: Install the Python Script
Home Assistant cannot generate images natively via YAML. We use a small Python script to handle the API call safely.

1.  Download `gemini_image.py` from this repository.
2.  Upload it to your Home Assistant `/config` folder (the same folder where `configuration.yaml` lives).
    * *Note: Do not put it in `/www`.*

### Step 2: Update Configuration.yaml
Add the following line to your `configuration.yaml` file to allow Home Assistant to run the script.

```yaml
shell_command:
  generate_gemini_image: 'python3 /config/gemini_image.py "{{ prompt }}" "{{ api_key }}"'
```

**Restart Home Assistant** after adding this line.

### Step 3: Import the Blueprint
Click the button below to import this blueprint directly into your Home Assistant instance.

[![Open your Home Assistant instance and show the blueprint import dialog.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/bradooken/ha-gemini-coach/blob/main/gemini_health_coach.yaml)

*(Or copy the `gemini_health_coach.yaml` file to your `/config/blueprints/automation/` folder manually).*

---

## 📝 Configuration Options

| Option | Description |
| :--- | :--- |
| **Google Gemini API Key** | Your Google Cloud API Key (must have Vertex AI enabled). |
| **Sleep Sensor** | Your sleep score sensor (0-100). Works with Garmin, Oura, Whoop, etc. |
| **Energy Sensor** | Your Body Battery or Recovery score sensor (0-100). |
| **Sport Focus** | An `input_select` helper containing your sports (e.g., "Running", "Cycling"). |
| **Notification Service** | The service to send the email (e.g., `notify.gmail` or `notify.email`). |
| **Next Alarm Sensor** | (Optional) The automation triggers 5 minutes after this alarm time. |

---

## ☕ Support

If this blueprint helps you crush your morning workouts, consider buying me a coffee!

<a href="https://www.buymeacoffee.com/bradooken" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
