import gmsh
import sys
# Initialize Gmsh
gmsh.initialize()
gmsh.model.add("UnitCell")

# Create a new model
gmsh.model.add("unit_cube")

# Define geometry (e.g., a simple cube)
lc = 1.0
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(1, 1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 1, 0, lc, 4)
gmsh.model.geo.addPoint(0, 0, 1, lc, 5)
gmsh.model.geo.addPoint(1, 0, 1, lc, 6)
gmsh.model.geo.addPoint(1, 1, 1, lc, 7)
gmsh.model.geo.addPoint(0, 1, 1, lc, 8)

gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)
gmsh.model.geo.addLine(1, 5, 5)
gmsh.model.geo.addLine(2, 6, 6)
gmsh.model.geo.addLine(3, 7, 7)
gmsh.model.geo.addLine(4, 8, 8)
gmsh.model.geo.addLine(5, 6, 9)
gmsh.model.geo.addLine(6, 7, 10)
gmsh.model.geo.addLine(7, 8, 11)
gmsh.model.geo.addLine(8, 5, 12)

gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 13)
gmsh.model.geo.addPlaneSurface([13], 14)

gmsh.model.geo.addCurveLoop([5, 9, -6, -1], 14)
gmsh.model.geo.addPlaneSurface([14], 15)

gmsh.model.geo.addCurveLoop([6, 10, -7, -2], 15)
gmsh.model.geo.addPlaneSurface([15], 16)

gmsh.model.geo.addCurveLoop([7, 11, -8, -3], 16)
gmsh.model.geo.addPlaneSurface([16], 17)

gmsh.model.geo.addCurveLoop([8, 12, -5, -4], 17)
gmsh.model.geo.addPlaneSurface([17], 18)

gmsh.model.geo.addCurveLoop([9, 10, 11, 12], 18)
gmsh.model.geo.addPlaneSurface([18], 19)

gmsh.model.geo.addSurfaceLoop([14, 15, 16, 17, 18, 19], 20)
gmsh.model.geo.addVolume([20], 21)


# Synchronize to transfer the geometry to the model
gmsh.model.geo.synchronize()

# Mesh controls
#gmsh.option.setNumber("Mesh.SubdivisionAlgorithm",2); # for hex only C3D20
# Set the mesh size
gmsh.option.setNumber("Mesh.CharacteristicLengthMin", 0.5)
gmsh.option.setNumber("Mesh.CharacteristicLengthMax", 0.5)
gmsh.option.setNumber("Mesh.Optimize", 1)
# Set the element order to 2 (second-order elements)
gmsh.option.setNumber("Mesh.ElementOrder", 2)

# Generate the mesh
gmsh.model.mesh.generate(3)

# Physical groups
#bottom_tag = gmsh.model.addPhysicalGroup(2, [14])
#gmsh.model.setPhysicalName(2, bottom_tag, "bottom")

#top_tag = gmsh.model.addPhysicalGroup(2, [15])
#gmsh.model.setPhysicalName(2, top_tag, "top")

#left_tag = gmsh.model.addPhysicalGroup(2, [16])
#gmsh.model.setPhysicalName(2, left_tag, "left")

#right_tag = gmsh.model.addPhysicalGroup(2, [17])
#gmsh.model.setPhysicalName(2, right_tag, "right")

#front_tag = gmsh.model.addPhysicalGroup(2, [18])
#gmsh.model.setPhysicalName(2, front_tag, "front")

#back_tag = gmsh.model.addPhysicalGroup(2, [19])
#gmsh.model.setPhysicalName(2, back_tag, "back")

volume = gmsh.model.addPhysicalGroup(3, [21])
gmsh.model.setPhysicalName(3, volume, "Cube")

bottom_tag = gmsh.model.addPhysicalGroup(2, [14])
gmsh.model.setPhysicalName(2, bottom_tag, "bottom")

back_tag = gmsh.model.addPhysicalGroup(2, [18])
gmsh.model.setPhysicalName(2, back_tag, "back")

front_tag = gmsh.model.addPhysicalGroup(2, [16])
gmsh.model.setPhysicalName(2, front_tag, "front")

gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 1)
# Save the mesh to a file
gmsh.write("gmsh2.inp")

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

# Finalize Gmsh
gmsh.finalize()
