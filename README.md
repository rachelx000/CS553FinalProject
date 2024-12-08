# CS 553 Final Project
## Comparing Contour Line and Morse-Smale Methods for Highlighting Symmetry in Cryo-EM Image
### Rachel Xing & Naitik Alpesh Shah

&nbsp;
### How to compile and run the Contour Line Visualization
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

#### How to use the "learnply" program:

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

&nbsp;

### How to run the Morse-Smale Segmentation
This is based on an open-source scientific visualization application called "Paraview" by Kitware Inc.

Please ensure you download version **5.11.0** from Paraview's official website: https://www.paraview.org/download/). 
After installation:
1. Navigate to **Tools** -> **Manage Plugins**
2. Locate the **Topology Toolkit** plugin
3. Check the **Auto-load** option and click **Load Selected** to enable the required plugin before running the visualization.

#### How to run the .pvsm file:
There are three **.pvsm** files corresponding to saved Paraview states of the Morse-Smale segmentation for the three cryo-EM 2D projection images.
To load the file:
1. Navigate to the **data** folder, copy the full path of the PNG image of interest.
2. Open the corresponding **.pvsm** file in a text editor, use `Ctrl+F` to locate the following line:
```bash
<Element index="0" value="/Users/rachelx000/Desktop/CS553FinalProject/data/emd_xxxxx.png"/>
```
&nbsp; &nbsp; &nbsp; &nbsp;Replace the content in **value** with the correct local path to the PNG file. 
3. Launch Paraview. In **File**, select **Load State** and choose the modified .pvsm file.
4. In the **Load State Options** prompt, select **"Search files under specified directory"**.
5. Set the data directory to the folder where the project is unzipped.
6. Click **OK** to run the visualization.

#### How to compute the Morse-Smale Segmentation for any PNG image you want:
1. Import and preprocessing: 
   - Import a **.png** file into the **"data"** folder.  
   - Add the image's filename to the list **png_file_names** in the script **Create_ply_from_png.py**.  
   - Run the script in PyCharm or Visual Studio Code. The computed **.ply** file will be exported to the **"data"** folder.
2. Running the Visualization in ParaView: 
   - Open ParaView and navigate to **View** → **Python Shell Window**.  
   - Run the script **MorseSmaleComplexPipelineParaview.py**.  
   - Adjust the following parameters in the script as needed: 
     -  `persistenceThreshold.LowerThreshold` to optimize the range of significant persistence.
     - Radius of tubes and icospheres for appropriate visualization sizes.  
3. View the Visualization in ParaView:
   - For **Persistence Diagram**:  
     1. Select **"Threshold 2"** for all persistence data and **"Tube 1"** for the axis of the persistence diagram.  
        - You can color them with a solid color.  
     2. Select **"Tube 2"** for significant persistence data and **"TTKIcospheresFromPoints1"** for critical points.  
        - Critical points can be rendered by their critical types (select **Critical Type** in its **Coloring** property).  
   - For **Morse-Smale Segmentation**:  
     1. Select **"Tube3"** for the segmentation line linking significant critical points filtered by persistence.
     2. Select **"Segmentation"**, and set the coloring to **"DescendingManifold"** to display the Morse-Smale segmentation based on the segmentation line.