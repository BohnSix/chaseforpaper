# DenseNet and Deconvolution Neural Network (DDnet) for Volumetric Enhancement
DDnet is a convolutional neural network that is used for computed tomography image enhancement. The network uses DenseNet blocks for building feature maps and Deconvolution for image reconstruction. DDn
et shows superior performance compared to state-of-the-art CT image reconstruction/enhancement algorithms.

## How to run
Go to the respective sub-folder, on the basis of the size of CT scan, and follow steps given below.
1. Following the [Pre-processing Instruction](https://github.com/vtsynergy/2D-DECT/blob/a739ec299051f5b0526202a456994890cdd8e494/Pre-processing_Instruction.md), convert all CT scans to TIFF format (TIFF
 images must be represented in Hounds Field (HF) unit), and put all CT scans in ../2D-DECT/Images/original_data/. Each scan should be in separate folders.
The folder structure should like shown in below:
```bash
/3D-DECT
  /Images
    /original_data
      /scan1
        image1.tif
        image2.tif
        ...
      /scan2
        image1.tif
        image2.tif
        ...
      ...
```
2. Run following command to start inference using DDnet.
```
./job_batch.sh
```
## Output
Following folders are produced as output from enhancement AI.
1. reconstructed_images/test: This folder contains enhanced images generated as output from AI. Each scan is put in seperate folders. Each folder contains TIFF images.
2. visualize/test/diff_target_out: This folder contains the absolute difference maps between high-quality CT scans and enhanced CT scans in separated folders. Each folder contains TIFF images.
3. visualize/test/diff_target_in: This folder contains the absolute difference maps between high-quality CT scans and low-quality CT scans in separated folders. Each folder contains TIFF images.

