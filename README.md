# Echo 🎙️

A child-friendly audio recording and playback device built on a Raspberry Pi 5. Press the button, speak for 4 seconds, and hear your voice played back immediately.

## How It Works

1. Press and release the button
2. The device records 4 seconds of audio through the USB microphone
3. The recording plays back immediately through the USB speaker

## Hardware

| Component | Details |
|-----------|---------|
| Raspberry Pi 5 | 1GB RAM |
| USB Microphone | Plugged into a USB port |
| USB Speaker | Plugged into a separate USB port |
| Momentary push button | Connected to GPIO pin 26 and GND |
| Enclosure | Houses all components |
| Power | USB-C cable |

## Wiring

| Button Pin | Pi Pin |
|------------|--------|
| One leg | GPIO 26 |
| Other leg | GND |

The script uses the Pi's internal pull-up resistor on GPIO 26 — no external resistor needed.

## Software

- **OS:** Raspberry Pi OS
- **Python:** Python 3
- **Dependencies:** `RPi.GPIO` (pre-installed on Raspberry Pi OS)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/edsonfox/echo.git
cd echo
```

### 2. Identify your audio devices

```bash
arecord -l   # find your microphone card number
aplay -l     # find your speaker card number
```

### 3. Update the audio device settings in `echo.py`

```python
# Update these to match your hardware
record_command = [
    "arecord",
    "-D", "sysdefault:CARD=3",  # change 3 to your mic card number
    ...
]
result = subprocess.run(["aplay", "-D", "plughw:2,0", FILE_NAME])  # change 2 to your speaker card number
```

### 4. Test manually

```bash
python echo.py
```

Press and release the button — you should hear your voice played back after 4 seconds.

### 5. Install as a systemd service (auto-start on boot)

```bash
sudo cp echo.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable echo.service
sudo systemctl start echo.service
```

### 6. Check service status

```bash
sudo systemctl status echo.service
# or follow live logs:
journalctl -u echo.service -f
```

## Files

| File | Description |
|------|-------------|
| `echo.py` | Main Python script |
| `echo.service` | systemd service file for auto-start on boot |

## Troubleshooting

**No audio playback:** Run `aplay -l` to confirm your speaker card number hasn't changed. Card numbers can shift between reboots if devices are unplugged and replugged.

**Service not starting:** Check logs with `journalctl -u echo.service -f`. Make sure the path in `echo.service` matches where you cloned the repo.

**Audio cuts off early:** This is a known intermittent issue with certain USB audio chipsets under ALSA. Recording at 48000 Hz (`-r 48000`) and using `plughw` for playback gives the best results.
