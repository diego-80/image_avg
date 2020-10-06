# image_avg
Compute an average image from input images

This program takes a folder of images (specified in the command-line or using the provided default) and outputs an image with the average size and pixel-wise average values from the inputs. It can be used, for example to filter out noise by keeping only persistent features in the final output.

I wrote this as part of a larger computer vision project involving locating bocce balls (see provided example images); specific instances vary from case-to-case in glare, reflection, exact orientation, and partial obscuration by the surrounding grass, but averaging even just a handful images tends to cancel out these ephemera and results in a general representation.
