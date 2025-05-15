import os
import scipy.io
from glob import glob

# === Input folders ===
image_folder = "/Users/timi/Downloads/ec/ec2/positive_images"
mat_folder = "/Users/timi/Downloads/ec/ec2/sunflower"
output_txt = "/Users/timi/Downloads/ec/ec2/annotations.txt"

# === Get all .mat files ===
mat_files = sorted(glob(os.path.join(mat_folder, "annotation_*.mat")))

lines = []

for mat_path in mat_files:
    # Extract number part (e.g., "0001")
    mat_filename = os.path.basename(mat_path)
    num_id = mat_filename.replace("annotation_", "").replace(".mat", "")
    image_filename = f"image_{num_id}.jpg"
    image_path = os.path.join(image_folder, image_filename)

    if not os.path.exists(image_path):
        print(f"Missing image for {mat_filename}")
        continue

    # Load box_coord
    mat_data = scipy.io.loadmat(mat_path)
    if "box_coord" not in mat_data:
        print(f"Missing 'box_coord' in {mat_path}")
        continue

    box = mat_data["box_coord"].flatten()  # [top, bottom, left, right]
    top, bottom, left, right = box
    x = int(left)
    y = int(top)
    w = int(right - left)
    h = int(bottom - top)

    line = f"{image_path} 1 {x} {y} {w} {h}"
    lines.append(line)

# Save annotations to file
with open(output_txt, "w") as f:
    f.write("\n".join(lines))

print(f"Saved {len(lines)} entries to {output_txt}")
