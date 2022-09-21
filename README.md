This is a program that allows a streamlined workflow for the bridge scour project.
The idea is after gathering sonar data, this program should return 3 things
-A point shape file of the sonar
-An interpolated tiff that is masked by a predifined polygon shapefile
-Logged stats about the kriging project, including a semivariogram, variogram stats, and stats about the kriging
To use the tool, define a domain and range, and enter it into the prompt
load the csvs into the program
load the shapefile into the program
The program should run and output the above 3 things.

KRIGING TYPES:
Spherical kriging provides good resolution, but is prone to artifacting (optimal nlags is about 6)
Gaussian kriging sucks, thats about it (optimal nlags is about 8)
Exponetial kriging provides good detail, but meh resolution. Note that certain nlags create singular matrixs
that cannot be use in kriging, in this instance just try +-1 nlags (optimal nlags is about 8)
(A singular matrix is a matrix that does not have an inverse, which is needed to interpolate)

VARIOGRAM NOTES:
Variograms are nice, as they allow you to see the interpolation preformance before the execution
If you have a returned bad variogram, you can return to the main page, as executing the interpolation is processor heavy

WORKFLOW
FILES ARE INPUTED -> THE SHAPE FILE IS REPROJECTED TO EPSG 4326 -> THE SONAR DATA CSV'S ARE CONCATINATED ->  A POINT
SHAPEFILE IS MADE FROM THE CSV -> THE KRIGING IS DONE -> THE INTERPOLATION IS CLIPPED BY THE POLYGON SHAPEFILE AND
OUTPUTTED AS A TIFF.