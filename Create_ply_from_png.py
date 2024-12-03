import numpy as np
from PIL import Image
from plyfile import PlyData, PlyElement

def read_png_in_greyscale(png_image_path):
    """
    Read the png image and obtain the data of its scalar field
    """
    # Read the image in grayscale
    img = Image.open(png_image_path).convert("L")

    # Resize the image to ensure the consistency among data
    img = img.resize((20, 20), Image.Resampling.LANCZOS)
    img_data = np.asarray(img)

    # Generate grid of points (x, y) with intensity as scalar value (s)
    rows, cols = img_data.shape
    x_data, y_data = np.meshgrid(np.arange(cols), np.arange(rows))
    s_data = img_data

    img_scalar_field = (x_data, y_data, s_data)
    return img_scalar_field

def generate_vertex_from_png_scalar(img_scalar_field):
    """
    Generate a grid of points (x, y) with the greyscale intensity as scalar value (s)
    """
    x_data, y_data, s_data = img_scalar_field
    vertex_data = []

    for i in range(len(x_data)):
        for j in range(len(x_data[0])):
            z, vx, vy, vz = 0, 0, 0, 0
            x = x_data[i][j]
            y = y_data[i][j]
            s = s_data[i][j]
            vertex_data.append((x, y, z, vx, vy, vz, s))

    # Format the data to fit the .ply file requirements
    vertex_data_array = np.array(vertex_data, dtype=[('x', 'float64'), ('y', 'float64'), ('z', 'float64'),
                                                     ('vx', 'float64'), ('vy', 'float64'), ('vz', 'float64'),
                                                     ('s', 'float64')])

    return vertex_data_array

def generate_face_from_png_scalar(img_scalar_field):
    """
    Create a quadrilateral grid for the scalar field
    """
    x_data, y_data, s_data = img_scalar_field

    height = len(y_data)
    width = len(x_data)

    faces = []
    for y in range(height - 1):
        for x in range(width - 1):
            # Calculate the indices of the four corners of the quadrilateral
            top_left = y * width + x
            top_right = top_left + 1
            bottom_left = (y + 1) * width + x
            bottom_right = bottom_left + 1
            # Define a quadrilateral face using these vertices
            faces.append(((top_left, top_right, bottom_right, bottom_left),))

    # Convert to numpy structured array
    face_data = np.array(faces, dtype=[('vertex_indices', 'int32', (4,))])
    return face_data

def write_ply(data_folder_path, filename, vertex_data, face_data):
    """
    Write the computed vertex and face data of the .png image into a .ply file
    """
    ply_filename = data_folder_path+filename+".ply"
    ply_vertex_data = PlyElement.describe(vertex_data, 'vertex')
    ply_face_data = PlyElement.describe(face_data, 'face')
    PlyData([ply_vertex_data, ply_face_data], text=True).write(ply_filename)


data_folder_path = "./data/"
png_file_names = ["emd_1654", "emd_19826", "emd_14435"]
for png_file_name in png_file_names:
    img_scalar_field = read_png_in_greyscale(data_folder_path+png_file_name+".png")
    vertex_data = generate_vertex_from_png_scalar(img_scalar_field)
    face_data = generate_face_from_png_scalar(img_scalar_field)
    write_ply(data_folder_path, png_file_name, vertex_data, face_data)
