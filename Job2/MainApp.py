import os
import subprocess

def main():
    image_directory = "../input/images_small/"
    mapper_output_file = "../output/mapper_output.txt"
    reducer_output_file = "../output/final_result.csv"

    # Run the MapReduce job with the mapper
    with open(mapper_output_file, 'w') as output_file:
        image_files = [f for f in os.listdir(image_directory) if f.endswith('.jpg')]
        for image_file in image_files:
            image_path = os.path.join(image_directory, image_file)
            try:
                subprocess.run(['python', 'mapper.py', '<', image_path], stdout=output_file, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error processing image {image_file}: {e}")

    # Read and sort the mapper output by key (Image_name)
    with open(mapper_output_file, 'r') as input_file:
        sorted_lines = sorted(input_file.readlines(), key=lambda line: line.split(',')[0])

    with open(f"{mapper_output_file}.sorted", 'w') as sorted_output_file:
        sorted_output_file.writelines(sorted_lines)

    # Run the Reducer on the sorted mapper output
    with open(reducer_output_file, 'w') as output_file:
        try:
            subprocess.run(['python', 'reducer.py', '<', f"{mapper_output_file}.sorted"], stdout=output_file, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running reducer: {e}")

    # Cleanup temporary files
    os.remove(f"{mapper_output_file}.sorted")

if __name__ == "__main__":
    main()



# #!/usr/bin/env python
#
# import os
# import subprocess
#
# def main():
#     image_directory = "../input/images_small/"
#     mapper_output_file = "../output/mapper_output.txt"
#     reducer_output_file = "../output/final_result.csv"
#
#     # Run the MapReduce job with the mapper
#     mapper_command = f"cat {image_directory}*.jpg | python mapper.py > {mapper_output_file}"
#     subprocess.run(mapper_command, shell=True)
#
#     # Sort the mapper output by key (Image_name)
#     sort_command = f"sort -t, -k1,1 {mapper_output_file} > {mapper_output_file}.sorted"
#     subprocess.run(sort_command, shell=True)
#
#     # Run the Reducer on the sorted mapper output
#     reducer_command = f"cat {mapper_output_file}.sorted | python reducer.py > {reducer_output_file}"
#     subprocess.run(reducer_command, shell=True)
#
# if __name__ == "__main__":
#     main()
