import subprocess
import os
#Code to register a moving image wrt different fixed images. In this case, an Atlas created during class wrt to fixed images given as tests
#This code is computed on the Atlas to get the transformation parameter that will be used to transform the probability map of the MNI

#Paths to elastix and transformix executables
elastix_path = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MIRRRRA/Labs/ATLAS/elastix-5.0.0-win64/elastix.exe"  # Update with your elastix path
transformix_path = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MIRRRRA/Labs/ATLAS/elastix-5.0.0-win64/transformix.exe"  # Update with your transformix path

def run_elastix(fixed_image, moving_image, output_dir, param_file):
    command = [
        elastix_path,
        "-f", fixed_image,
        "-m", moving_image,
        "-out", output_dir,
        "-p", param_file
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def run_transformix(input_image, output_dir, param_file):
    command = [
        transformix_path,
        "-in", input_image,
        "-out", output_dir,
        "-tp", param_file
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def main():
    # List of fixed images
    fixed_images = [
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1003.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1004.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1005.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1018.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1019.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1023.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1024.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1025.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1038.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1039.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1101.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1104.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1107.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1110.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1113.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1116.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1119.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1122.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1125.nii.gz",
        "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MISSSSSA/Atlas_part2/test-set/testing-images/1128.nii.gz"

    ]
  
    # Constant moving image
    moving_image = r"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\MNITemplateAtlas\template.nii\template.nii".replace("\\", "/")

    # Parameter files
    # Checkar paràmetros
    rigid_param_file = r"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\Transformation_params\Parameters.Par0009.affine.txt".replace("\\", "/")
    elastic_param_file = r"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\Transformation_params\Parameters.Par0009.elastic.txt".replace("\\", "/")

    # Directories for output
    base_rigid_output_dir = r"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\Code\Outputs_MNI\Rigid".replace("\\", "/")
    base_elastic_output_dir = r"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\Code\Outputs_MNI\NonRigid".replace("\\", "/")
    
    for fixed_image in fixed_images:
        # Create unique output directories for each fixed image
        image_name = os.path.splitext(os.path.basename(fixed_image))[0].replace("\\", "/")
        rigid_output_dir = os.path.join(base_rigid_output_dir, f"Atlas_{image_name}").replace("\\", "/")
        elastic_output_dir = os.path.join(base_elastic_output_dir, f"Atlas_{image_name}").replace("\\", "/")

        # Ensure directories exist
        os.makedirs(rigid_output_dir, exist_ok=True)
        os.makedirs(elastic_output_dir, exist_ok=True)

        # Step 1: Run Rigid Registration
        run_elastix(fixed_image, moving_image, rigid_output_dir, rigid_param_file)

        # Step 2: Run Elastic Registration Using Rigid Output
        rigid_result_image = os.path.join(rigid_output_dir, "result.0.hdr").replace("\\", "/")
        run_elastix(fixed_image, rigid_result_image, elastic_output_dir, elastic_param_file)


if __name__ == "__main__":
    main()
