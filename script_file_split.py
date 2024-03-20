import os

def split_file(input_file, num_parts=10):
    file_size = os.path.getsize(input_file)
    part_size = file_size // num_parts

    with open(input_file, 'rb') as f:
        for i in range(num_parts):
            output_file = f"{input_file}_part_{i + 1}.binetflow"

            with open(output_file, 'wb') as part:
                part.write(f.read(part_size))

            print(f"Part {i + 1} created: {output_file}")

if __name__ == "__main__":
    input_file = "dataset5_capture20110815.binetflow"  # replace with your .binetflow file name
    split_file(input_file)
