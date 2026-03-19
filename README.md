<div align="center">

# 🎙️ NeuTTS Studio

<style>
@keyframes fillBar {
  0% { width: 0%; }
  100% { width: 100%; }
}

@keyframes glow {
  0% { box-shadow: 0 0 10px #00d2ff; }
  50% { box-shadow: 0 0 30px #3a7bd5; }
  100% { box-shadow: 0 0 10px #00d2ff; }
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
  100% { transform: translateY(0px); }
}

@keyframes shimmer {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

@keyframes pulse {
  0% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.8; transform: scale(1.05); }
  100% { opacity: 1; transform: scale(1); }
}

@keyframes slideIn {
  0% { transform: translateX(-20px); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}

@keyframes borderPulse {
  0% { border-color: #00d2ff; }
  50% { border-color: #3a7bd5; }
  100% { border-color: #00d2ff; }
}

@keyframes rainbowGlow {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

@keyframes countUp {
  0% { content: "0"; }
  10% { content: "1"; }
  20% { content: "2"; }
  30% { content: "3"; }
  40% { content: "4"; }
  50% { content: "5"; }
  60% { content: "6"; }
  70% { content: "7"; }
  80% { content: "8"; }
  90% { content: "9"; }
  100% { content: "10"; }
}

.progress-wrapper {
  width: 100%;
  margin: 30px 0;
}

.progress-bar-container {
  width: 100%;
  height: 50px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 30px;
  padding: 5px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  position: relative;
  margin: 15px 0;
}

.progress-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #00d2ff, #3a7bd5);
  border-radius: 30px;
  animation: fillBar 3s ease-out forwards, glow 2s ease-in-out infinite;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 20px;
  color: white;
  font-weight: bold;
  box-sizing: border-box;
}

.progress-fill::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
  animation: shimmer 2s infinite;
}

.progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-weight: bold;
  font-size: 1.3em;
  text-shadow: 0 0 10px black;
  z-index: 10;
  background: rgba(0,0,0,0.5);
  padding: 5px 20px;
  border-radius: 30px;
  border: 1px solid rgba(255,255,255,0.3);
}

.js-counter {
  font-size: 2.5em;
  font-weight: bold;
  color: #00d2ff;
  text-shadow: 0 0 20px rgba(0,210,255,0.5);
  animation: pulse 2s ease-in-out infinite;
  display: inline-block;
}

.badge {
  background: rgba(255,255,255,0.1);
  padding: 8px 20px;
  border-radius: 30px;
  display: inline-block;
  margin: 5px;
  border: 1px solid rgba(255,255,255,0.2);
  transition: all 0.3s;
  backdrop-filter: blur(5px);
  animation: float 3s ease-in-out infinite;
}

.badge:hover {
  background: rgba(255,255,255,0.2);
  transform: scale(1.05) translateY(-5px);
  border-color: #00d2ff;
  box-shadow: 0 0 20px #00d2ff;
}

.model-chip {
  display: inline-block;
  padding: 10px 20px;
  border-radius: 40px;
  margin: 5px;
  font-weight: bold;
  border-left: 4px solid;
  background: rgba(0,0,0,0.3);
  backdrop-filter: blur(5px);
  animation: float 4s ease-in-out infinite;
  transition: all 0.3s;
}

.model-chip:hover {
  transform: scale(1.05);
  box-shadow: 0 0 30px currentColor;
}

.float-icon {
  animation: float 3s ease-in-out infinite;
  display: inline-block;
  font-size: 2.5em;
  filter: drop-shadow(0 0 10px currentColor);
}

.section-header {
  background: linear-gradient(90deg, #00d2ff, #3a7bd5, #00d2ff);
  background-size: 200% 100%;
  animation: rainbowGlow 3s linear infinite;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 2em;
  font-weight: bold;
  margin: 40px 0 20px;
  text-shadow: 0 0 20px rgba(0,210,255,0.3);
  display: inline-block;
  padding: 0 20px;
}

.pulse-dot {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #00ff00;
  animation: pulse 1.5s ease-in-out infinite;
  margin-right: 8px;
  box-shadow: 0 0 15px #00ff00;
}

.comparison-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  background: rgba(255,255,255,0.05);
  border-radius: 20px;
  overflow: hidden;
  animation: slideIn 1s ease-out;
}

.comparison-table td {
  padding: 15px;
  border: 1px solid rgba(255,255,255,0.1);
  color: white;
}

.comparison-table tr:hover {
  background: rgba(0,210,255,0.1);
  transition: 0.3s;
}

.installation-step {
  background: rgba(0,0,0,0.3);
  border-left: 4px solid #00d2ff;
  padding: 15px;
  margin: 15px 0;
  border-radius: 0 15px 15px 0;
  animation: slideIn 0.5s ease-out;
  transition: all 0.3s;
}

.installation-step:hover {
  transform: translateX(10px);
  border-left-color: #3a7bd5;
  background: rgba(0,210,255,0.1);
}

.qna-box {
  background: rgba(255,255,255,0.05);
  border-radius: 15px;
  padding: 20px;
  margin: 20px 0;
  border: 1px solid rgba(255,255,255,0.1);
  transition: all 0.3s;
  animation: float 5s ease-in-out infinite;
}

.qna-box:hover {
  border-color: #00d2ff;
  box-shadow: 0 0 30px rgba(0,210,255,0.3);
  transform: scale(1.02);
}

.qna-question {
  color: #00d2ff;
  font-weight: bold;
  font-size: 1.1em;
  margin-bottom: 10px;
  animation: pulse 2s ease-in-out infinite;
}

.feature-card-animated {
  background: linear-gradient(135deg, rgba(0,210,255,0.1), rgba(58,123,213,0.1));
  border-radius: 20px;
  padding: 25px;
  margin: 15px;
  border: 1px solid rgba(255,255,255,0.1);
  transition: all 0.3s;
  animation: float 4s ease-in-out infinite;
  position: relative;
  overflow: hidden;
}

.feature-card-animated::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
  transform: rotate(45deg);
  animation: shimmer 3s infinite;
}

.feature-card-animated:hover {
  transform: scale(1.05);
  border-color: #00d2ff;
  box-shadow: 0 0 40px rgba(0,210,255,0.3);
}

.stats-number {
  font-size: 3em;
  font-weight: bold;
  background: linear-gradient(135deg, #00d2ff, #3a7bd5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: pulse 2s ease-in-out infinite;
  display: inline-block;
}

.progress-stats-bar {
  width: 100%;
  height: 30px;
  background: rgba(0,0,0,0.3);
  border-radius: 15px;
  margin: 10px 0;
  overflow: hidden;
  position: relative;
}

.progress-stats-fill {
  height: 100%;
  background: linear-gradient(90deg, #00d2ff, #3a7bd5);
  border-radius: 15px;
  animation: fillBar 2s ease-out forwards;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 10px;
  color: white;
  font-weight: bold;
  font-size: 0.9em;
}

.timeline-item {
  display: flex;
  align-items: center;
  margin: 20px 0;
  padding: 15px;
  background: rgba(255,255,255,0.03);
  border-radius: 15px;
  transition: all 0.3s;
  animation: slideIn 0.5s ease-out;
}

.timeline-item:hover {
  transform: translateX(10px);
  background: rgba(0,210,255,0.1);
}

.timeline-dot {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #00d2ff;
  margin-right: 20px;
  animation: pulse 2s ease-in-out infinite;
  box-shadow: 0 0 20px #00d2ff;
}

.glow-text {
  animation: glow 2s ease-in-out infinite;
  display: inline-block;
  padding: 5px 15px;
  border-radius: 30px;
  background: rgba(0,210,255,0.1);
}

.footer-animated {
  background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
  padding: 40px;
  border-radius: 40px;
  margin: 40px 0;
  animation: glow 4s ease-in-out infinite;
  border: 1px solid rgba(255,255,255,0.1);
}
</style>

<!-- JavaScript for live counter -->
<script>
function startCounter() {
  let count = 0;
  const counterEl = document.getElementById('live-counter');
  if (!counterEl) return;
  
  const interval = setInterval(() => {
    count += 1;
    counterEl.textContent = count + '%';
    
    if (count >= 100) {
      clearInterval(interval);
      counterEl.style.color = '#4aff4a';
    }
  }, 30);
}

window.onload = startCounter;
</script>

<!-- MAIN BANNER -->
<div style="background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); padding: 50px 30px; border-radius: 50px; max-width: 900px; margin: 30px auto; color: white; box-shadow: 0 30px 60px rgba(0,0,0,0.8); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);">

<div style="text-align: center; margin-bottom: 20px;">
  <span style="font-size: 6em; font-weight: 900; background: linear-gradient(135deg, #00d2ff 0%, #928dab 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 40px #00d2ff); letter-spacing: 4px; display: inline-block; animation: float 3s ease-in-out infinite;">NEUTTS</span>
  <div style="font-size: 2.5em; letter-spacing: 15px; margin-top: 10px; color: rgba(255,255,255,0.9); text-shadow: 0 0 30px rgba(0,210,255,0.5); animation: pulse 3s ease-in-out infinite;">STUDIO</div>
</div>

<!-- Feature Grid -->
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 50px 0;">
  <div style="text-align: center; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 30px; backdrop-filter: blur(5px); border: 1px solid rgba(255,255,255,0.1); animation: float 3s ease-in-out infinite;">
    <div class="float-icon" style="font-size: 3em;">🎤</div>
    <div style="font-weight: bold; margin: 10px 0; font-size: 1.2em;">TTS</div>
    <div style="color: #4aff4a; display: flex; align-items: center; justify-content: center; gap: 5px;"><span class="pulse-dot"></span> ONLINE</div>
  </div>
  <div style="text-align: center; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 30px; backdrop-filter: blur(5px); border: 1px solid rgba(255,255,255,0.1); animation: float 3s ease-in-out infinite 0.2s;">
    <div class="float-icon" style="font-size: 3em;">🎧</div>
    <div style="font-weight: bold; margin: 10px 0; font-size: 1.2em;">CLONE</div>
    <div style="color: #4aff4a; display: flex; align-items: center; justify-content: center; gap: 5px;"><span class="pulse-dot"></span> READY</div>
  </div>
  <div style="text-align: center; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 30px; backdrop-filter: blur(5px); border: 1px solid rgba(255,255,255,0.1); animation: float 3s ease-in-out infinite 0.4s;">
    <div class="float-icon" style="font-size: 3em;">⚡</div>
    <div style="font-weight: bold; margin: 10px 0; font-size: 1.2em;">STREAM</div>
    <div style="color: #4aff4a; display: flex; align-items: center; justify-content: center; gap: 5px;"><span class="pulse-dot"></span> ACTIVE</div>
  </div>
  <div style="text-align: center; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 30px; backdrop-filter: blur(5px); border: 1px solid rgba(255,255,255,0.1); animation: float 3s ease-in-out infinite 0.6s;">
    <div class="float-icon" style="font-size: 3em;">🔧</div>
    <div style="font-weight: bold; margin: 10px 0; font-size: 1.2em;">FINE-TUNE</div>
    <div style="color: #4aff4a; display: flex; align-items: center; justify-content: center; gap: 5px;"><span class="pulse-dot"></span> LOADED</div>
  </div>
</div>

<!-- PROGRESS BAR WITH LIVE COUNT -->
<div style="margin: 60px 0;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <span style="font-size: 1.5em; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">⚡ SYSTEM LOADING</span>
    <span id="live-counter" class="js-counter" style="font-size: 3em;">0%</span>
  </div>
  
  <div class="progress-bar-container">
    <div class="progress-fill"></div>
    <div class="progress-text">NEUTTS STUDIO READY</div>
  </div>
  
  <div style="display: flex; justify-content: space-between; margin-top: 20px; color: rgba(255,255,255,0.7); font-size: 1em; background: rgba(0,0,0,0.3); padding: 15px; border-radius: 15px;">
    <span>📊 Models: Q4 · Q8 · SafeTensors</span>
    <span class="glow-text">⚡ Speed: 150x RTF</span>
    <span>💾 All Systems Nominal</span>
  </div>
</div>

<!-- Models Display -->
<div style="margin: 50px 0;">
  <div style="text-align: center; font-size: 1.6em; margin-bottom: 30px; color: #00d2ff; text-shadow: 0 0 20px #00d2ff; animation: pulse 2s ease-in-out infinite;">⚡ AVAILABLE MODELS ⚡</div>
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
    <span class="model-chip" style="border-left-color: #00d2ff; color: #00d2ff; font-size: 1.1em; padding: 15px 25px;">🚀 Q4 GGUF · Fastest (Mobile)</span>
    <span class="model-chip" style="border-left-color: #b87aff; color: #b87aff; font-size: 1.1em; padding: 15px 25px;">⚖️ Q8 GGUF · Balanced (High-End)</span>
    <span class="model-chip" style="border-left-color: #4d4dff; color: #9999ff; font-size: 1.1em; padding: 15px 25px;">💻 SafeTensors · Best (Desktop/GPU)</span>
  </div>
</div>

<!-- Platform Badges -->
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin: 40px 0;">
  <span class="badge" style="font-size: 1em;">🐍 Python 3.10+</span>
  <span class="badge" style="font-size: 1em;">📱 Android</span>
  <span class="badge" style="font-size: 1em;">🍎 iOS</span>
  <span class="badge" style="font-size: 1em;">🐧 Linux</span>
  <span class="badge" style="font-size: 1em;">🍏 macOS</span>
  <span class="badge" style="font-size: 1em;">🪟 WSL2</span>
  <span class="badge" style="font-size: 1em;">🥧 Raspberry Pi</span>
</div>

<!-- Quote Box -->
<div style="background: linear-gradient(135deg, rgba(0,210,255,0.15) 0%, rgba(58,123,213,0.15) 100%); border-radius: 30px; padding: 30px; margin: 50px 0; border: 1px solid rgba(0,210,255,0.3); backdrop-filter: blur(5px); animation: glow 3s ease-in-out infinite;">
  <p style="margin: 0; font-size: 1.4em; line-height: 1.8; text-align: center;">
    <span style="color: #00d2ff; font-weight: bold; font-size: 1.2em;">✦ The original NeuTTS ✦</span><br>
    is built for researchers and developers.<br>
    <span style="color: #00d2ff; font-weight: bold; font-size: 1.2em;">✦ NeuTTS Studio ✦</span><br>
    is built for everyone — especially mobile users.
  </p>
</div>

<!-- Footer Icons -->
<div style="display: flex; justify-content: center; gap: 40px; margin: 40px 0;">
  <span class="float-icon" style="font-size: 3em; animation-delay: 0s;">🎙️</span>
  <span class="float-icon" style="font-size: 3em; animation-delay: 0.2s;">🎤</span>
  <span class="float-icon" style="font-size: 3em; animation-delay: 0.4s;">⚡</span>
  <span class="float-icon" style="font-size: 3em; animation-delay: 0.6s;">🎧</span>
  <span class="float-icon" style="font-size: 3em; animation-delay: 0.8s;">🔧</span>
</div>

<!-- Tagline -->
<div style="text-align: center; margin-top: 30px; font-size: 1em; color: rgba(255,255,255,0.6); letter-spacing: 4px; text-transform: uppercase; background: rgba(0,0,0,0.2); padding: 15px; border-radius: 50px;">
  On-Device TTS · Voice Cloning · Real-Time Streaming · Fine-Tuning
</div>

</div>

<br>
</div>

## 📌 Table of Contents

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 30px 0;">
  <div class="badge" style="text-align: center; padding: 15px;">📖 <a href="#-why-i-built-this" style="color: white; text-decoration: none;">Why I Built This</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">👏 <a href="#-credits--attribution" style="color: white; text-decoration: none;">Credits</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">📱 <a href="#-platform-support" style="color: white; text-decoration: none;">Platform Support</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">👍 <a href="#-model-recommendations" style="color: white; text-decoration: none;">Model Recs</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">✨ <a href="#-features" style="color: white; text-decoration: none;">Features</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">🧠 <a href="#-smart-chunking--unlimited-text-length" style="color: white; text-decoration: none;">Smart Chunking</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">🗂️ <a href="#-project-structure" style="color: white; text-decoration: none;">Project Structure</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">📦 <a href="#-installation-guides" style="color: white; text-decoration: none;">Installation</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">🚀 <a href="#-how-to-use" style="color: white; text-decoration: none;">How to Use</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">🔧 <a href="#-a-to-z-troubleshooting" style="color: white; text-decoration: none;">Troubleshooting</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">🔒 <a href="#-responsible-use" style="color: white; text-decoration: none;">Responsible Use</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">📄 <a href="#-license" style="color: white; text-decoration: none;">License</a></div>
  <div class="badge" style="text-align: center; padding: 15px;">🌐 <a href="#-links" style="color: white; text-decoration: none;">Links</a></div>
</div>

---

## <div class="section-header">📌 Why I Built This</div>

<div class="feature-card-animated">
  <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 250px;">
      <span style="font-size: 4em; display: block; text-align: center;">💡</span>
    </div>
    <div style="flex: 3;">
      <p style="font-size: 1.2em; line-height: 1.6;">The original <a href="https://github.com/neuphonic/neutts" style="color: #00d2ff;">NeuTTS</a> by <strong>Neuphonic</strong> is an incredible open-source project — state-of-the-art text-to-speech that runs on-device. But it was built for developers who are comfortable with command-line flags and technical setups.</p>
      <p style="font-size: 1.2em; line-height: 1.6;">I asked myself: <em>"Why should only developers get to use this?"</em></p>
      <p style="font-size: 1.2em; line-height: 1.6;">So I reverse-engineered the interface to create a <strong>user-friendly shell</strong> that anyone can use — no terminal expertise required. Just pick numbers from a menu and go.</p>
    </div>
  </div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 40px 0;">
  <div class="installation-step" style="background: rgba(255,0,0,0.1); border-left-color: #ff4444;">
    <div style="font-size: 1.3em; font-weight: bold; margin-bottom: 15px;">🔴 What the original looks like:</div>
    <pre style="background: rgba(0,0,0,0.5); padding: 20px; border-radius: 15px; color: #ff9999;"><code>python -m examples.basic_example \
  --input_text "Hello world" \
  --ref_audio ./samples/jo.wav \
  --ref_text ./samples/jo.txt \
  --backbone neuphonic/neutts-nano-q4-gguf \
  --output_path ./output.wav</code></pre>
  </div>
  
  <div class="installation-step" style="background: rgba(0,255,0,0.1); border-left-color: #44ff44;">
    <div style="font-size: 1.3em; font-weight: bold; margin-bottom: 15px;">🟢 What NeuTTS Studio looks like:</div>
    <pre style="background: rgba(0,0,0,0.5); padding: 20px; border-radius: 15px; color: #99ff99;"><code>python run.py
# Then just pick numbers from a menu!</code></pre>
  </div>
</div>

<table class="comparison-table">
  <tr style="background: rgba(0,210,255,0.2);">
    <th style="padding: 15px; font-size: 1.2em;">Original NeuTTS</th>
    <th style="padding: 15px; font-size: 1.2em;">NeuTTS Studio</th>
  </tr>
  <tr><td>Command-line flags</td><td>Interactive numbered menus</td></tr>
  <tr><td>Manual model each run</td><td>Load once, use everywhere</td></tr>
  <tr><td>No progress feedback</td><td>Animated progress bars with RTF stats</td></tr>
  <tr><td>30-second text limit</td><td>Unlimited text — auto-chunking</td></tr>
  <tr><td>Manual audio encoding</td><td>Auto-encode + save voice profiles</td></tr>
  <tr><td>Files save anywhere</td><td>Organized `data/outputs/` folders</td></tr>
  <tr><td>Requires developer knowledge</td><td>Anyone can use it</td></tr>
  <tr><td>Hidden cache (`~/.cache`)</td><td>Models inside project folder</td></tr>
</table>

---

## <div class="section-header">📌 Credits & Attribution</div>

<div style="background: rgba(255,0,0,0.1); border-radius: 20px; padding: 25px; margin: 30px 0; border-left: 6px solid #ff4444; animation: pulse 3s ease-in-out infinite;">
  <p style="font-size: 1.3em; margin: 0;">⚠️ <strong>This project does NOT claim ownership of any AI model.</strong></p>
</div>

<p style="font-size: 1.2em;">All TTS models, the NeuCodec audio codec, and the core inference engine are the intellectual property of <strong><a href="https://neuphonic.com" style="color: #00d2ff;">Neuphonic</a></strong>.</p>

<p style="font-size: 1.2em;">NeuTTS Studio is purely an <strong>interface layer</strong> — a user-friendly shell built around their open-source work. The models have not been modified, retrained, or redistributed in any way.</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
  <div class="model-chip" style="border-left-color: #00d2ff; text-align: center; padding: 20px;">
    <div style="font-weight: bold;">NeuTTS-Nano models</div>
    <div><a href="https://neuphonic.com" style="color: #00d2ff;">Neuphonic</a></div>
    <div style="font-size: 0.9em; opacity: 0.8;">NeuTTS Open License 1.0</div>
  </div>
  <div class="model-chip" style="border-left-color: #8a2be2; text-align: center; padding: 20px;">
    <div style="font-weight: bold;">NeuCodec audio codec</div>
    <div><a href="https://neuphonic.com" style="color: #8a2be2;">Neuphonic</a></div>
    <div style="font-size: 0.9em; opacity: 0.8;">NeuTTS Open License 1.0</div>
  </div>
  <div class="model-chip" style="border-left-color: #4d4dff; text-align: center; padding: 20px;">
    <div style="font-weight: bold;">Core inference engine</div>
    <div><a href="https://github.com/neuphonic/neutts" style="color: #4d4dff;">neuphonic/neutts</a></div>
    <div style="font-size: 0.9em; opacity: 0.8;">See repo</div>
  </div>
  <div class="model-chip" style="border-left-color: #ffaa00; text-align: center; padding: 20px;">
    <div style="font-weight: bold;">espeak-ng phonemizer</div>
    <div><a href="https://github.com/espeak-ng/espeak-ng" style="color: #ffaa00;">espeak-ng</a></div>
    <div style="font-size: 0.9em; opacity: 0.8;">GPL v3</div>
  </div>
  <div class="model-chip" style="border-left-color: #ff66aa; text-align: center; padding: 20px;">
    <div style="font-weight: bold;">Perth watermarking</div>
    <div><a href="https://github.com/resemble-ai/perth" style="color: #ff66aa;">resemble-ai/perth</a></div>
    <div style="font-size: 0.9em; opacity: 0.8;">MIT</div>
  </div>
  <div class="model-chip" style="border-left-color: #44ff44; text-align: center; padding: 20px;">
    <div style="font-weight: bold;">llama.cpp GGUF backend</div>
    <div><a href="https://github.com/ggml-org/llama.cpp" style="color: #44ff44;">ggml-org/llama.cpp</a></div>
    <div style="font-size: 0.9em; opacity: 0.8;">MIT</div>
  </div>
  <div class="model-chip" style="border-left-color: #ffffff; text-align: center; padding: 20px; grid-column: span 2;">
    <div style="font-weight: bold;">NeuTTS Studio interface</div>
    <div><strong>This project</strong></div>
    <div style="font-size: 0.9em; opacity: 0.8;">MIT</div>
  </div>
</div>

<div class="qna-box" style="background: linear-gradient(135deg, rgba(0,210,255,0.2), rgba(58,123,213,0.2));">
  <p style="font-size: 1.3em; margin: 0;"><strong>💛 Huge thanks to the entire Neuphonic team</strong> for open-sourcing such high-quality on-device TTS and making it accessible to the community.</p>
</div>

<div class="installation-step" style="background: rgba(255,215,0,0.1); border-left-color: gold;">
  <p style="font-size: 1.2em; margin: 0;"><strong>👨‍💻 My contribution:</strong> 20+ hours of debugging, reverse-engineering, and optimizing to make this work seamlessly on mobile devices — especially Android via Termux.</p>
</div>

---

## <div class="section-header">📱 Platform Support</div>

<div style="overflow-x: auto;">
  <table class="comparison-table">
    <tr style="background: rgba(0,210,255,0.2);">
      <th>Platform</th>
      <th>Status</th>
      <th>Requirements</th>
      <th>Tested On</th>
    </tr>
    <tr>
      <td><strong>Android</strong></td>
      <td><span style="color: #00ff00; animation: pulse 2s ease-in-out infinite;">✅ Optimised</span></td>
      <td>Termux + Ubuntu (via proot-distro)</td>
      <td>Galaxy A25, S23, Pixel 7</td>
    </tr>
    <tr>
      <td><strong>iOS</strong></td>
      <td><span style="color: #00ff00; animation: pulse 2s ease-in-out infinite 0.2s;">✅ Optimised</span></td>
      <td>iSH or a-Shell</td>
      <td>iPhone 14, iPad Pro</td>
    </tr>
    <tr>
      <td><strong>Linux</strong></td>
      <td><span style="color: #00ff00; animation: pulse 2s ease-in-out infinite 0.4s;">✅ Supported</span></td>
      <td>Python 3.10+, build-essential</td>
      <td>Ubuntu 22.04+, Debian, Arch</td>
    </tr>
    <tr>
      <td><strong>macOS</strong></td>
      <td><span style="color: #00ff00; animation: pulse 2s ease-in-out infinite 0.6s;">✅ Supported</span></td>
      <td>Python 3.10+, Xcode CLT</td>
      <td>Intel & Apple Silicon</td>
    </tr>
    <tr>
      <td><strong>Windows</strong></td>
      <td><span style="color: #ffaa00; animation: pulse 2s ease-in-out infinite 0.8s;">⚠️ WSL2 Required</span></td>
      <td>WSL2 with Ubuntu</td>
      <td>Windows 10/11</td>
    </tr>
    <tr>
      <td><strong>Raspberry Pi</strong></td>
      <td><span style="color: #00ff00; animation: pulse 2s ease-in-out infinite 1s;">✅ Supported</span></td>
      <td>Raspberry Pi OS</td>
      <td>Pi 4, Pi 5</td>
    </tr>
  </table>
</div>

---

## <div class="section-header">👍 Model Recommendations</div>

<div style="overflow-x: auto;">
  <table class="comparison-table">
    <tr style="background: rgba(0,210,255,0.2);">
      <th>Platform</th>
      <th>Recommended Model</th>
      <th>Why</th>
    </tr>
    <tr><td><strong>Android (High-end)</strong> 8GB+ RAM</td><td><span class="glow-text">NeuTTS-Nano Q8 GGUF</span></td><td>Better quality while staying fast on devices like S23, Pixel 7 Pro</td></tr>
    <tr><td><strong>Android (Mid-range)</strong> 4-6GB RAM</td><td><span class="glow-text">NeuTTS-Nano Q4 GGUF</span></td><td>Optimized for most phones, fastest on ARM, streaming ready</td></tr>
    <tr><td><strong>iOS (High-end)</strong> iPhone Pro Max / iPad Pro</td><td><span class="glow-text">NeuTTS-Nano Q8 GGUF</span></td><td>Take advantage of more RAM for better quality</td></tr>
    <tr><td><strong>iOS (Mid-range)</strong> Standard iPhone/iPad</td><td><span class="glow-text">NeuTTS-Nano Q4 GGUF</span></td><td>Smooth performance, lowest resource usage</td></tr>
    <tr><td><strong>Linux (High-end)</strong> 16GB+ RAM, modern CPU</td><td><span class="glow-text">NeuTTS-Nano SafeTensors</span></td><td>Best quality, finetuning capable</td></tr>
    <tr><td><strong>Linux (Mid-range)</strong> 8-16GB RAM</td><td><span class="glow-text">NeuTTS-Nano Q8 GGUF</span></td><td>Good balance of quality and speed</td></tr>
    <tr><td><strong>Linux (Low-end)</strong> 4-8GB RAM, older hardware</td><td><span class="glow-text">NeuTTS-Nano Q4 GGUF</span></td><td>If you have limited resources</td></tr>
    <tr><td><strong>macOS (Apple Silicon)</strong> M1/M2/M3</td><td><span class="glow-text">NeuTTS-Nano Q8 GGUF</span></td><td>Optimized for Apple Silicon, great performance</td></tr>
    <tr><td><strong>macOS (Intel)</strong></td><td><span class="glow-text">NeuTTS-Nano SafeTensors</span></td><td>Works natively on Intel Macs</td></tr>
    <tr><td><strong>Windows (WSL2)</strong></td><td><span class="glow-text">NeuTTS-Nano SafeTensors</span></td><td>Full performance via Ubuntu WSL2</td></tr>
    <tr><td><strong>Raspberry Pi 4/5</strong></td><td><span class="glow-text">NeuTTS-Nano Q4 GGUF</span></td><td>Only model that runs smoothly on ARM SBCs</td></tr>
  </table>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin: 40px 0;">
  <div class="model-chip" style="border-left-color: #00d2ff; text-align: center;">
    <strong>Q4 GGUF</strong> = Fastest, lowest memory, streaming ready — <strong>Best for mid-range mobile</strong>
  </div>
  <div class="model-chip" style="border-left-color: #8a2be2; text-align: center;">
    <strong>Q8 GGUF</strong> = Better quality, needs more RAM — <strong>Great for high-end mobile and Apple Silicon</strong>
  </div>
  <div class="model-chip" style="border-left-color: #4d4dff; text-align: center;">
    <strong>SafeTensors</strong> = Best quality, requires more RAM, finetuning capable — <strong>Best for desktops</strong>
  </div>
</div>

---

## <div class="section-header">✨ Features</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 25px; margin: 40px 0;">
  <div class="feature-card-animated">
    <div style="font-size: 3em; text-align: center; animation: float 3s ease-in-out infinite;">🗣️</div>
    <h3 style="color: #00d2ff; text-align: center;">Text to Speech</h3>
    <ul style="list-style-type: none; padding: 0;">
      <li class="timeline-item" style="margin: 10px 0;">✓ Type, paste, or load text from file</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ <strong>No length limit</strong> — smart auto-chunking</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Live progress bar per chunk with RTF stats</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Merge chunks OR save individually OR both</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Output saved to <code>data/outputs/tts/</code></li>
    </ul>
  </div>
  
  <div class="feature-card-animated" style="animation-delay: 0.2s;">
    <div style="font-size: 3em; text-align: center; animation: float 3s ease-in-out infinite 0.2s;">🎤</div>
    <h3 style="color: #8a2be2; text-align: center;">Voice Cloning</h3>
    <ul style="list-style-type: none; padding: 0;">
      <li class="timeline-item" style="margin: 10px 0;">✓ Clone any voice from 3+ seconds of audio</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Save as named reusable <code>.pt</code> profiles</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Test cloned voice with any phrase</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Add language & gender metadata with flags</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Output saved to <code>data/outputs/cloning/</code></li>
    </ul>
  </div>
  
  <div class="feature-card-animated" style="animation-delay: 0.4s;">
    <div style="font-size: 3em; text-align: center; animation: float 3s ease-in-out infinite 0.4s;">⚡</div>
    <h3 style="color: #ffaa00; text-align: center;">Streaming Mode</h3>
    <ul style="list-style-type: none; padding: 0;">
      <li class="timeline-item" style="margin: 10px 0;">✓ Audio plays as it generates — no waiting</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Live chunk stats: duration, gen time, RTF</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Stream to speakers only</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Stream + save simultaneously</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Output saved to <code>data/outputs/streaming/</code></li>
    </ul>
  </div>
  
  <div class="feature-card-animated" style="animation-delay: 0.6s;">
    <div style="font-size: 3em; text-align: center; animation: float 3s ease-in-out infinite 0.6s;">🔧</div>
    <h3 style="color: #ff66aa; text-align: center;">Fine Tuning</h3>
    <ul style="list-style-type: none; padding: 0;">
      <li class="timeline-item" style="margin: 10px 0;">✓ Train on your own voice data</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Interactive config builder</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Launch training from inside the app</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Resume from checkpoints</li>
      <li class="timeline-item" style="margin: 10px 0;">✓ Dataset guide built in</li>
    </ul>
  </div>
</div>

---

## <div class="section-header">🧠 Smart Chunking — Unlimited Text Length</div>

<div class="feature-card-animated">
  <p style="font-size: 1.2em;">The NeuTTS model has a <strong>2048 token context window</strong> (~30 seconds per call). NeuTTS Studio solves this automatically with a <strong>4-tier chunking strategy</strong>:</p>
</div>

<div style="background: rgba(0,0,0,0.3); border-radius: 30px; padding: 30px; margin: 40px 0; border: 1px solid #00d2ff;">
  <pre style="color: #00d2ff; font-size: 1.1em; text-align: center;">
Your text (any length — sentence, page, chapter, book)
                         ↓
     ┌─────────────────────────────────────────────┐
     │  Tier 1  ·  Split at sentence endings       │  .  !  ?
     │  Tier 2  ·  Split at clause boundaries      │  ,  ;  :
     │  Tier 3  ·  Split at word boundaries        │  spaces
     │  Tier 4  ·  Hard cut at 250 characters      │  last resort
     └─────────────────────────────────────────────┘
                         ↓
      [chunk 1]  [chunk 2]  [chunk 3]  ...  [chunk N]
                         ↓
         Same voice applied to every single chunk
                         ↓
       All chunks stitched with smooth 200ms gaps
                         ↓
              ✅  One seamless final .wav file
  </pre>
</div>

<div style="display: flex; justify-content: center; gap: 30px; margin: 30px 0; flex-wrap: wrap;">
  <div class="installation-step" style="min-width: 200px;">
    <span class="stats-number">10,000</span>
    <div>character input</div>
  </div>
  <div class="installation-step" style="min-width: 200px;">
    <span class="stats-number">→ 40</span>
    <div>chunks automatically</div>
  </div>
  <div class="installation-step" style="min-width: 200px;">
    <span class="stats-number">15 min</span>
    <div>audio generated</div>
  </div>
  <div class="installation-step" style="min-width: 200px;">
    <span class="stats-number">0</span>
    <div>manual intervention</div>
  </div>
</div>

---

## <div class="section-header">🗂️ Project Structure</div>

<div style="background: rgba(0,0,0,0.4); border-radius: 30px; padding: 30px; margin: 30px 0; border: 1px solid #00d2ff; overflow-x: auto;">
  <pre style="color: #00ff00; font-family: monospace; line-height: 1.8;">
NeuTTS-Studio/
│
├── 🚀 <span style="color: #ffff00;">run.py</span>                    ← Entry point — run this to start
├── ⚙️  <span style="color: #ffff00;">config.py</span>                 ← All settings, paths, model definitions
├── 📋 <span style="color: #ffff00;">requirements.txt</span>          ← Python dependencies
├── 📖 <span style="color: #ffff00;">README.md</span>                 ← You are here
│
├── 🧠 <span style="color: #00d2ff;">core/</span>
│   ├── engine.py                ← NeuTTS wrapper (model loading & inference)
│   ├── chunker.py               ← Smart 4-tier text splitting system
│   ├── audio.py                 ← Audio stitching, saving, file management
│   ├── ui.py                    ← Interactive menus, colors, input prompts
│   └── progress.py              ← Animated progress bars & spinners
│
├── 📦 <span style="color: #00d2ff;">modules/</span>
│   ├── tts.py                   ← Text to Speech module
│   ├── cloning.py               ← Voice Cloning module
│   ├── streaming.py             ← Streaming Mode module
│   ├── finetuning.py            ← Fine Tuning module
│   ├── settings.py              ← Settings & model management
│   └── voice_selector.py        ← Shared voice picker
│
└── 💾 <span style="color: #00d2ff;">data/</span>
    ├── voices/                  ← Your cloned voice profiles (.pt + .txt + .wav)
    ├── samples/                  ← Built-in reference voices (.wav + .txt)
    ├── models/                   ← Downloaded models cached here (NOT hidden)
    └── outputs/
        ├── tts/                  ← Audio from Text to Speech
        ├── streaming/            ← Recordings from Streaming sessions
        └── cloning/              ← Test audio from Voice Cloning
  </pre>
</div>

---

## <div class="section-header">🤖 Android Installation (Termux + Ubuntu)</div>

<div class="qna-box" style="background: rgba(255,0,0,0.2); border-left-color: #ff4444;">
  <p style="font-size: 1.3em; font-weight: bold;">⚠️ IMPORTANT — Read Before Starting</p>
  <p>Default Termux uses its own package system (<code>pkg</code>) which is <strong>missing many packages</strong> required by NeuTTS Studio such as <code>libopenblas-dev</code>, <code>portaudio19-dev</code>, <code>pkg-config</code>, <code>cmake</code> and more.</p>
  <p><strong>You MUST set up a full Ubuntu environment inside Termux first.</strong> This gives you access to the complete <code>apt-get</code> ecosystem.</p>
</div>

<div class="installation-step">
  <span style="font-size: 1.3em; font-weight: bold;">Step 0 — Install Termux</span>
</div>

<p><strong>Install Termux from F-Droid</strong> (NOT the Play Store — F-Droid version is actively maintained):</p>
<pre style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 15px;"><code>https://f-droid.org/packages/com.termux/</code></pre>

<p>Open Termux and run:</p>

<div class="installation-step">
  <pre style="background: rgba(0,0,0,0.3);"><code># Update Termux base packages
pkg update && pkg upgrade -y

# Install proot-distro — the Ubuntu manager for Termux
pkg install proot-distro -y

# Install Ubuntu
proot-distro install ubuntu

# Enter Ubuntu environment
proot-distro login ubuntu</code></pre>
</div>

<p>Your prompt will change to:</p>
<pre style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 15px;"><code>root@localhost:~#</code></pre>

<p>You are now inside a full Ubuntu environment with complete <code>apt-get</code> access.</p>

<div class="qna-box" style="background: rgba(0,210,255,0.2);">
  <p>💡 <strong>Every time you open Termux</strong>, you must re-enter Ubuntu before using NeuTTS Studio:</p>
  <pre style="background: rgba(0,0,0,0.3);"><code>proot-distro login ubuntu</code></pre>
</div>

<p><strong>Create a shortcut so you never forget:</strong></p>
<pre style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 15px;"><code># Run this in regular Termux (NOT inside Ubuntu)
echo "alias ubuntu='proot-distro login ubuntu'" >> ~/.bashrc
source ~/.bashrc

# Now just type this to enter Ubuntu anytime:
ubuntu</code></pre>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 1 — Update system packages</span>
  <pre><code>apt-get update && apt-get upgrade -y</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 2 — Install Python</span>
  <pre><code>apt-get install python3 python3-pip python3-venv -y
python3 --version   # Must be 3.10+</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 3 — Install espeak-ng</span>
  <pre><code>apt-get install espeak-ng -y
espeak-ng --version   # Must be 1.52+</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 4 — Install build tools</span>
  <pre><code>apt-get install build-essential cmake git pkg-config -y</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 5 — Install OpenBLAS</span>
  <pre><code>apt-get install libopenblas-dev -y</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 6 — Install PortAudio (for streaming)</span>
  <pre><code>apt-get install portaudio19-dev -y</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 7 — Install ffmpeg (for audio conversion)</span>
  <pre><code>apt-get install ffmpeg -y</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 8 — Create virtual environment</span>
  <pre><code>python3 -m venv ai-env
source ai-env/bin/activate</code></pre>
  <p>💡 Always run <code>source ai-env/bin/activate</code> before using the app.</p>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 9 — Clone NeuTTS Studio</span>
  <pre><code>git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 10 — Install Python dependencies</span>
  <pre><code>pip install -r requirements.txt</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 11 — Install llama-cpp-python with OpenBLAS (CRITICAL for ARM)</span>
  <pre><code>CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 12 — Add sample voices</span>
  <p>Download from <a href="https://github.com/neuphonic/neutts/tree/main/samples" style="color: #00d2ff;">original NeuTTS samples</a> and copy into <code>data/samples/</code>:</p>
  <pre><code>data/samples/
├── dave.wav  +  dave.txt     ← English male
├── jo.wav    +  jo.txt       ← English female
├── mateo.wav +  mateo.txt    ← Spanish male
├── greta.wav +  greta.txt    ← German female
└── juliette.wav + juliette.txt  ← French female</code></pre>
</div>

<div class="installation-step" style="background: rgba(0,255,0,0.2); border-left-color: #00ff00;">
  <span style="font-size: 1.3em; font-weight: bold;">Step 13 — Launch! 🚀</span>
  <pre><code>python run.py</code></pre>
</div>

---

## <div class="section-header">🍎 iOS Installation (iSH)</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 1 — Install iSH from App Store</span>
  <p>Search: <strong>iSH Shell</strong> → Download → Open</p>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 2 — Setup Alpine Linux</span>
  <pre><code>apk update && apk upgrade
apk add python3 py3-pip cmake build-base git pkgconfig
apk add espeak-ng espeak-ng-dev
apk add portaudio-dev
apk add openblas-dev
apk add ffmpeg</code></pre>
</div>

<div class="installation-step">
  <span style="font-size: 1.2em; font-weight: bold;">Step 3 — Clone and install</span>
  <pre><code>git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
pip install -r requirements.txt
CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir</code></pre>
</div>

<div class="installation-step" style="background: rgba(0,255,0,0.2); border-left-color: #00ff00;">
  <span style="font-size: 1.2em; font-weight: bold;">Step 4 — Launch</span>
  <pre><code>python run.py</code></pre>
</div>

---

## <div class="section-header">🐧 Linux Installation</div>

<div class="installation-step">
  <pre><code># Install system dependencies
sudo apt update
sudo apt install python3 python3-pip python3-venv espeak-ng \
  build-essential cmake git pkg-config libopenblas-dev portaudio19-dev \
  ffmpeg -y

# Clone and setup
git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
python3 -m venv ai-env
source ai-env/bin/activate
pip install -r requirements.txt

# Optional: For better performance on Linux
CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir

# Launch
python run.py</code></pre>
</div>

---

## <div class="section-header">🍎 macOS Installation</div>

<div class="installation-step">
  <pre><code># Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3 espeak-ng cmake pkg-config openblas portaudio ffmpeg

# Clone and setup
git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
python3 -m venv ai-env
source ai-env/bin/activate
pip install -r requirements.txt

# For Apple Silicon (M1/M2/M3), this is optimized automatically
# Launch
python run.py</code></pre>
</div>

---

## <div class="section-header">🪟 Windows Installation (WSL2)</div>

<div class="installation-step">
  <pre><code># In PowerShell (Admin)
wsl --install -d Ubuntu

# Restart your computer when prompted

# Open Ubuntu WSL terminal
# Follow Linux instructions above</code></pre>
</div>

---

## <div class="section-header">🥧 Raspberry Pi Installation</div>

<div class="installation-step">
  <pre><code>sudo apt update
sudo apt install python3 python3-pip python3-venv espeak-ng \
  build-essential cmake git pkg-config libopenblas-dev portaudio19-dev \
  ffmpeg -y

git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
python3 -m venv ai-env
source ai-env/bin/activate
pip install -r requirements.txt

# CRITICAL for Raspberry Pi ARM
CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir

# Launch
python run.py</code></pre>
</div>

---

## <div class="section-header">🚀 How to Use</div>

### Main Menu

<div style="background: rgba(0,0,0,0.4); border-radius: 20px; padding: 25px; border: 1px solid #00d2ff;">
  <pre style="color: #00ff00;">
╔══════════════════════════════════════════════════════════════╗
║  Main Menu
╚══════════════════════════════════════════════════════════════╝

  [1]  🗣️   Text to Speech     — convert text to audio with chunking
  [2]  🎤   Voice Cloning      — clone & manage voice profiles
  [3]  ⚡   Streaming Mode     — real-time audio generation
  [4]  🔧   Fine Tuning        — train on custom voice data
  [5]  ⚙️   Settings           — load model, manage outputs
  [0]  Exit

  ────────────────────────────────────────────────────────

  [0]  ← Back

  Select ❯
  </pre>
</div>

### 📝 Text to Speech

<div class="installation-step">
  <ol>
    <li>Select <code>[1] Text to Speech</code></li>
    <li>Choose input mode:
      <ul>
        <li><code>[1] Single line</code> — short sentences</li>
        <li><code>[2] Multi-paragraph</code> — paste long text (Enter twice to finish)</li>
        <li><code>[3] Load from .txt file</code> — read from file</li>
      </ul>
    </li>
    <li>Preview chunk breakdown</li>
    <li>Pick a voice (sample or your cloned voice)</li>
    <li>Choose output format:
      <ul>
        <li><code>[1] Merged single file</code> — one seamless audio</li>
        <li><code>[2] Individual chunk files</code> — per-chunk files</li>
        <li><code>[3] Both</code> — everything!</li>
      </ul>
    </li>
    <li>Watch real-time progress:</li>
  </ol>
  <pre style="background: rgba(0,0,0,0.3);"><code>  Generating [████████████████████████████] 100.0% [1/1] 12.5s ETA: 0.0s
  ✓  Generated 2.44s audio in 12.5s  ·  RTF 5.1</code></pre>
  <p>7. Audio saved to <code>data/outputs/tts/</code></p>
</div>

### 🎤 Voice Cloning

<div class="installation-step">
  <ol>
    <li>Record 3–15 seconds of clear speech on your phone</li>
    <li>Convert to WAV if needed:</li>
  </ol>
  <pre><code>ffmpeg -i recording.m4a -ar 16000 -ac 1 -sample_fmt s16 voice.wav</code></pre>
  <ol start="3">
    <li>Select <code>[2] Voice Cloning → [1] Clone new voice</code></li>
    <li>Provide:
      <ul>
        <li>Path to WAV file</li>
        <li>Exact transcript (word-for-word)</li>
        <li>Voice name</li>
        <li>Language (with flag support! 🇧🇩)</li>
        <li>Gender</li>
      </ul>
    </li>
    <li>Watch encoding progress:</li>
  </ol>
  <pre><code>    Loading encoder model...
    ✓ Encoder loaded in 16.1s
    Loading audio file...
    ✓ Audio loaded: 32000Hz, 8.9s in 10.1s
    Encoding voice...
        ✓ Encoding complete in 207.9s</code></pre>
  <p>6. Test immediately with <code>[3] Test a voice</code></p>
</div>

### ⚡ Streaming Mode

<div class="installation-step">
  <ol>
    <li>Select <code>[3] Streaming Mode</code> (GGUF model required)</li>
    <li>Choose mode:
      <ul>
        <li><code>[1] Stream to speakers</code> — live playback</li>
        <li><code>[2] Stream and save</code> — generate + save</li>
        <li><code>[3] Stream, play, and save</code> — both!</li>
      </ul>
    </li>
    <li>Type your text</li>
    <li>Watch real-time chunk stats:</li>
  </ol>
  <pre><code>  [01] TTFA   512ms audio  gen 920ms  ✅ 55% RT
  [02]        480ms audio  gen 460ms  ✅ 96% RT
  [03]        495ms audio  gen 480ms  ✅ 97% RT</code></pre>
</div>

### 🎵 Converting Any Audio Format to WAV

<div class="installation-step">
  <p>NeuTTS requires <code>.wav</code> format. Use <code>ffmpeg</code> for conversion:</p>
  <pre><code># Universal command — works for ALL formats
ffmpeg -i input_file.m4a -ar 16000 -ac 1 -sample_fmt s16 output.wav

# Examples:
ffmpeg -i recording.mp3  -ar 16000 -ac 1 voice.wav
ffmpeg -i audio.ogg      -ar 16000 -ac 1 voice.wav
ffmpeg -i sound.aac      -ar 16000 -ac 1 voice.wav
ffmpeg -i music.flac     -ar 16000 -ac 1 voice.wav</code></pre>
</div>

<p><strong>What each flag means:</strong></p>

<table class="comparison-table">
  <tr><th>Flag</th><th>Meaning</th><th>Why</th></tr>
  <tr><td><code>-i input.m4a</code></td><td>Input file</td><td>Your original recording</td></tr>
  <tr><td><code>-ar 16000</code></td><td>Sample rate = 16kHz</td><td>What NeuTTS expects</td></tr>
  <tr><td><code>-ac 1</code></td><td>Mono channel</td><td>Single speaker, no stereo</td></tr>
  <tr><td><code>-sample_fmt s16</code></td><td>16-bit PCM</td><td>Standard WAV format</td></tr>
  <tr><td><code>output.wav</code></td><td>Output filename</td><td>The file for NeuTTS</td></tr>
</table>

<p><strong>Check your converted file:</strong></p>
<pre><code>ffprobe output.wav
# Should show: Audio: pcm_s16le, 16000 Hz, mono</code></pre>

<p><strong>Trim to optimal length (3-15 seconds):</strong></p>
<pre><code># Trim from 0s to 10s
ffmpeg -i output.wav -ss 0 -t 10 trimmed.wav</code></pre>

---

## <div class="section-header">🔧 A-to-Z Troubleshooting</div>

### 🟢 Installation Issues

<div class="qna-box">
  <div class="qna-question">Q: <code>proot-distro: command not found</code></div>
  <div><strong>Cause:</strong> proot-distro not installed in Termux.</div>
  <pre><code># In regular Termux (NOT Ubuntu)
pkg update && pkg install proot-distro -y</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Ubuntu won't start after <code>proot-distro login ubuntu</code></div>
  <div><strong>Cause:</strong> Ubuntu installation corrupted.</div>
  <pre><code>proot-distro remove ubuntu
proot-distro install ubuntu
proot-distro login ubuntu</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Confused between <code>pkg</code> and <code>apt-get</code></div>
  <div>
    <ul>
      <li><code>pkg</code> = Termux (outside Ubuntu)</li>
      <li><code>apt-get</code> = Ubuntu (inside proot-distro)</li>
    </ul>
  </div>
  <pre><code># ✅ Correct — in regular Termux
pkg install proot-distro

# ✅ Correct — inside Ubuntu
apt-get install python3

# ❌ Wrong — apt-get in regular Termux
# ❌ Wrong — pkg inside Ubuntu</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Can't access Android storage from Ubuntu</div>
  <pre><code># In regular Termux (NOT Ubuntu) first
termux-setup-storage
# Grant permission when prompted

# Then inside Ubuntu, access files at:
ls /storage/emulated/0/</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Files not visible between Termux and Ubuntu</div>
  <div><strong>Cause:</strong> Ubuntu's home directory is separate.</div>
  <pre><code># Work directly in Android storage
cd /storage/emulated/0/Repository/NeuTTS-Studio
python run.py</code></pre>
</div>

### 🟡 Python & Package Issues

<div class="qna-box">
  <div class="qna-question">Q: <code>No module named 'resampy'</code></div>
  <pre><code>pip install resampy</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>PySoundFile failed</code> warning</div>
  <pre><code>pip install soundfile</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>Failed building wheel for llama-cpp-python</code></div>
  <div><strong>Cause:</strong> Build tools or OpenBLAS missing.</div>
  <pre><code>apt-get install build-essential cmake pkg-config libopenblas-dev -y

CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>ModuleNotFoundError: No module named 'torch'</code></div>
  <pre><code>source ai-env/bin/activate  # Activate venv first!
pip install -r requirements.txt</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>Could NOT find PkgConfig (missing: PKG_CONFIG_EXECUTABLE)</code></div>
  <pre><code># Android / Ubuntu
apt-get install pkg-config -y

# iOS / Alpine
apk add pkgconfig</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>portaudio.h: No such file or directory</code></div>
  <pre><code># Android / Ubuntu
apt-get install portaudio19-dev -y

# iOS / Alpine
apk add portaudio-dev</code></pre>
</div>

### 🔴 Model Loading Issues

<div class="qna-box">
  <div class="qna-question">Q: Download hangs or times out</div>
  <pre><code># Increase timeout
export HF_HUB_DOWNLOAD_TIMEOUT=60

# Or use mirror if blocked
export HF_ENDPOINT=https://hf-mirror.com

# Then run again
python run.py</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>out of memory</code> during model loading</div>
  <ul>
    <li>Switch to Q4 GGUF model (smallest)</li>
    <li>Close all other apps</li>
    <li>Restart Termux/Ubuntu session</li>
    <li>On Android: disable background apps in system settings</li>
  </ul>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>Streaming requires a GGUF model</code></div>
  <div><strong>Cause:</strong> SafeTensors model doesn't support streaming.</div>
  <p>Go to: <code>[5] Settings → [1] Load Model → Select [2] Q8 or [3] Q4</code></p>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>FileNotFoundError: Sample 'jo.wav' not found</code></div>
  <div><strong>Cause:</strong> Sample voices missing.</div>
  <p>Download from: <code>https://github.com/neuphonic/neutts/tree/main/samples</code><br>
  Copy to <code>NeuTTS-Studio/data/samples/</code></p>
</div>

### 🎤 Voice Cloning Issues

<div class="qna-box">
  <div class="qna-question">Q: Cloned voice sounds robotic or wrong</div>
  <div><strong>Checklist:</strong></div>
  <ul>
    <li>☐ Audio is 3-15 seconds long</li>
    <li>☐ Format is WAV (not MP3/M4A)</li>
    <li>☐ Sample rate 16-44kHz</li>
    <li>☐ Mono channel (not stereo)</li>
    <li>☐ No background noise</li>
    <li>☐ Transcript matches EXACTLY word for word</li>
  </ul>
  <p><strong>Fix audio:</strong></p>
  <pre><code>ffmpeg -i input.m4a -ar 16000 -ac 1 -sample_fmt s16 output.wav</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Voice cloning takes forever</div>
  <div><strong>Normal for first time:</strong></div>
  <ul>
    <li>Downloads <code>facebook/w2v-bert-2.0</code> (~2-3GB)</li>
    <li>Takes 3-5 minutes on mobile</li>
    <li><strong>Only happens once!</strong></li>
  </ul>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>list index out of range</code> error during cloning</div>
  <p>Fixed in v2.0.0 — update your code.</p>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Cloned voice sounds like it's mixing with sample voices</div>
  <p>Fixed! Now uses original transcript as reference.</p>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Converted WAV sounds distorted or too quiet</div>
  <pre><code># Normalize audio levels
ffmpeg -i input.m4a -ar 16000 -ac 1 -af "loudnorm" output.wav</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>Invalid data found when processing input</code></div>
  <pre><code># Check actual format
ffprobe your_file.m4a

# Try forcing format
ffmpeg -f mp4 -i your_file.m4a -ar 16000 -ac 1 output.wav</code></pre>
</div>

### 🟣 Terminal & Input Issues

<div class="qna-box">
  <div class="qna-question">Q: Input prompt shows garbage (e ❯)</div>
  <p>Fixed in v2.0.0 — now uses <code>></code> instead of special chars.</p>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Spinner keeps running during input</div>
  <p>Fixed with <code>InputSafeSpinner</code> class.</p>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Paste triggers auto-enter</div>
  <p>Fixed with custom <code>ask_multiline()</code> function.</p>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Progress bar stuck at 0%</div>
  <pre><code>export PYTHONUNBUFFERED=1
# Already set in run.py</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>permission denied</code> on storage path</div>
  <pre><code># Work from home directory instead
cd ~
git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio && python run.py</code></pre>
</div>

### 🟠 Performance Issues

<div class="qna-box">
  <div class="qna-question">Q: Generation is very slow</div>
  <div><strong>Normal for mobile:</strong></div>
  <ul>
    <li>50-100x real-time is expected</li>
    <li>2s audio = 100-200s on mobile CPU</li>
    <li>Switch to Q4 GGUF for 2-3x speedup</li>
  </ul>
</div>

<div class="qna-box">
  <div class="qna-question">Q: Audio has clicks/pops between chunks</div>
  <p>Edit <code>config.py</code>:</p>
  <pre><code>CHUNK_SILENCE_MS = 300  # Increase from 200ms</code></pre>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>PyAudio</code> stream underflow warning</div>
  <div><strong>Cause:</strong> CPU too slow to feed audio buffer.</div>
  <ul>
    <li>Switch to Q4 GGUF for faster generation</li>
    <li>This is a warning, not an error</li>
  </ul>
</div>

<div class="qna-box">
  <div class="qna-question">Q: <code>antlr4</code> deprecation warning</div>
  <p>Safe to ignore completely — just a packaging warning.</p>
</div>

### 🔵 Expected Performance

<div style="overflow-x: auto;">
  <table class="comparison-table">
    <tr><th>Device</th><th>Model</th><th>Speed</th><th>RTF</th></tr>
    <tr><td>Galaxy A25 (Mid-range)</td><td>Q4 GGUF</td><td>45 tok/s</td><td>50-60x</td></tr>
    <tr><td>Galaxy S23 (High-end)</td><td>Q4 GGUF</td><td>80 tok/s</td><td>30-40x</td></tr>
    <tr><td>Galaxy S23</td><td>Q8 GGUF</td><td>70 tok/s</td><td>35-45x</td></tr>
    <tr><td>Pixel 7</td><td>Q4 GGUF</td><td>70 tok/s</td><td>35-45x</td></tr>
    <tr><td>iPhone 14 (iSH)</td><td>Q4 GGUF</td><td>60 tok/s</td><td>40-50x</td></tr>
    <tr><td>iPad Pro</td><td>Q8 GGUF</td><td>90 tok/s</td><td>25-35x</td></tr>
    <tr><td>Raspberry Pi 4</td><td>Q4 GGUF</td><td>30 tok/s</td><td>80-100x</td></tr>
    <tr><td>PC (i5, no GPU)</td><td>SafeTensors</td><td>150 tok/s</td><td>15-20x</td></tr>
    <tr><td>PC (with GPU)</td><td>SafeTensors</td><td>500+ tok/s</td><td><5x</td></tr>
  </table>
</div>

<blockquote style="border-left: 4px solid #00d2ff; padding: 15px; background: rgba(0,210,255,0.1); border-radius: 0 15px 15px 0;">
  <p><strong>RTF = Real-Time Factor</strong> (lower is better)<br>
  50 tok/s ≈ 1 second of audio per second of generation</p>
</blockquote>

---

## <div class="section-header">🔒 Responsible Use</div>

<div class="feature-card-animated">
  <p>Every audio file generated includes an invisible <strong><a href="https://github.com/resemble-ai/perth" style="color: #00d2ff;">Perth watermark</a></strong> that cryptographically identifies it as AI-generated.</p>
  
  <ul style="list-style-type: none; padding: 0;">
    <li class="timeline-item">❌ Do not impersonate real people without explicit consent</li>
    <li class="timeline-item">❌ Do not generate deceptive, harmful, or fraudulent audio</li>
    <li class="timeline-item">✅ Respect the privacy and dignity of all individuals</li>
    <li class="timeline-item">✅ Follow all applicable laws in your jurisdiction</li>
    <li class="timeline-item">✅ Use for creative, educational, and personal projects</li>
  </ul>
</div>

---

## <div class="section-header">📄 License</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
  <div class="model-chip" style="border-left-color: #00d2ff; text-align: center;">
    <strong>NeuTTS Studio Interface</strong><br>
    MIT
  </div>
  <div class="model-chip" style="border-left-color: #8a2be2; text-align: center;">
    <strong>NeuTTS-Nano Models</strong><br>
    <a href="https://github.com/neuphonic/neutts/blob/main/LICENSE" style="color: #8a2be2;">NeuTTS Open License 1.0</a>
  </div>
  <div class="model-chip" style="border-left-color: #4d4dff; text-align: center;">
    <strong>NeuCodec</strong><br>
    NeuTTS Open License 1.0
  </div>
  <div class="model-chip" style="border-left-color: #ffaa00; text-align: center;">
    <strong>espeak-ng</strong><br>
    GPL v3
  </div>
  <div class="model-chip" style="border-left-color: #ff66aa; text-align: center;">
    <strong>Perth</strong><br>
    MIT
  </div>
  <div class="model-chip" style="border-left-color: #44ff44; text-align: center;">
    <strong>llama.cpp</strong><br>
    MIT
  </div>
</div>

---

## <div class="section-header">🌐 Links</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0;">
  <a href="https://github.com/neuphonic/neutts" style="text-decoration: none;">
    <div class="badge" style="display: block; text-align: center; padding: 20px;">
      🏠 Original NeuTTS repo
    </div>
  </a>
  <a href="https://neuphonic.com" style="text-decoration: none;">
    <div class="badge" style="display: block; text-align: center; padding: 20px;">
      🌍 Neuphonic website
    </div>
  </a>
  <a href="https://huggingface.co/neuphonic" style="text-decoration: none;">
    <div class="badge" style="display: block; text-align: center; padding: 20px;">
      🤗 HuggingFace models
    </div>
  </a>
  <a href="https://huggingface.co/spaces/neuphonic/neutts-nano-multilingual-collection" style="text-decoration: none;">
    <div class="badge" style="display: block; text-align: center; padding: 20px;">
      🎮 Try online
    </div>
  </a>
  <a href="https://github.com/fardin-sabid/NeuTTS-Studio/issues" style="text-decoration: none;">
    <div class="badge" style="display: block; text-align: center; padding: 20px;">
      🐛 Report issues
    </div>
  </a>
</div>

---

<div class="footer-animated" align="center">

**Made with ❤️ by Fardin Sabid**  
**🇧🇩 From Bangladesh, for the World 🌍**

<br>

<div style="font-size: 1.5em; background: linear-gradient(135deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: pulse 2s ease-in-out infinite;">
  If you can dream it, you can speak it.
</div>

<br>
After 20+ hours of debugging, reverse-engineering, and optimizing — it's finally here.

<br><br>

<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://github.com/fardin-sabid/NeuTTS-Studio">
    <div class="badge" style="font-size: 1.2em; padding: 15px 30px;">
      ⭐ Star on GitHub
    </div>
  </a>
  <a href="https://github.com/fardin-sabid">
    <div class="badge" style="font-size: 1.2em; padding: 15px 30px;">
      👤 Follow
    </div>
  </a>
</div>

<br>

<div style="display: flex; justify-content: center; gap: 30px; font-size: 3em;">
  <span class="float-icon">🎙️</span>
  <span class="float-icon" style="animation-delay: 0.2s;">🎤</span>
  <span class="float-icon" style="animation-delay: 0.4s;">⚡</span>
  <span class="float-icon" style="animation-delay: 0.6s;">🎧</span>
  <span class="float-icon" style="animation-delay: 0.8s;">🔧</span>
</div>

<br>
<strong>If you find this project useful, please ⭐ star it on GitHub!</strong>

</div>