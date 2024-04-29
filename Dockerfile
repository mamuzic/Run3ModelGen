# Specify the image from which you are working
FROM gitlab-registry.cern.ch/sft/docker/alma9-core

# Put the current repo (the one in which this Dockerfile resides) in the directory specified here
# Note that this directory is created on the fly and does not need to reside in the repo already
ADD . /workdir

# Go into the directory specified here (again, it will create the directory if it doesn't already exist)
WORKDIR /workdir/

# Create a run directory
# RUN sudo mkdir /Tutorial/run

# Source the ATLAS analysis environment
# Make sure the directory containing your analysis code (and the code inside it) is owned by atlas user
# Build your source code using cmake
# RUN source ~/release_setup.sh &&  \
#     sudo chown -R atlas /Tutorial && \
#     cmake ../source && \
#     make
RUN source source/setup.sh && \
    mkdir build && cd build && \
    cmake ../source && \
    make && \
    source setup.sh

# Add atlas user to root group (needed to avoid permissions issues when writing files on the local machine)
# RUN source ~/release_setup.sh && sudo usermod -aG root atlas