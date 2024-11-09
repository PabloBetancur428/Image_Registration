#Code to register a moving image wrt different fixed images. In this case, the probabilities maps from the MNI atlas wrt to fixed images given as tests

import subprocess
import os
import nibabel as nib


elastix_path = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MIRRRRA/Labs/ATLAS/elastix-5.0.0-win64/elastix.exe" 
transformix_path = "C:/Users/User/Desktop/UDG_old_pc/UDG/Subjects/MIRRRRA/Labs/ATLAS/elastix-5.0.0-win64/transformix.exe"  

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
    # List of fixed images paths
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
    
    
    tissues_name = {1: "bg",
                    2: "CSF",
                    3: "GM",
                    4: "WM"}
    #Tissue number to be computed: 
    tissue_num = 4

    
    # Constant moving image
    #The prob maps here are an upsampled version, because the raw images had values from 0-1 and it was causing trouble with the registration part
    moving_image = fr"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\MNITemplateAtlas\img_upsampled_maps\upsampled_tissue_{tissue_num}.nii.gz".replace("\\", "/") 


    # Directories for output
    base_rigid_output_dir = r"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\Code\Outputs_MNI\MapsRigid".replace("\\", "/")
    base_elastic_output_dir = r"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\Code\Outputs_MNI\MapsNonRigid".replace("\\", "/")
    
    for fixed_image in fixed_images: 
        patient = fixed_image.split("/")[-1].split(".")[0]
        rigid_param_file = fr"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\Code\Outputs_MNI\Rigid\Atlas_{patient}.nii\TransformParameters.0.txt".replace("\\", "/")
        elastic_param_file = fr"C:\Users\User\Desktop\UDG_old_pc\UDG\Subjects\MISSSSSA\Atlas_part2\Code\Outputs_MNI\NonRigid\Atlas_{patient}.nii\TransformParameters.0.txt".replace("\\", "/")
        
        # Create unique output directories for each fixed image
        image_name = os.path.splitext(os.path.basename(fixed_image))[0].replace("\\", "/")
        rigid_output_dir = os.path.join(base_rigid_output_dir, f"{image_name}").replace("\\", "/")
        elastic_output_dir = os.path.join(base_elastic_output_dir, f"{image_name}").replace("\\", "/")

        # Ensure directories exist
        os.makedirs(rigid_output_dir, exist_ok=True)
        os.makedirs(elastic_output_dir, exist_ok=True)

        # Step 1: Run Rigid Registration and rescale
        try:
            run_transformix(moving_image, rigid_output_dir, rigid_param_file,)
            #Read rigid image
            transformed_result_path = os.path.join(rigid_output_dir, 'result.hdr') #'result.hdr' is the name of the output image generated by transformix
            transformed_img = nib.load(transformed_result_path)
            transformed_Data = transformed_img.get_fdata()
            #Rescale image 0-1
            transformed_data_rescaled = transformed_Data/1000.0
            final_output_path = os.path.join(rigid_output_dir, f"{tissues_name[tissue_num]}_final_transformed_{image_name}.nii")
            #Save the image
            final_transformed_img = nib.Nifti1Image(transformed_data_rescaled, transformed_img.affine)
            nib.save(final_transformed_img, final_output_path)
            rigid_result_image = os.path.join(rigid_output_dir, "result.hdr").replace("\\", "/")
        except Exception as e:
            print(f"Error in rigid transformation for {image_name}: {e}")
    

        # Step 2: Run NonRigid Registration and rescale
        try: 
            run_transformix(rigid_result_image, elastic_output_dir, elastic_param_file)
            transformed_result_path_nonrigid = os.path.join(elastic_output_dir, 'result.hdr')
            transformed_img = nib.load(transformed_result_path_nonrigid)
            transformed_Data = transformed_img.get_fdata()
            #Rescale 0-1
            transformed_data_rescaled = transformed_Data/1000.0
            final_output_nonrigid_path = os.path.join(elastic_output_dir, f"{tissues_name[tissue_num]}_NonRigid_final_transformed_{image_name}.nii")
            final_transformed_img_nonrigid = nib.Nifti1Image(transformed_data_rescaled, transformed_img.affine)
            nib.save(final_transformed_img_nonrigid, final_output_nonrigid_path)
        except Exception as e:
            print(f"Error in non-rigid transformation for {image_name}: {e}")

        
if __name__ == "__main__":
    main()
