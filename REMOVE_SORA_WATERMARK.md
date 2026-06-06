# How to Remove Sora Watermark from Videos

## ✅ OFFICIAL/LEGIT METHODS:

### 1. **ChatGPT Plus/Pro Subscription**
- If you have ChatGPT Plus or Pro, videos generated should be watermark-free
- Check your account tier at: https://chatgpt.com/settings
- If still watermarked, might be a trial/preview version

### 2. **Download Original File**
- Sometimes the preview has watermark but downloaded file doesn't
- Click download button (not screenshot/screen record)
- Check the actual .mp4 file

### 3. **Crop It Out (Quick Fix)**
- If watermark is in corner/bottom
- Use video editing to crop slightly
- Tools: CapCut (free), iMovie, Canva

---

## 🛠️ TECHNICAL METHODS:

### Method A: Crop with Free Tools

**Using CapCut (Free, Mobile/Desktop):**
1. Import video
2. Select video → Crop
3. Adjust frame to cut out watermark area
4. Export in highest quality

**Using Canva (Free, Web):**
1. Create video project
2. Upload your Sora video
3. Resize/crop to remove watermark
4. Download

### Method B: Video Editing Software

**Install on Linux:**
```bash
sudo apt install kdenlive
# or
sudo apt install openshot-qt
```

**Steps:**
1. Import video
2. Add "Crop and Transform" effect
3. Crop out watermark area
4. Render video

### Method C: Command Line (if ffmpeg available)

```bash
# Crop bottom 50 pixels (if watermark is at bottom)
ffmpeg -i input.mp4 -vf "crop=in_w:in_h-50:0:0" output.mp4

# Crop right 100 pixels (if watermark on right)
ffmpeg -i input.mp4 -vf "crop=in_w-100:in_h:0:0" output.mp4
```

---

## ⚠️ IMPORTANT NOTES:

### **OpenAI's Terms:**
- Check if your Sora tier allows commercial use
- Some plans require attribution
- Read: https://openai.com/policies/terms-of-use

### **For Chore Me Marketing:**
If Sora requires watermark for your tier:
1. **Option A:** Upgrade to commercial tier (if available)
2. **Option B:** Use video as B-roll with overlay graphics covering watermark
3. **Option C:** Add your own branding on top (make it look intentional)

---

## 🎨 CREATIVE WORKAROUND:

Instead of removing, **cover it strategically:**

1. **Add Your Logo** in same corner
2. **Add CTA Button** ("Download Now") over watermark
3. **Add Subtitles/Captions** at bottom covering it
4. **Use Graphics Overlay** - put app screenshots over watermark area

This way it looks professional, not like you're hiding something!

---

## 💡 BEST PRACTICE:

**For 9-second video:**
- Watermark likely at bottom-right corner
- Add bright Chore Me logo/text overlay there
- Makes it look like branding choice, not watermark cover-up
- Bonus: reinforces your brand!

**Example:**
```
Bottom-right overlay:
🎮 Chore Me
Download Free →
```

This covers watermark + adds CTA = win-win!
