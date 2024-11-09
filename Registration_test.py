#Code to register a moving image wrt different fixed images. In this case, an Atlas created during class wrt to fixed images given as tests
import subprocess
import os

# Paths to elastix and transformix executables
elastix_path = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MIRRRRA/Labs/ATLAS/elastix-5.0.0-win64/elastix.exe"  # Update with your elastix path
transformix_path = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MIRRRRA/Labs/ATLAS/elastix-5.0.0-win64/transformix.exe"  # Update with your transformix path

def run_elastix(fixed_image, moving_image, output_dir, param_file):
    """
    Run elastix with specified parameters and images.

    :param fixed_image: Path to the fixed image.
    :param moving_image: Path to the moving image.
    :param output_dir: Directory to save the output.
    :param param_file: Parameter file for transformation.
    """
    command = [
        elastix_path,  # Use the full path to elastix here
        "-f", fixed_image,
        "-m", moving_image,
        "-out", output_dir,
        "-p", param_file
    ]
    
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def run_transformix(input_image, output_dir, param_file):
    """
    Run transformix with specified parameters and input image.

    :param input_image: Path to the input image.
    :param output_dir: Directory to save the output.
    :param param_file: Parameter file for transformation.
    """
    command = [
        transformix_path,  # Use the full path to transformix here
        "-in", input_image,
        "-out", output_dir,
        "-tp", param_file
    ]
    
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def main():
    # File paths
    fixed_image = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1005.nii.gz"
    moving_image = r"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\ATLAS_our\drive-download-20241105T175009Z-001\ReslicedAtlas.nii.gz".replace("\\", "/")
    rigid_param_file = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MIRRRRA/Labs/ATLAS/transformaciones_p1/par0009/Parameters.Par0009.affine.txt"
    elastic_param_file = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MIRRRRA/Labs/ATLAS/transformaciones_p1/par0009/Parameters.Par0009.elastic.txt"

    # Output directories
    rigid_output_dir = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/Code/Outputs/Rigid/Atlas_1005"
    elastic_output_dir = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/Code/Outputs/Nonrigid/Atlas_1005"
    final_transform_output_dir = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/Code/Outputs/Final_trans"

    # Ensure output directories exist
    os.makedirs(rigid_output_dir, exist_ok=True)
    os.makedirs(elastic_output_dir, exist_ok=True)
    os.makedirs(final_transform_output_dir, exist_ok=True)

    # Step 1: Run Rigid Registration
    run_elastix(fixed_image, moving_image, rigid_output_dir, rigid_param_file)

    # Step 2: Run Elastic Registration Using Rigid Output
    rigid_result_image = os.path.join(rigid_output_dir, "result.0.nii").replace("\\", "/")
    run_elastix(fixed_image, rigid_result_image, elastic_output_dir, elastic_param_file)

    # Step 3: Apply Transformations with Transformix (Optional)
    # Change 'new_image.nii' to the path of any new image you want to apply the transformations to.
    #new_image = "new_image.nii"
    #final_transform_param = os.path.join(elastic_output_dir, "TransformParameters.1.txt").replace("\\", "/")
    #run_transformix(new_image, final_transform_output_dir, final_transform_param)

if __name__ == "__main__":
    main()

