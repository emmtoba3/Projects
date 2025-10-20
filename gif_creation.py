import imageio.v2 as iio  # quita el warning
from pathlib import Path

filenames = [
    '/Users/emmanuel/Documents/luffy1.png',
    '/Users/emmanuel/Documents/luffy2.png',
    '/Users/emmanuel/Documents/luffy3.png',
    '/Users/emmanuel/Documents/luffy4.png',
]
images = [iio.imread(f) for f in filenames]
iio.mimsave('/Users/emmanuel/Documents/team.gif', images, duration=0.5)

out_path = Path(__file__).resolve().parent / "team.gif"
iio.mimsave(out_path, images, duration=0.5)

print(f"✅ GIF created: {out_path}")
print(f"🖼️ Frames: {len(images)}  •  ⏱️ Duration per frame: 0.5s  •  🔁 Loops: infinite")