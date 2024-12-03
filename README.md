# CS 553 Final Project
## Comparing Contour Line and Morse-Smale Methods for Highlighting Symmetry in Cryo-EM Image
### Rachel Xing & Naitik Alpesh Shah

### How to compile and run the Contour Line Method
This is based on the program called "learnply" for scientific visualization provided by Prof. Eugene Zhang @ Oregon State University.

CMake is used to compile the program, so please make sure a version of 3.5 or higher is downloaded.

The general steps to build the "learnply" program are as follows:
1. Download this project as a "`.zip`" file and unzip it
2. Direct to the folder for the unzipped file in the terminal
3. In the terminal, run the following command to compile the program:
```bash
mkdir build
cd build
cmake ..
make
```
4. To run the program with .ply for visualization, run the following command with the specific filename:
```bash
./learnply ../data/emd_1654.ply
```

How to use the "learnply" program:
1. Select a rendering mode/color scale for the scalar field:
   1. Press the key `1` - Render the scalar field with a solid color (grey in default)
   2. Press the key `2` - Render the scalar field as a wireframe model
   3. Press the key `3` - Render the scalar field in greyscale
   4. Press the key `4` - Render the scalar field in a bi-color scale (red for maxima, green for minima)
   5. Press the key `5` - Render the scalar field in a rainbow scale (red for maxima, blue for minima)
2. Press the key `h` to visualize the scalar field as a height field, where the height of each point corresponds to its scalar value. Pressing `h` again resets the scalar field to a flat view.
3. Scalar Topology Visualization: Press `s` to toggle scalar topology visualization for the input dataset.
   1. Evenly Divided Contour Line Visualization **(Technique used in this project)**:
      - Press the key `n` to divide the scalar field range [min, max] into N equal sub-intervals.  
      - The system will prompt you to enter a positive integer N.  
      - It will then compute and display the contours in light grey. You can then render them with different color scales as described in step 4.
   2. Extract a Contour Line with a Specific Value:
      - Press the key `c` to extract a contour line.  
      - The system will prompt you to enter a scalar value.  
      - If valid, it will compute and display the contour in white. 
   3. Extract and Classify Critical Points: 
      - Press the key `p` to calculate and visualize critical points.  
      - Each category of critical points is displayed in different colors:  
        - Blue: Saddle points  
        - Red: Local maxima
        - Green: Local minima  
      - Press the key `p` again to hide the critical points.  
   4. Extract and Visualize Critical Contours: 
      - Press the key `a` to compute and display all contours containing at least one saddle point in pink.  
      - Press the key `a` again to hide these contours.  
4. Rendering contour line with different color scales:
   1. Press the key `6` - Render contour lines with a solid color (light grey in default).  
   2. Press the key `7` - Render contour lines in greyscale.  
   3. Press the key `8` - Render contour lines with a bi-color scale (red for maxima, green for minima).  
   4. Press the key `9` - Render contour lines with a rainbow scale (red for maxima, blue for minima).  

